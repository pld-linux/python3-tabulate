#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module		tabulate
Summary:	Pretty-print tabular data
Summary(pl.UTF-8):	Ładne wypisywanie danych tabelarycznych
Name:		python3-%{module}
Version:	0.10.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/tabulate/
Source0:	https://files.pythonhosted.org/packages/source/t/tabulate/%{module}-%{version}.tar.gz
# Source0-md5:	6ac315ec07ad9ead2452dff4806b7400
URL:		https://github.com/astanin/python-tabulate
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.10
BuildRequires:	python3-setuptools >= 1:77.0.3
BuildRequires:	python3-setuptools_scm >= 3.4.3
%if %{with tests}
BuildRequires:	python3-pytest
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.045
Requires:	python3-modules >= 1:3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pretty-print tabular data in Python.

The main use cases of the library are:
- printing small tables without hassle: just one function call,
  formatting is guided by the data itself
- authoring tabular data for lightweight plain-text markup: multiple
  output formats suitable for further editing or transformation
- readable presentation of mixed textual and numeric data: smart
  column alignment, configurable number formatting, alignment by a
  decimal point

%description -l pl.UTF-8
Ładne wypisywanie danych tabelarycznych w Pythonie.

Główne przypadki użycia tej biblioteki to:
- proste wypisywanie małych tabelek - tylko jedno wywołanie funkcji,
  formatowanie sugerowane przez same dane
- tworzenie danych tabelarycznych do lekkich znaczników tekstowych -
  wiele formatów wyjściowych, odpowiednich do dalszej edycji lub
  przekształceń
- czytelna prezentacja mieszanych danych tekstowych i liczbowych -
  inteligentne wyrównywanie kolumn, konfigurowalne formatowanie liczb,
  wyrównywanie do kropki/przecinka dziesiętnego

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest -v --doctest-modules test tabulate
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README.md
%attr(755,root,root) %{_bindir}/tabulate
%{py3_sitescriptdir}/tabulate
%{py3_sitescriptdir}/tabulate-%{version}.dist-info
