%define kmod_name		bnxt_en
%define kmod_vendor		redhat
%define kmod_driver_version	1.10.0_dup8.1
%define kmod_driver_epoch	%{nil}
%define kmod_rpm_release	2
%define kmod_kernel_version	4.18.0-147.el8
%define kmod_kernel_version_min	%{nil}
%define kmod_kernel_version_dep	%{nil}
%define kmod_kbuild_dir		drivers/net/ethernet/broadcom/bnxt
%define kmod_dependencies       %{nil}
%define kmod_dist_build_deps	%{nil}
%define kmod_build_dependencies	%{nil}
%define kmod_devel_package	0
%define kmod_install_path	extra/kmod-redhat-bnxt_en
%define kernel_pkg		kernel
%define kernel_devel_pkg	kernel-devel
%define kernel_modules_pkg	kernel-modules

%{!?dist: %define dist .el8_1}
%{!?make_build: %define make_build make}

%if "%{kmod_kernel_version_dep}" == ""
%define kmod_kernel_version_dep %{kmod_kernel_version}
%endif

%if "%{kmod_dist_build_deps}" == ""
%if (0%{?rhel} > 7) || (0%{?centos} > 7)
%define kmod_dist_build_deps redhat-rpm-config kernel-abi-whitelists elfutils-libelf-devel kernel-rpm-macros kmod
%else
%define kmod_dist_build_deps redhat-rpm-config kernel-abi-whitelists
%endif
%endif

