# These and other macros are documented in dhd/droid-hal-device.inc

%define device scorpion
%define vendor sony

%define vendor_pretty SONY
%define device_pretty Xperia Z3 Tablet Compact (LTE)

%define installable_zip 1
%define enable_kernel_update 1

%define straggler_files \
/selinux_version\
/service_contexts\
%{nil}

%include rpm/dhd/droid-hal-device.inc
