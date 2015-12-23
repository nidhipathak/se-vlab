#!/bin/sh
#
# User account required for hosting the source code
# Note: The default user is barun -- if you change this, you need to
# manually update the settings.py file
#
# [Originally created by Chandan Gupta (IIIT-H)]
# Updated by Barun Saha (http://barunsaha.me)
# 16 March 2015, IIT Kharagpur
#

source ../scripts/common.sh

log '*** Executing configure.sh'
log $TIMESTAMP 'Host: ' $SYSTEM
log 'Current directory is: ' $CURRENT_DIR


log ' 1. Creating user barun'
USER_ID=barun
useradd -m -s /bin/bash "$USER_ID"
#* Only used for testing -- should be disabled later
echo $USER_ID:abcd | chpasswd
#* Takes effect in the next login
sudo adduser $USER_ID sudo
#*

export HOME_PATH=/home/"$USER_ID"
export SE_PATH=$HOME_PATH/codes/python/django/nb/ISAD/src/vlabs


# Directories where intermediate files would be created
log ' 2. Creating directories'
mkdir -p /var/vlabs/isad/uml/img
mkdir -p /var/vlabs/isad/cfg
mkdir -p /var/vlabs/isad/uploads/image_uploads
chown -R www-data /var/vlabs


log ' 3. Deploying code'
log "Moving codes to $HOME_PATH/codes"
mkdir -p "$HOME_PATH/codes"
cp -r codes/* "$HOME_PATH/codes/"
cp -r content "$HOME_PATH/"

# Set ownership of files
chown -R barun:www-data "$HOME_PATH/codes"
# Apache needs write permission on vlabs/ to generate two files
chmod g+w "$SE_PATH"

#echo "Copying Apache configuration file" >> $(LOG_FILE)
#cp conf/httpd.conf /etc/apache2/

#echo "Moving other configuration files" >> $(LOG_FILE)
#cp -r conf/www /usr/local/



# Create symlinks (force if already exists)
log ' 4. Creating symlinks'
ln -sf /var/vlabs/isad/ "$SE_PATH"/media/isad_erd
ln -sf /var/vlabs/isad/uploads "$SE_PATH"/media/uploads
ln -sf /var/vlabs/ "$SE_PATH"/media/vlabs