Source0:	%{kmod_name}-%{kmod_vendor}-%{kmod_driver_version}.tar.bz2
# Source code patches
Patch0:	0001-netdrv-linux-dim-Fix-overflow-in-dim-calculation.patch
Patch1:	0002-netdrv-bnxt_en-Add-bnxt_en-initial-port-params-table.patch
Patch2:	0003-netdrv-revert-devlink-Add-a-generic-wake_on_lan-port.patch
Patch3:	0004-netdrv-bnxt-add-missing-net-devlink.h-include.patch
Patch4:	0005-netdrv-bnxt-set-devlink-port-attrs-properly.patch
Patch5:	0006-netdrv-bnxt-call-devlink_port_type_eth_set-before-po.patch
Patch6:	0007-netdrv-bnxt-set-devlink-port-type-after-registration.patch
Patch7:	0009-netdrv-bnx2x-Mark-expected-switch-fall-throughs.patch
Patch8:	0010-netdrv-bnx2x-Mark-expected-switch-fall-thoughs.patch
Patch9:	0011-netdrv-bnxt_en-Fix-firmware-signaled-resource-change.patch
Patch10:	0012-netdrv-cross-tree-phase-out-dma_zalloc_coherent.patch
Patch11:	0013-netdrv-bnxt-Implement-ndo_get_port_parent_id.patch
Patch12:	0016-netdrv-bnxt-move-bp-switch_id-initialization-to-PF-p.patch
Patch13:	0018-netdrv-bnxt_en-Update-firmware-interface-to-1.10.0.6.patch
Patch14:	0019-netdrv-bnxt_en-Refactor-bnxt_alloc_stats.patch
Patch15:	0020-netdrv-bnxt_en-Add-support-for-PCIe-statistics.patch
Patch16:	0021-netdrv-bnxt_en-Check-new-firmware-capability-to-disp.patch
Patch17:	0022-netdrv-bnxt_en-Read-package-version-from-firmware.patch
Patch18:	0023-netdrv-bnxt_en-read-the-clause-type-from-the-PHY-ID.patch
Patch19:	0024-netdrv-bnxt_en-Separate-RDMA-MR-AH-context-allocatio.patch
Patch20:	0025-netdrv-bnxt_en-Query-firmware-capability-to-support-.patch
Patch21:	0026-netdrv-bnxt_en-Add-support-for-aRFS-on-57500-chips.patch
Patch22:	0027-netdrv-bnxt_en-Device-serial-number-is-supported-onl.patch
Patch23:	0028-netdrv-bnxt_en-rename-some-xdp-functions.patch
Patch24:	0029-netdrv-bnxt_en-Refactor-__bnxt_xmit_xdp.patch
Patch25:	0030-netdrv-bnxt_en-optimized-XDP_REDIRECT-support.patch
Patch26:	0031-netdrv-bnxt_en-add-page_pool-support.patch
Patch27:	0032-netdrv-bnxt_en-Add-page_pool_destroy-during-RX-ring-.patch
Patch28:	0033-netdrv-bnxt_en-Fix-VNIC-accounting-when-enabling-aRF.patch
Patch29:	0034-netdrv-bnxt_en-Fix-VNIC-clearing-logic-for-57500-chi.patch
Patch30:	0035-netdrv-bnxt_en-Improve-RX-doorbell-sequence.patch
Patch31:	0036-netdrv-bnxt_en-Fix-handling-FRAG_ERR-when-NVM_INSTAL.patch
Patch32:	0037-netdrv-bnxt_en-Use-correct-src_fid-to-determine-dire.patch
Patch33:	0038-netdrv-bnxt_en-Fix-to-include-flow-direction-in-L2-k.patch
Patch34:	0039-netdrv-bnxt_en-Suppress-HWRM-errors-for-HWRM_NVM_GET.patch
Patch35:	0040-netdrv-bnxt_en-Update-firmware-interface-spec.-to-1..patch
Patch36:	0041-netdrv-bnxt_en-Add-TPA-structure-definitions-for-BCM.patch
Patch37:	0042-netdrv-bnxt_en-Refactor-TPA-logic.patch
Patch38:	0043-netdrv-bnxt_en-Expand-bnxt_tpa_info-struct-to-suppor.patch
Patch39:	0044-netdrv-bnxt_en-Handle-standalone-RX_AGG-completions.patch
Patch40:	0045-netdrv-bnxt_en-Refactor-tunneled-hardware-GRO-logic.patch
Patch41:	0046-netdrv-bnxt_en-Set-TPA-GRO-mode-flags-on-57500-chips.patch
Patch42:	0047-netdrv-bnxt_en-Add-fast-path-logic-for-TPA-on-57500-.patch
Patch43:	0048-netdrv-bnxt_en-Add-TPA-ID-mapping-logic-for-57500-ch.patch
Patch44:	0049-netdrv-bnxt_en-Add-hardware-GRO-setup-function-for-5.patch
Patch45:	0050-netdrv-bnxt_en-Refactor-ethtool-ring-statistics-logi.patch
Patch46:	0051-netdrv-bnxt_en-Allocate-the-larger-per-ring-statisti.patch
Patch47:	0052-netdrv-bnxt_en-Support-TPA-counters-on-57500-chips.patch
Patch48:	0053-netdrv-bnxt_en-Refactor-bnxt_init_one-and-turn-on-TP.patch
Patch49:	0054-netdrv-bnxt_en-Support-all-variants-of-the-5750X-chi.patch
Patch50:	0055-netdrv-bnxt_en-Add-PCI-IDs-for-57500-series-NPAR-dev.patch
Patch51:	0056-netdrv-bnxt-no-need-to-check-return-value-of-debugfs.patch
Patch52:	0057-netdrv-bnxt_en-Fix-allocation-of-zero-statistics-blo.patch
Patch53:	0058-netdrv-bnxt_en-Use-a-common-function-to-print-the-sa.patch
Patch54:	0059-netdrv-bnxt_en-Remove-the-1-error-return-code-from-b.patch
Patch55:	0060-netdrv-bnxt_en-Convert-error-code-in-firmware-messag.patch
Patch56:	0061-netdrv-bnxt_en-Simplify-error-checking-in-the-SR-IOV.patch
Patch57:	0062-netdrv-bnxt_en-Suppress-all-error-messages-in-hwrm_d.patch
Patch58:	0063-netdrv-bnxt_en-Prepare-bnxt_init_one-to-be-called-mu.patch
Patch59:	0064-netdrv-bnxt_en-Refactor-bnxt_sriov_enable.patch
Patch60:	0065-netdrv-bnxt_en-Register-buffers-for-VFs-before-reser.patch
Patch61:	0066-netdrv-bnxt_en-Handle-firmware-reset-status-during-I.patch
Patch62:	0067-netdrv-bnxt_en-Discover-firmware-error-recovery-capa.patch
Patch63:	0068-netdrv-bnxt_en-Pre-map-the-firmware-health-monitorin.patch
Patch64:	0069-netdrv-bnxt_en-Enable-health-monitoring.patch
Patch65:	0070-netdrv-bnxt_en-Add-BNXT_STATE_IN_FW_RESET-state.patch
Patch66:	0071-netdrv-bnxt_en-Add-new-FW-devlink_health_reporter.patch
Patch67:	0072-netdrv-bnxt_en-Handle-RESET_NOTIFY-async-event-from-.patch
Patch68:	0073-netdrv-bnxt_en-Handle-firmware-reset.patch
Patch69:	0074-netdrv-bnxt_en-Add-devlink-health-reset-reporter.patch
Patch70:	0075-netdrv-bnxt_en-Retain-user-settings-on-a-VF-after-RE.patch
Patch71:	0076-netdrv-bnxt_en-Do-not-send-firmware-messages-if-firm.patch
Patch72:	0077-netdrv-bnxt_en-Add-RESET_FW-state-logic-to-bnxt_fw_r.patch
Patch73:	0078-netdrv-bnxt_en-Add-bnxt_fw_exception-to-handle-fatal.patch
Patch74:	0079-netdrv-bnxt_en-Add-FW-fatal-devlink_health_reporter.patch
Patch75:	0080-netdrv-bnxt_en-Fix-compile-error-regression-with-CON.patch
Patch76:	0081-netdrv-bnxt_en-Don-t-proceed-in-.ndo_set_rx_mode-whe.patch
Patch77:	0082-netdrv-bnxt_en-Increase-timeout-for-HWRM_DBG_COREDUM.patch
Patch78:	0083-netdrv-bnxt_en-Update-firmware-interface-spec.-to-1..patch
Patch79:	0084-netdrv-bnxt_en-Add-a-new-BNXT_FW_RESET_STATE_POLL_FW.patch
Patch80:	0085-netdrv-bnxt_en-Fix-the-size-of-devlink-MSIX-paramete.patch
Patch81:	0086-netdrv-bnxt_en-Fix-devlink-NVRAM-related-byte-order-.patch
Patch82:	0087-netdrv-bnxt_en-Adjust-the-time-to-wait-before-pollin.patch
Patch83:	0088-netdrv-bnxt_en-Minor-formatting-changes-in-FW-devlin.patch
Patch84:	0089-netdrv-bnxt_en-Avoid-disabling-pci-device-in-bnxt_re.patch
Patch85:	0090-netdrv-broadcom-bnxt-Fix-use-true-false-for-bool.patch
Patch86:	0091-netdrv-bnxt_en-Add-support-to-invoke-OP-TEE-API-to-r.patch
Patch87:	0092-netdrv-bnxt_en-Add-support-to-collect-crash-dump-via.patch
Patch88:	0093-netdrv-bnxt-Avoid-logging-an-unnecessary-message-whe.patch
Patch89:	0094-netdrv-bnxt_en-Improve-bnxt_ulp_stop-bnxt_ulp_start-.patch
Patch90:	0095-netdrv-bnxt_en-Call-bnxt_ulp_stop-bnxt_ulp_start-dur.patch
Patch91:	0096-netdrv-bnxt_en-Call-bnxt_ulp_stop-bnxt_ulp_start-dur.patch
Patch92:	9000-bump-driver-version.patch

