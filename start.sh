#/bin/bash
debug=$1
rm tmp/shm_id
if [ $debug = "debug" ]
then 
	sudo chroot . /qemu -E LD_PRELOAD="/libnvram-faker.so" -g 1234 /usr/sbin/httpd_patch
else
	sudo chroot . /qemu -E LD_PRELOAD="/libnvram-faker.so"  /usr/sbin/httpd_patch
fi
