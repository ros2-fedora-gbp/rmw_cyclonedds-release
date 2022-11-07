%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/humble/.*$
%global __requires_exclude_from ^/opt/ros/humble/.*$

Name:           ros-humble-rmw-cyclonedds-cpp
Version:        1.3.4
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS rmw_cyclonedds_cpp package

License:        Apache License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-humble-cyclonedds
Requires:       ros-humble-iceoryx-binding-c
Requires:       ros-humble-rcpputils
Requires:       ros-humble-rcutils
Requires:       ros-humble-rmw
Requires:       ros-humble-rmw-dds-common
Requires:       ros-humble-rosidl-runtime-c
Requires:       ros-humble-rosidl-typesupport-introspection-c
Requires:       ros-humble-rosidl-typesupport-introspection-cpp
Requires:       ros-humble-tracetools
Requires:       ros-humble-ros-workspace
BuildRequires:  ros-humble-ament-cmake-ros
BuildRequires:  ros-humble-cyclonedds
BuildRequires:  ros-humble-iceoryx-binding-c
BuildRequires:  ros-humble-rcpputils
BuildRequires:  ros-humble-rcutils
BuildRequires:  ros-humble-rmw
BuildRequires:  ros-humble-rmw-dds-common
BuildRequires:  ros-humble-rosidl-runtime-c
BuildRequires:  ros-humble-rosidl-typesupport-introspection-c
BuildRequires:  ros-humble-rosidl-typesupport-introspection-cpp
BuildRequires:  ros-humble-tracetools
BuildRequires:  ros-humble-ros-workspace
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
Provides:       ros-humble-rmw-implementation-packages(member)

%if 0%{?with_tests}
BuildRequires:  ros-humble-ament-lint-auto
BuildRequires:  ros-humble-ament-lint-common
%endif

%if 0%{?with_weak_deps}
Supplements:    ros-humble-rmw-implementation-packages(all)
%endif

%description
Implement the ROS middleware interface using Eclipse CycloneDDS in C++.

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/humble" \
    -DAMENT_PREFIX_PATH="/opt/ros/humble" \
    -DCMAKE_PREFIX_PATH="/opt/ros/humble" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/humble/setup.sh" ]; then . "/opt/ros/humble/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/humble

%changelog
* Mon Nov 07 2022 Erik Boasson <erik.boasson@adlinktech.com> - 1.3.4-1
- Autogenerated by Bloom

* Tue Apr 19 2022 Erik Boasson <erik.boasson@adlinktech.com> - 1.3.3-2
- Autogenerated by Bloom

* Wed Apr 06 2022 Erik Boasson <erik.boasson@adlinktech.com> - 1.3.3-1
- Autogenerated by Bloom

* Tue Apr 05 2022 Erik Boasson <erik.boasson@adlinktech.com> - 1.3.2-1
- Autogenerated by Bloom

* Thu Mar 31 2022 Erik Boasson <erik.boasson@adlinktech.com> - 1.3.1-1
- Autogenerated by Bloom

* Fri Mar 25 2022 Erik Boasson <erik.boasson@adlinktech.com> - 1.3.0-1
- Autogenerated by Bloom

* Tue Mar 01 2022 Erik Boasson <erik.boasson@adlinktech.com> - 1.2.0-1
- Autogenerated by Bloom

* Tue Feb 08 2022 Erik Boasson <erik.boasson@adlinktech.com> - 1.1.2-2
- Autogenerated by Bloom