%define findpat %( echo "%""P" )
%define __find_requires /usr/lib/rpm/redhat/find-requires.ksyms
%define __find_provides /usr/lib/rpm/redhat/find-provides.ksyms %{kmod_name} %{?epoch:%{epoch}:}%{version}-%{release}
%define sbindir %( if [ -d "/sbin" -a \! -h "/sbin" ]; then echo "/sbin"; else echo %{_sbindir}; fi )
%define dup_state_dir %{_localstatedir}/lib/rpm-state/kmod-dups
%define kver_state_dir %{dup_state_dir}/kver
%define kver_state_file %{kver_state_dir}/%{kmod_kernel_version}.%(arch)
%define dup_module_list %{dup_state_dir}/rpm-kmod-%{kmod_name}-modules

Name:		kmod-redhat-bnxt_en
Version:	%{kmod_driver_version}
Release:	%{kmod_rpm_release}%{?dist}
%if "%{kmod_driver_epoch}" != ""
Epoch:		%{kmod_driver_epoch}
%endif
Summary:	bnxt_en kernel module for Driver Update Program
Group:		System/Kernel
License:	GPLv2
URL:		https://www.kernel.org/
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:	%kernel_devel_pkg = %kmod_kernel_version
%if "%{kmod_dist_build_deps}" != ""
BuildRequires:	%{kmod_dist_build_deps}
%endif
ExclusiveArch:	x86_64
%global kernel_source() /usr/src/kernels/%{kmod_kernel_version}.$(arch)

