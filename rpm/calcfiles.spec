Name:           calcfiles
Version:        1.0
Release:        1%{?dist}
Summary:        A simple script to calculate files in a directory
Requires:       unzip

License:        MIT
URL:            https://github.com/pavelmagadan/system_programming
Source0:        https://github.com/pavelmagadan/system_programming/archive/main.zip

BuildArch:      noarch

%description
calc_files.sh is a simple script that calculates the number of files in a directory.

%prep
unzip %SOURCE0
cd system_programming-main/

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 %{_builddir}/system_programming-main/calc_files.sh %{buildroot}/usr/bin/calc_files

%files
/usr/bin/calc_files

%changelog
* Sun Jan 14 2024 Petrenko Pavel <pavel.petrenko.magadan@gmail.com> - 1.0-1
- Initial build
