#!/bin/bash -x
cl_dir=/opt/clamav
cl_home_dir=/usr/local/clamav
# Check ClamAV update

cl_old_ver=`clamscan --version | tr -s ' ' | cut -d' ' -f2 | cut -d'/' -f1`            # Old Version of ClamAV

cl_ver_file=/tmp/clamav_cl_new_version.txt     # Version File
touch $cl_ver_file

# Run freshclam to update database and to check for new version
freshclam &> $cl_ver_file

cl_new_ver=`grep 'Recommended version:' $cl_ver_file | tr -s ' ' | cut -d':' -f4 | cut -d' ' -f2`   # New Version of ClamAV
echo "WARNING: Local version: $cl_old_ver .... Recommended version: $cl_new_ver"

EMAIL_FROM="`hostname`";
EMAIL_TO="vgaurihar@gmail.com, vgaurihar@proteusdh.com, gchouhan@proteusdh.com";


# Check New Version with Current version
if [ "${cl_new_ver}" = "${cl_old_ver}" ]; then
        echo "No update for now !"
        exit
else
        echo -en "\nYour Local Version Clamav_$cl_old_ver is outdated! Kindly update it to newer one Clamav_$cl_new_ver! \nDON'T PANIC! Read http://www.clamav.net/support/faq  for installation help\n" | mail -s "Update ClamAV on `hostname`" -r $EMAIL_FROM $EMAIL_TO
        
fi

########################################################### Upgrading Clamav to newer version ##########################################################

echo "--------------------------------------------------------------Process 1 --------------------------------------------------------------------------"
# Check that newer version and go to /opt/clamav/
cd ${cl_dir}
# Check that newer version tar already exists in /opt/clamav directory  or not ....

if [ -e "clamav-${cl_new_ver}.tar.gz" ]; then

	echo "Newer version of ClamAV tar ... clamav-$cl_new_ver.tar.gz  already exists....Processing further installation...Please wait.... "
echo "--------------------------------------------------------------Process 2 --------------------------------------------------------------------------"
else
	# Download newer version by wget in above directory
	echo "Downloading newer version by wget in /opt/clamav directory....please wait...."
	wget http://sourceforge.net/projects/clamav/files/clamav/$cl_new_ver/clamav-$cl_new_ver.tar.gz
fi
sleep 5;

echo "--------------------------------------------------------------Process 2 --------------------------------------------------------------------------"
# Now go to old version's directory in /opt/clamav
echo "Now going to old version's directory in /opt/clamav"
cd ${cl_dir}/clamav-$cl_old_ver/
# Note - If directory is not there then untar it
# Copy old configuration files from current version
cp -rf ${cl_home_dir}/etc/clamd.conf ${cl_dir}
cp -rf ${cl_home_dir}/etc/freshclam.conf ${cl_dir}
# Uninstall old version
echo "Uninstalling old version.....Please wait........."
./configure; make uninstall &> /dev/null
sleep 5;


echo "--------------------------------------------------------------Process 3 --------------------------------------------------------------------------"
# Now go to '/opt/clamav/' and untar newer version...
echo "Installing and Configuring Newer Version of ClamAV ... please wait...."
cd ${cl_dir}
rm -rf clamav-$cl_new_ver/ 
chmod 755 clamav-$cl_new_ver.tar.gz
tar -xvzf clamav-${cl_new_ver}.tar.gz
cd clamav-$cl_new_ver/; ./configure --prefix=/usr/local/clamav --disable-zlib-vcheck; make; make install
sleep 5;

echo "--------------------------------------------------------------Process 4 --------------------------------------------------------------------------"
# Now go to /opt/clamav and run following commands
echo "Completing after installation process....Please wait...."
cd ${cl_dir}
echo "Copying ready configuration files.... "
cp -rf clamd.conf ${cl_home_dir}/etc/ 
cp -rf freshclam.conf ${cl_home_dir}/etc/
sleep 5;

echo "creating directory..."
mkdir –p /var/run/clamav
sleep 5;

echo "creating ownership...."
chown clamav:clamav -R /var/run/clamav/
sleep 5;

echo "creating permissions...."
chmod -R 775 /var/run/clamav
sleep 5;

echo "creating clamav directory in share directory...."
mkdir -p ${cl_home_dir}/share/clamav
sleep 5;

echo "Creating ownership for above directory...."
chown -R clamav:clamav ${cl_home_dir}/share/clamav
sleep 5;

echo "Creating socket file...."
touch /var/run/clamav/clamd.socket
sleep 5;

echo "Creating ownership for socket file....."
chown clamav:clamav -R /var/run/clamav/clamd.socket
sleep 5;

echo "Creating freshclam log file....."
touch /var/log/freshclam.log
sleep 5;

echo "Giving permission...."
chmod 600 /var/log/freshclam.log
sleep 5;

echo "Creating Ownership......"
chown clamav /var/log/freshclam.log
sleep 5;

echo 'Creating clamav directory in /var/log.....'
mkdir –p /var/log/clamav
sleep 5;

echo "Creating clamd log file...."
touch /var/log/clamav/clamd.log 
sleep 5;

echo "Giving permissions...."
chmod 600 /var/log/clamav/clamd.log 
sleep  5;

echo "Creating ownerships for clmad.log file........"
chown clamav:clamav /var/log/clamav/clamd.log
sleep 5;

echo "Creating permissions for clamd socket file........"
chmod -R 755 /var/run/clamav/clamd.socket
sleep 5;

echo "Creating softlinks for clamscan and freshclam binary....."
cd ${cl_home_dir}/bin/;  ln -s ${cl_home_dir}/bin/clamscan  /usr/bin/clamscan;  ln -s ${cl_home_dir}/bin/freshclam  /usr/bin/freshclam
sleep 5;

echo "Running  freshclam for checking and updating database..... Please wait......."
# Now run freshclam to update database
freshclam 
exit 0