%global _use_internal_dependency_generator 0
%if "%{?kmod_kernel_version_min}" != ""
Provides:	%kernel_modules_pkg >= %{kmod_kernel_version_min}.%{_target_cpu}
%else
Provides:	%kernel_modules_pkg = %{kmod_kernel_version_dep}.%{_target_cpu}
%endif
Provides:	kmod-%{kmod_name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires(post):	%{sbindir}/weak-modules
Requires(postun):	%{sbindir}/weak-modules
Requires:	kernel >= 4.18.0-147.el8

Requires:	kernel < 4.18.0-148.el8
%if 0
Requires: firmware(%{kmod_name}) = ENTER_FIRMWARE_VERSION
%endif
%if "%{kmod_build_dependencies}" != ""
BuildRequires:  %{kmod_build_dependencies}
%endif
%if "%{kmod_dependencies}" != ""
Requires:       %{kmod_dependencies}
%endif
# if there are multiple kmods for the same driver from different vendors,
# they should conflict with each other.
Conflicts:	kmod-%{kmod_name}

%description
bnxt_en kernel module for Driver Update Program

%if 0

%package -n kmod-redhat-bnxt_en-firmware
Version:	ENTER_FIRMWARE_VERSION
Summary:	bnxt_en firmware for Driver Update Program
Provides:	firmware(%{kmod_name}) = ENTER_FIRMWARE_VERSION
%if "%{kmod_kernel_version_min}" != ""
Provides:	%kernel_modules_pkg >= %{kmod_kernel_version_min}.%{_target_cpu}
%else
Provides:	%kernel_modules_pkg = %{kmod_kernel_version_dep}.%{_target_cpu}
%endif
%description -n  kmod-redhat-bnxt_en-firmware
bnxt_en firmware for Driver Update Program


%files -n kmod-redhat-bnxt_en-firmware
%defattr(644,root,root,755)
%{FIRMWARE_FILES}

%endif

# Development package
%if 0%{kmod_devel_package}
%package -n kmod-redhat-bnxt_en-devel
Version:	%{kmod_driver_version}
Requires:	kernel >= 4.18.0-147.el8

Requires:	kernel < 4.18.0-148.el8
Summary:	bnxt_en development files for Driver Update Program

%description -n  kmod-redhat-bnxt_en-devel
bnxt_en development files for Driver Update Program


%files -n kmod-redhat-bnxt_en-devel
%defattr(644,root,root,755)
/usr/share/kmod-%{kmod_vendor}-%{kmod_name}/Module.symvers
%endif

%post
modules=( $(find /lib/modules/%{kmod_kernel_version}.%(arch)/%{kmod_install_path} | grep '\.ko$') )
printf '%s\n' "${modules[@]}" | %{sbindir}/weak-modules --add-modules --no-initramfs

mkdir -p "%{kver_state_dir}"
touch "%{kver_state_file}"

exit 0

%posttrans
# We have to re-implement part of weak-modules here because it doesn't allow
# calling initramfs regeneration separately
if [ -f "%{kver_state_file}" ]; then
	kver_base="%{kmod_kernel_version_dep}"
	kvers=$(ls -d "/lib/modules/${kver_base%%.*}"*)

	for k_dir in $kvers; do
		k="${k_dir#/lib/modules/}"

		tmp_initramfs="/boot/initramfs-$k.tmp"
		dst_initramfs="/boot/initramfs-$k.img"

		# The same check as in weak-modules: we assume that the kernel present
		# if the symvers file exists.
		if [ -e "/boot/symvers-$k.gz" ]; then
			/usr/bin/dracut -f "$tmp_initramfs" "$k" || exit 1
			cmp -s "$tmp_initramfs" "$dst_initramfs"
			if [ "$?" = 1 ]; then
				mv "$tmp_initramfs" "$dst_initramfs"
			else
				rm -f "$tmp_initramfs"
			fi
		fi
	done

	rm -f "%{kver_state_file}"
	rmdir "%{kver_state_dir}" 2> /dev/null
fi

rmdir "%{dup_state_dir}" 2> /dev/null

exit 0

%preun
if rpm -q --filetriggers kmod 2> /dev/null| grep -q "Trigger for weak-modules call on kmod removal"; then
	mkdir -p "%{kver_state_dir}"
	touch "%{kver_state_file}"
fi

mkdir -p "%{dup_state_dir}"
rpm -ql kmod-redhat-bnxt_en-%{kmod_driver_version}-%{kmod_rpm_release}%{?dist}.$(arch) | \
	grep '\.ko$' > "%{dup_module_list}"

%postun
if rpm -q --filetriggers kmod 2> /dev/null| grep -q "Trigger for weak-modules call on kmod removal"; then
	initramfs_opt="--no-initramfs"
else
	initramfs_opt=""
fi

modules=( $(cat "%{dup_module_list}") )
rm -f "%{dup_module_list}"
printf '%s\n' "${modules[@]}" | %{sbindir}/weak-modules --remove-modules $initramfs_opt

rmdir "%{dup_state_dir}" 2> /dev/null

exit 0

%files
%defattr(644,root,root,755)
/lib/modules/%{kmod_kernel_version}.%(arch)
/etc/depmod.d/%{kmod_name}.conf
/usr/share/doc/kmod-%{kmod_name}/greylist.txt

%prep
%setup -n %{kmod_name}-%{kmod_vendor}-%{kmod_driver_version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1
%patch81 -p1
%patch82 -p1
%patch83 -p1
%patch84 -p1
%patch85 -p1
%patch86 -p1
%patch87 -p1
%patch88 -p1
%patch89 -p1
%patch90 -p1
%patch91 -p1
%patch92 -p1
set -- *
mkdir source
mv "$@" source/
mkdir obj

%build
rm -rf obj
cp -r source obj

PWD_PATH="$PWD"
%if "%{workaround_no_pwd_rel_path}" != "1"
PWD_PATH=$(realpath --relative-to="%{kernel_source}" . 2>/dev/null || echo "$PWD")
%endif
%{make_build} -C %{kernel_source} V=1 M="$PWD_PATH/obj/%{kmod_kbuild_dir}" \
	NOSTDINC_FLAGS="-I$PWD_PATH/obj/include -I$PWD_PATH/obj/include/uapi" \
	EXTRA_CFLAGS="%{nil}" \
	%{nil}
# mark modules executable so that strip-to-file can strip them
find obj/%{kmod_kbuild_dir} -name "*.ko" -type f -exec chmod u+x '{}' +

whitelist="/lib/modules/kabi-current/kabi_whitelist_%{_target_cpu}"
for modules in $( find obj/%{kmod_kbuild_dir} -name "*.ko" -type f -printf "%{findpat}\n" | sed 's|\.ko$||' | sort -u ) ; do
	# update depmod.conf
	module_weak_path=$(echo "$modules" | sed 's/[\/]*[^\/]*$//')
	if [ -z "$module_weak_path" ]; then
		module_weak_path=%{name}
	else
		module_weak_path=%{name}/$module_weak_path
	fi
	echo "override $(echo $modules | sed 's/.*\///')" \
	     "$(echo "%{kmod_kernel_version_dep}" |
	        sed 's/\.[^\.]*$//;
		     s/\([.+?^$\/\\|()\[]\|\]\)/\\\0/g').*" \
		     "weak-updates/$module_weak_path" >> source/depmod.conf

	# update greylist
	nm -u obj/%{kmod_kbuild_dir}/$modules.ko | sed 's/.*U //' |  sed 's/^\.//' | sort -u | while read -r symbol; do
		grep -q "^\s*$symbol\$" $whitelist || echo "$symbol" >> source/greylist
	done
done
sort -u source/greylist | uniq > source/greylist.txt

%install
export INSTALL_MOD_PATH=$RPM_BUILD_ROOT
export INSTALL_MOD_DIR=%{kmod_install_path}
PWD_PATH="$PWD"
%if "%{workaround_no_pwd_rel_path}" != "1"
PWD_PATH=$(realpath --relative-to="%{kernel_source}" . 2>/dev/null || echo "$PWD")
%endif
make -C %{kernel_source} modules_install \
	M=$PWD_PATH/obj/%{kmod_kbuild_dir}
# Cleanup unnecessary kernel-generated module dependency files.
find $INSTALL_MOD_PATH/lib/modules -iname 'modules.*' -exec rm {} \;

install -m 644 -D source/depmod.conf $RPM_BUILD_ROOT/etc/depmod.d/%{kmod_name}.conf
install -m 644 -D source/greylist.txt $RPM_BUILD_ROOT/usr/share/doc/kmod-%{kmod_name}/greylist.txt
%if 0
%{FIRMWARE_FILES_INSTALL}
%endif
%if 0%{kmod_devel_package}
install -m 644 -D $PWD/obj/%{kmod_kbuild_dir}/Module.symvers $RPM_BUILD_ROOT/usr/share/kmod-%{kmod_vendor}-%{kmod_name}/Module.symvers
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Feb 19 2020 Eugene Syromiatnikov <esyr@redhat.com> 1.10.0_dup8.1-2
- Bump release.

* Tue Feb 18 2020 Eugene Syromiatnikov <esyr@redhat.com> 1.10.0_dup8.1-1
- 9158390ccae759c2c0221de6e0c9541375a480f6
- bnxt_en kernel module for Driver Update Program
- Resolves: #bz1802054
