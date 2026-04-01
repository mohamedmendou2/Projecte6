#!/bin/bash
# ============================================================================
# Script de còpia de seguretat per a Nextcloud (Instal·lació nativa)
# Autor: [El teu nom]
# Data: $(date +"%Y-%m-%d")
# Descripció: Realitza backup de la base de dades i de la carpeta data
# ============================================================================

# ========================= CONFIGURACIÓ =========================
# Directori on es guardaran els backups
BACKUP_DIR="/var/backups/nextcloud"

# Directori d'instal·lació de Nextcloud
NEXTCLOUD_DIR="/var/www/html/nextcloud"

# Directoris a incloure en el backup
DATA_DIR="$NEXTCLOUD_DIR/data"
CONFIG_DIR="$NEXTCLOUD_DIR/config"
APPS_DIR="$NEXTCLOUD_DIR/apps"

# Configuració de la base de dades
DB_NAME="nextcloud"
DB_USER="nextclouduser"
DB_PASS="1234"  # CANVIA AQUESTA CONTRASENYA

# Nombre de dies a mantenir backups
RETENTION_DAYS=7

# ========================= FUNCIONS =========================
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $1"
}

error_exit() {
    log "ERROR: $1"
    exit 1
}

# ========================= INICI =========================
clear
log "=================================================="
log "    BACKUP DE NEXTCLOUD - INSTAL·LACIÓ NATIVA"
log "=================================================="
log "Data: $(date +'%Y-%m-%d %H:%M:%S')"
log ""

# Crear directori de backups si no existeix
if [ ! -d "$BACKUP_DIR" ]; then
    log "Creant directori de backups: $BACKUP_DIR"
    sudo mkdir -p "$BACKUP_DIR"
    sudo chmod 755 "$BACKUP_DIR"
fi

# Generar nom únic per aquest backup
DATE=$(date +"%Y%m%d_%H%M%S")
BACKUP_NAME="nextcloud_backup_$DATE"
DB_BACKUP="$BACKUP_DIR/${BACKUP_NAME}_db.sql"
FILES_BACKUP="$BACKUP_DIR/${BACKUP_NAME}_files.tar.gz"

log "Nom del backup: $BACKUP_NAME"
log "Directori destí: $BACKUP_DIR"
log ""

# ========================= MANTENIMENT =========================
log "Activant mode manteniment de Nextcloud..."
sudo -u www-data php "$NEXTCLOUD_DIR/occ" maintenance:mode --on
if [ $? -ne 0 ]; then
    error_exit "No s'ha pogut activar el mode manteniment"
fi
log "✓ Mode manteniment activat"
log ""

# ========================= BACKUP BASE DE DADES =========================
log "Realitzant backup de la base de dades..."
log "  - Nom BD: $DB_NAME"
log "  - Usuari: $DB_USER"

mysqldump -u "$DB_USER" -p"$DB_PASS" "$DB_NAME" > "$DB_BACKUP" 2>/dev/null

if [ $? -eq 0 ] && [ -f "$DB_BACKUP" ]; then
    DB_SIZE=$(du -h "$DB_BACKUP" | cut -f1)
    DB_LINES=$(wc -l < "$DB_BACKUP")
    log "✓ Backup de BD completat!"
    log "  - Fitxer: $(basename $DB_BACKUP)"
    log "  - Mida: $DB_SIZE"
    log "  - Línies: $DB_LINES"
else
    sudo -u www-data php "$NEXTCLOUD_DIR/occ" maintenance:mode --off
    error_exit "Error en el backup de la base de dades"
fi
log ""

# ========================= BACKUP FITXERS =========================
log "Realitzant backup dels fitxers..."
log "  - Carpeta data: $DATA_DIR"
log "  - Carpeta config: $CONFIG_DIR"
log "  - Carpeta apps: $APPS_DIR"

sudo tar -czf "$FILES_BACKUP" "$DATA_DIR" "$CONFIG_DIR" "$APPS_DIR" 2>/dev/null

if [ $? -eq 0 ] && [ -f "$FILES_BACKUP" ]; then
    FILES_SIZE=$(du -h "$FILES_BACKUP" | cut -f1)
    log "✓ Backup de fitxers completat!"
    log "  - Fitxer: $(basename $FILES_BACKUP)"
    log "  - Mida: $FILES_SIZE"
else
    sudo -u www-data php "$NEXTCLOUD_DIR/occ" maintenance:mode --off
    error_exit "Error en el backup dels fitxers"
fi
log ""

# ========================= DESACTIVAR MANTENIMENT =========================
log "Desactivant mode manteniment de Nextcloud..."
sudo -u www-data php "$NEXTCLOUD_DIR/occ" maintenance:mode --off
log "✓ Mode manteniment desactivat"
log ""

# ========================= NETEGAR BACKUPS ANTICS =========================
log "Netejant backups antics (més de $RETENTION_DAYS dies)..."
find "$BACKUP_DIR" -type f -name "*.sql" -mtime +$RETENTION_DAYS -delete
find "$BACKUP_DIR" -type f -name "*.tar.gz" -mtime +$RETENTION_DAYS -delete
find "$BACKUP_DIR" -type f -name "*.log" -mtime +$RETENTION_DAYS -delete
log "✓ Neteja completada"
log ""

# ========================= INFORMACIÓ DE L'ESPai =========================
TOTAL_SIZE=$(du -sh "$BACKUP_DIR" | cut -f1)
BACKUP_COUNT=$(find "$BACKUP_DIR" -type f \( -name "*.sql" -o -name "*.tar.gz" \) | wc -l)

log "=================================================="
log "           RESUM DEL BACKUP"
log "=================================================="
log "✅ Backup completat amb èxit!"
log ""
log "📁 Ubicació: $BACKUP_DIR"
log "📊 Espai total utilitzat: $TOTAL_SIZE"
log "📄 Nombre de backups: $BACKUP_COUNT"
log ""
log "Fitxers generats:"
log "  🗄️  BD: $(basename $DB_BACKUP) ($DB_SIZE)"
log "  📦 Fitxers: $(basename $FILES_BACKUP) ($FILES_SIZE)"
log ""
log "📋 Per restaurar:"
log "  - Base de dades: mysql -u $DB_USER -p $DB_NAME < $DB_BACKUP"
log "  - Fitxers: tar -xzf $FILES_BACKUP -C /"
log ""
log "=================================================="

# Crear fitxer de log
LOG_FILE="$BACKUP_DIR/backup_$DATE.log"
echo "Backup completat: $(date)" > "$LOG_FILE"
echo "BD: $DB_BACKUP ($DB_SIZE)" >> "$LOG_FILE"
echo "Fitxers: $FILES_BACKUP ($FILES_SIZE)" >> "$LOG_FILE"
log "Log guardat a: $LOG_FILE"
