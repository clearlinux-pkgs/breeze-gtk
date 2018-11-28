#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xEC94D18F7F05997E (jr@jriddell.org)
#
Name     : breeze-gtk
Version  : 5.14.4
Release  : 7
URL      : https://download.kde.org/stable/plasma/5.14.4/breeze-gtk-5.14.4.tar.xz
Source0  : https://download.kde.org/stable/plasma/5.14.4/breeze-gtk-5.14.4.tar.xz
Source99 : https://download.kde.org/stable/plasma/5.14.4/breeze-gtk-5.14.4.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: breeze-gtk-data = %{version}-%{release}
Requires: breeze-gtk-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

%description
# Gnome-breeze
A GTK Theme Built to Match KDE's Breeze. GTK2 theme made by [scionicspectre](https://github.com/scionicspectre/BreezyGTK)

%package data
Summary: data components for the breeze-gtk package.
Group: Data

%description data
data components for the breeze-gtk package.


%package license
Summary: license components for the breeze-gtk package.
Group: Default

%description license
license components for the breeze-gtk package.


%prep
%setup -q -n breeze-gtk-5.14.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1543391099
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1543391099
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/breeze-gtk
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/breeze-gtk/COPYING.LIB
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/kconf_update_bin/gtkbreeze5.5

%files data
%defattr(-,root,root,-)
/usr/share/kconf_update/gtkbreeze5.5.upd
/usr/share/themes/Breeze-Dark/assets/arrow-down-active.png
/usr/share/themes/Breeze-Dark/assets/arrow-down-hover.png
/usr/share/themes/Breeze-Dark/assets/arrow-down-insensitive.png
/usr/share/themes/Breeze-Dark/assets/arrow-down.png
/usr/share/themes/Breeze-Dark/assets/arrow-left-active.png
/usr/share/themes/Breeze-Dark/assets/arrow-left-hover.png
/usr/share/themes/Breeze-Dark/assets/arrow-left-insensitive.png
/usr/share/themes/Breeze-Dark/assets/arrow-left.png
/usr/share/themes/Breeze-Dark/assets/arrow-right-active.png
/usr/share/themes/Breeze-Dark/assets/arrow-right-hover.png
/usr/share/themes/Breeze-Dark/assets/arrow-right-insensitive.png
/usr/share/themes/Breeze-Dark/assets/arrow-right.png
/usr/share/themes/Breeze-Dark/assets/arrow-small-down-active.png
/usr/share/themes/Breeze-Dark/assets/arrow-small-down-hover.png
/usr/share/themes/Breeze-Dark/assets/arrow-small-down-insensitive.png
/usr/share/themes/Breeze-Dark/assets/arrow-small-down.png
/usr/share/themes/Breeze-Dark/assets/arrow-small-left-active.png
/usr/share/themes/Breeze-Dark/assets/arrow-small-left-hover.png
/usr/share/themes/Breeze-Dark/assets/arrow-small-left-insensitive.png
/usr/share/themes/Breeze-Dark/assets/arrow-small-left.png
/usr/share/themes/Breeze-Dark/assets/arrow-small-right-active.png
/usr/share/themes/Breeze-Dark/assets/arrow-small-right-hover.png
/usr/share/themes/Breeze-Dark/assets/arrow-small-right-insensitive.png
/usr/share/themes/Breeze-Dark/assets/arrow-small-right.png
/usr/share/themes/Breeze-Dark/assets/arrow-small-up-active.png
/usr/share/themes/Breeze-Dark/assets/arrow-small-up-hover.png
/usr/share/themes/Breeze-Dark/assets/arrow-small-up-insensitive.png
/usr/share/themes/Breeze-Dark/assets/arrow-small-up.png
/usr/share/themes/Breeze-Dark/assets/arrow-up-active.png
/usr/share/themes/Breeze-Dark/assets/arrow-up-hover.png
/usr/share/themes/Breeze-Dark/assets/arrow-up-insensitive.png
/usr/share/themes/Breeze-Dark/assets/arrow-up.png
/usr/share/themes/Breeze-Dark/assets/button-active.png
/usr/share/themes/Breeze-Dark/assets/button-hover.png
/usr/share/themes/Breeze-Dark/assets/button-insensitive.png
/usr/share/themes/Breeze-Dark/assets/button.png
/usr/share/themes/Breeze-Dark/assets/check-checked-active.png
/usr/share/themes/Breeze-Dark/assets/check-checked-active@2.png
/usr/share/themes/Breeze-Dark/assets/check-checked-backdrop-insensitive.png
/usr/share/themes/Breeze-Dark/assets/check-checked-backdrop-insensitive@2.png
/usr/share/themes/Breeze-Dark/assets/check-checked-backdrop.png
/usr/share/themes/Breeze-Dark/assets/check-checked-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/check-checked-hover.png
/usr/share/themes/Breeze-Dark/assets/check-checked-hover@2.png
/usr/share/themes/Breeze-Dark/assets/check-checked-insensitive.png
/usr/share/themes/Breeze-Dark/assets/check-checked-insensitive@2.png
/usr/share/themes/Breeze-Dark/assets/check-mixed-active.png
/usr/share/themes/Breeze-Dark/assets/check-mixed-active@2.png
/usr/share/themes/Breeze-Dark/assets/check-mixed-backdrop-insensitive.png
/usr/share/themes/Breeze-Dark/assets/check-mixed-backdrop-insensitive@2.png
/usr/share/themes/Breeze-Dark/assets/check-mixed-backdrop.png
/usr/share/themes/Breeze-Dark/assets/check-mixed-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/check-mixed-hover.png
/usr/share/themes/Breeze-Dark/assets/check-mixed-hover@2.png
/usr/share/themes/Breeze-Dark/assets/check-mixed-insensitive.png
/usr/share/themes/Breeze-Dark/assets/check-mixed-insensitive@2.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-checked-active.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-checked-active@2.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-checked-backdrop-insensitive.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-checked-backdrop-insensitive@2.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-checked-backdrop.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-checked-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-checked-hover.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-checked-hover@2.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-checked-insensitive.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-checked-insensitive@2.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-unchecked-active.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-unchecked-active@2.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-unchecked-backdrop-insensitive.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-unchecked-backdrop-insensitive@2.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-unchecked-backdrop.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-unchecked-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-unchecked-hover.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-unchecked-hover@2.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-unchecked-insensitive.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-unchecked-insensitive@2.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-unchecked.png
/usr/share/themes/Breeze-Dark/assets/check-selectionmode-unchecked@2.png
/usr/share/themes/Breeze-Dark/assets/check-unchecked-active.png
/usr/share/themes/Breeze-Dark/assets/check-unchecked-active@2.png
/usr/share/themes/Breeze-Dark/assets/check-unchecked-backdrop-insensitive.png
/usr/share/themes/Breeze-Dark/assets/check-unchecked-backdrop-insensitive@2.png
/usr/share/themes/Breeze-Dark/assets/check-unchecked-backdrop.png
/usr/share/themes/Breeze-Dark/assets/check-unchecked-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/check-unchecked-hover.png
/usr/share/themes/Breeze-Dark/assets/check-unchecked-hover@2.png
/usr/share/themes/Breeze-Dark/assets/check-unchecked-insensitive.png
/usr/share/themes/Breeze-Dark/assets/check-unchecked-insensitive@2.png
/usr/share/themes/Breeze-Dark/assets/check-unchecked.png
/usr/share/themes/Breeze-Dark/assets/check-unchecked@2.png
/usr/share/themes/Breeze-Dark/assets/combo-entry-active.png
/usr/share/themes/Breeze-Dark/assets/combo-entry-button-active.png
/usr/share/themes/Breeze-Dark/assets/combo-entry-button-insensitive.png
/usr/share/themes/Breeze-Dark/assets/combo-entry-button.png
/usr/share/themes/Breeze-Dark/assets/combo-entry-insensitive.png
/usr/share/themes/Breeze-Dark/assets/combo-entry.png
/usr/share/themes/Breeze-Dark/assets/entry-active.png
/usr/share/themes/Breeze-Dark/assets/entry-insensitive.png
/usr/share/themes/Breeze-Dark/assets/entry.png
/usr/share/themes/Breeze-Dark/assets/frame-gap-end.png
/usr/share/themes/Breeze-Dark/assets/frame-gap-start.png
/usr/share/themes/Breeze-Dark/assets/frame.png
/usr/share/themes/Breeze-Dark/assets/handle-h.png
/usr/share/themes/Breeze-Dark/assets/handle-v.png
/usr/share/themes/Breeze-Dark/assets/line-h.png
/usr/share/themes/Breeze-Dark/assets/line-v.png
/usr/share/themes/Breeze-Dark/assets/menu-arrow-insensitive.png
/usr/share/themes/Breeze-Dark/assets/menu-arrow-selected.png
/usr/share/themes/Breeze-Dark/assets/menu-arrow.png
/usr/share/themes/Breeze-Dark/assets/menubar-button.png
/usr/share/themes/Breeze-Dark/assets/notebook-frame-bottom.png
/usr/share/themes/Breeze-Dark/assets/notebook-frame-right.png
/usr/share/themes/Breeze-Dark/assets/notebook-frame-top.png
/usr/share/themes/Breeze-Dark/assets/notebook-gap-horizontal.png
/usr/share/themes/Breeze-Dark/assets/notebook-gap-vertical.png
/usr/share/themes/Breeze-Dark/assets/null.png
/usr/share/themes/Breeze-Dark/assets/progressbar-bar.png
/usr/share/themes/Breeze-Dark/assets/progressbar-trough.png
/usr/share/themes/Breeze-Dark/assets/radio-checked-active.png
/usr/share/themes/Breeze-Dark/assets/radio-checked-active@2.png
/usr/share/themes/Breeze-Dark/assets/radio-checked-backdrop-insensitive.png
/usr/share/themes/Breeze-Dark/assets/radio-checked-backdrop-insensitive@2.png
/usr/share/themes/Breeze-Dark/assets/radio-checked-backdrop.png
/usr/share/themes/Breeze-Dark/assets/radio-checked-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/radio-checked-hover.png
/usr/share/themes/Breeze-Dark/assets/radio-checked-hover@2.png
/usr/share/themes/Breeze-Dark/assets/radio-checked-insensitive.png
/usr/share/themes/Breeze-Dark/assets/radio-checked-insensitive@2.png
/usr/share/themes/Breeze-Dark/assets/radio-mixed-active.png
/usr/share/themes/Breeze-Dark/assets/radio-mixed-active@2.png
/usr/share/themes/Breeze-Dark/assets/radio-mixed-backdrop-insensitive.png
/usr/share/themes/Breeze-Dark/assets/radio-mixed-backdrop-insensitive@2.png
/usr/share/themes/Breeze-Dark/assets/radio-mixed-backdrop.png
/usr/share/themes/Breeze-Dark/assets/radio-mixed-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/radio-mixed-hover.png
/usr/share/themes/Breeze-Dark/assets/radio-mixed-hover@2.png
/usr/share/themes/Breeze-Dark/assets/radio-mixed-insensitive.png
/usr/share/themes/Breeze-Dark/assets/radio-mixed-insensitive@2.png
/usr/share/themes/Breeze-Dark/assets/radio-unchecked-active.png
/usr/share/themes/Breeze-Dark/assets/radio-unchecked-active@2.png
/usr/share/themes/Breeze-Dark/assets/radio-unchecked-backdrop-insensitive.png
/usr/share/themes/Breeze-Dark/assets/radio-unchecked-backdrop-insensitive@2.png
/usr/share/themes/Breeze-Dark/assets/radio-unchecked-backdrop.png
/usr/share/themes/Breeze-Dark/assets/radio-unchecked-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/radio-unchecked-hover.png
/usr/share/themes/Breeze-Dark/assets/radio-unchecked-hover@2.png
/usr/share/themes/Breeze-Dark/assets/radio-unchecked-insensitive.png
/usr/share/themes/Breeze-Dark/assets/radio-unchecked-insensitive@2.png
/usr/share/themes/Breeze-Dark/assets/radio-unchecked.png
/usr/share/themes/Breeze-Dark/assets/radio-unchecked@2.png
/usr/share/themes/Breeze-Dark/assets/scale-slider-active.png
/usr/share/themes/Breeze-Dark/assets/scale-slider-hover.png
/usr/share/themes/Breeze-Dark/assets/scale-slider-insensitive.png
/usr/share/themes/Breeze-Dark/assets/scale-slider.png
/usr/share/themes/Breeze-Dark/assets/scale-trough-horizontal.png
/usr/share/themes/Breeze-Dark/assets/scale-trough-vertical.png
/usr/share/themes/Breeze-Dark/assets/scrollbar-slider-horizontal-active.png
/usr/share/themes/Breeze-Dark/assets/scrollbar-slider-horizontal-active@2.png
/usr/share/themes/Breeze-Dark/assets/scrollbar-slider-horizontal-hover.png
/usr/share/themes/Breeze-Dark/assets/scrollbar-slider-horizontal-hover@2.png
/usr/share/themes/Breeze-Dark/assets/scrollbar-slider-horizontal.png
/usr/share/themes/Breeze-Dark/assets/scrollbar-slider-horizontal@2.png
/usr/share/themes/Breeze-Dark/assets/scrollbar-slider-vertical-active.png
/usr/share/themes/Breeze-Dark/assets/scrollbar-slider-vertical-active@2.png
/usr/share/themes/Breeze-Dark/assets/scrollbar-slider-vertical-hover.png
/usr/share/themes/Breeze-Dark/assets/scrollbar-slider-vertical-hover@2.png
/usr/share/themes/Breeze-Dark/assets/scrollbar-slider-vertical.png
/usr/share/themes/Breeze-Dark/assets/scrollbar-slider-vertical@2.png
/usr/share/themes/Breeze-Dark/assets/scrollbar-trough-horizontal.png
/usr/share/themes/Breeze-Dark/assets/scrollbar-trough-horizontal@2.png
/usr/share/themes/Breeze-Dark/assets/scrollbar-trough-vertical.png
/usr/share/themes/Breeze-Dark/assets/scrollbar-trough-vertical@2.png
/usr/share/themes/Breeze-Dark/assets/spinbutton-down-insensitive.png
/usr/share/themes/Breeze-Dark/assets/spinbutton-down-rtl-insensitive.png
/usr/share/themes/Breeze-Dark/assets/spinbutton-down-rtl.png
/usr/share/themes/Breeze-Dark/assets/spinbutton-down.png
/usr/share/themes/Breeze-Dark/assets/spinbutton-up-insensitive.png
/usr/share/themes/Breeze-Dark/assets/spinbutton-up-rtl-insensitive.png
/usr/share/themes/Breeze-Dark/assets/spinbutton-up-rtl.png
/usr/share/themes/Breeze-Dark/assets/spinbutton-up.png
/usr/share/themes/Breeze-Dark/assets/tab-bottom-active.png
/usr/share/themes/Breeze-Dark/assets/tab-bottom-inactive.png
/usr/share/themes/Breeze-Dark/assets/tab-left-active.png
/usr/share/themes/Breeze-Dark/assets/tab-left-inactive.png
/usr/share/themes/Breeze-Dark/assets/tab-right-active.png
/usr/share/themes/Breeze-Dark/assets/tab-right-inactive.png
/usr/share/themes/Breeze-Dark/assets/tab-top-active.png
/usr/share/themes/Breeze-Dark/assets/tab-top-inactive.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-close-active-backdrop.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-close-active-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-close-active.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-close-active@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-close-backdrop.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-close-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-close-hover-backdrop.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-close-hover-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-close-hover.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-close-hover@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-close.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-close@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-active-backdrop.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-active-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-active.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-active@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-backdrop.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-hover-backdrop.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-hover-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-hover.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-hover@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-active-backdrop.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-active-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-active.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-active@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-backdrop.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-hover-backdrop.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-hover-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-hover.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-hover@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-maximized.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize-maximized@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-maximize@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-minimize-active-backdrop.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-minimize-active-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-minimize-active.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-minimize-active@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-minimize-backdrop.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-minimize-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-minimize-hover-backdrop.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-minimize-hover-backdrop@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-minimize-hover.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-minimize-hover@2.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-minimize.png
/usr/share/themes/Breeze-Dark/assets/titlebutton-minimize@2.png
/usr/share/themes/Breeze-Dark/assets/togglebutton-active.png
/usr/share/themes/Breeze-Dark/assets/togglebutton-hover.png
/usr/share/themes/Breeze-Dark/assets/togglebutton-insensitive.png
/usr/share/themes/Breeze-Dark/assets/togglebutton.png
/usr/share/themes/Breeze-Dark/assets/toolbar-background.png
/usr/share/themes/Breeze-Dark/assets/toolbutton-active.png
/usr/share/themes/Breeze-Dark/assets/toolbutton-hover.png
/usr/share/themes/Breeze-Dark/assets/toolbutton-toggled.png
/usr/share/themes/Breeze-Dark/assets/tree-header.png
/usr/share/themes/Breeze-Dark/gtk-2.0/gtkrc
/usr/share/themes/Breeze-Dark/gtk-2.0/widgets/buttons
/usr/share/themes/Breeze-Dark/gtk-2.0/widgets/default
/usr/share/themes/Breeze-Dark/gtk-2.0/widgets/entry
/usr/share/themes/Breeze-Dark/gtk-2.0/widgets/menu
/usr/share/themes/Breeze-Dark/gtk-2.0/widgets/misc
/usr/share/themes/Breeze-Dark/gtk-2.0/widgets/notebook
/usr/share/themes/Breeze-Dark/gtk-2.0/widgets/progressbar
/usr/share/themes/Breeze-Dark/gtk-2.0/widgets/range
/usr/share/themes/Breeze-Dark/gtk-2.0/widgets/scrollbar
/usr/share/themes/Breeze-Dark/gtk-2.0/widgets/styles
/usr/share/themes/Breeze-Dark/gtk-2.0/widgets/toolbar
/usr/share/themes/Breeze-Dark/gtk-3.18/gtk.css
/usr/share/themes/Breeze-Dark/gtk-3.20/gtk.css
/usr/share/themes/Breeze/assets/arrow-down-active.png
/usr/share/themes/Breeze/assets/arrow-down-hover.png
/usr/share/themes/Breeze/assets/arrow-down-insensitive.png
/usr/share/themes/Breeze/assets/arrow-down.png
/usr/share/themes/Breeze/assets/arrow-left-active.png
/usr/share/themes/Breeze/assets/arrow-left-hover.png
/usr/share/themes/Breeze/assets/arrow-left-insensitive.png
/usr/share/themes/Breeze/assets/arrow-left.png
/usr/share/themes/Breeze/assets/arrow-right-active.png
/usr/share/themes/Breeze/assets/arrow-right-hover.png
/usr/share/themes/Breeze/assets/arrow-right-insensitive.png
/usr/share/themes/Breeze/assets/arrow-right.png
/usr/share/themes/Breeze/assets/arrow-small-down-active.png
/usr/share/themes/Breeze/assets/arrow-small-down-hover.png
/usr/share/themes/Breeze/assets/arrow-small-down-insensitive.png
/usr/share/themes/Breeze/assets/arrow-small-down.png
/usr/share/themes/Breeze/assets/arrow-small-left-active.png
/usr/share/themes/Breeze/assets/arrow-small-left-hover.png
/usr/share/themes/Breeze/assets/arrow-small-left-insensitive.png
/usr/share/themes/Breeze/assets/arrow-small-left.png
/usr/share/themes/Breeze/assets/arrow-small-right-active.png
/usr/share/themes/Breeze/assets/arrow-small-right-hover.png
/usr/share/themes/Breeze/assets/arrow-small-right-insensitive.png
/usr/share/themes/Breeze/assets/arrow-small-right.png
/usr/share/themes/Breeze/assets/arrow-small-up-active.png
/usr/share/themes/Breeze/assets/arrow-small-up-hover.png
/usr/share/themes/Breeze/assets/arrow-small-up-insensitive.png
/usr/share/themes/Breeze/assets/arrow-small-up.png
/usr/share/themes/Breeze/assets/arrow-up-active.png
/usr/share/themes/Breeze/assets/arrow-up-hover.png
/usr/share/themes/Breeze/assets/arrow-up-insensitive.png
/usr/share/themes/Breeze/assets/arrow-up.png
/usr/share/themes/Breeze/assets/button-active.png
/usr/share/themes/Breeze/assets/button-hover.png
/usr/share/themes/Breeze/assets/button-insensitive.png
/usr/share/themes/Breeze/assets/button.png
/usr/share/themes/Breeze/assets/check-checked-active.png
/usr/share/themes/Breeze/assets/check-checked-active@2.png
/usr/share/themes/Breeze/assets/check-checked-backdrop-insensitive.png
/usr/share/themes/Breeze/assets/check-checked-backdrop-insensitive@2.png
/usr/share/themes/Breeze/assets/check-checked-backdrop.png
/usr/share/themes/Breeze/assets/check-checked-backdrop@2.png
/usr/share/themes/Breeze/assets/check-checked-hover.png
/usr/share/themes/Breeze/assets/check-checked-hover@2.png
/usr/share/themes/Breeze/assets/check-checked-insensitive.png
/usr/share/themes/Breeze/assets/check-checked-insensitive@2.png
/usr/share/themes/Breeze/assets/check-mixed-active.png
/usr/share/themes/Breeze/assets/check-mixed-active@2.png
/usr/share/themes/Breeze/assets/check-mixed-backdrop-insensitive.png
/usr/share/themes/Breeze/assets/check-mixed-backdrop-insensitive@2.png
/usr/share/themes/Breeze/assets/check-mixed-backdrop.png
/usr/share/themes/Breeze/assets/check-mixed-backdrop@2.png
/usr/share/themes/Breeze/assets/check-mixed-hover.png
/usr/share/themes/Breeze/assets/check-mixed-hover@2.png
/usr/share/themes/Breeze/assets/check-mixed-insensitive.png
/usr/share/themes/Breeze/assets/check-mixed-insensitive@2.png
/usr/share/themes/Breeze/assets/check-selectionmode-checked-active.png
/usr/share/themes/Breeze/assets/check-selectionmode-checked-active@2.png
/usr/share/themes/Breeze/assets/check-selectionmode-checked-backdrop-insensitive.png
/usr/share/themes/Breeze/assets/check-selectionmode-checked-backdrop-insensitive@2.png
/usr/share/themes/Breeze/assets/check-selectionmode-checked-backdrop.png
/usr/share/themes/Breeze/assets/check-selectionmode-checked-backdrop@2.png
/usr/share/themes/Breeze/assets/check-selectionmode-checked-hover.png
/usr/share/themes/Breeze/assets/check-selectionmode-checked-hover@2.png
/usr/share/themes/Breeze/assets/check-selectionmode-checked-insensitive.png
/usr/share/themes/Breeze/assets/check-selectionmode-checked-insensitive@2.png
/usr/share/themes/Breeze/assets/check-selectionmode-unchecked-active.png
/usr/share/themes/Breeze/assets/check-selectionmode-unchecked-active@2.png
/usr/share/themes/Breeze/assets/check-selectionmode-unchecked-backdrop-insensitive.png
/usr/share/themes/Breeze/assets/check-selectionmode-unchecked-backdrop-insensitive@2.png
/usr/share/themes/Breeze/assets/check-selectionmode-unchecked-backdrop.png
/usr/share/themes/Breeze/assets/check-selectionmode-unchecked-backdrop@2.png
/usr/share/themes/Breeze/assets/check-selectionmode-unchecked-hover.png
/usr/share/themes/Breeze/assets/check-selectionmode-unchecked-hover@2.png
/usr/share/themes/Breeze/assets/check-selectionmode-unchecked-insensitive.png
/usr/share/themes/Breeze/assets/check-selectionmode-unchecked-insensitive@2.png
/usr/share/themes/Breeze/assets/check-selectionmode-unchecked.png
/usr/share/themes/Breeze/assets/check-selectionmode-unchecked@2.png
/usr/share/themes/Breeze/assets/check-unchecked-active.png
/usr/share/themes/Breeze/assets/check-unchecked-active@2.png
/usr/share/themes/Breeze/assets/check-unchecked-backdrop-insensitive.png
/usr/share/themes/Breeze/assets/check-unchecked-backdrop-insensitive@2.png
/usr/share/themes/Breeze/assets/check-unchecked-backdrop.png
/usr/share/themes/Breeze/assets/check-unchecked-backdrop@2.png
/usr/share/themes/Breeze/assets/check-unchecked-hover.png
/usr/share/themes/Breeze/assets/check-unchecked-hover@2.png
/usr/share/themes/Breeze/assets/check-unchecked-insensitive.png
/usr/share/themes/Breeze/assets/check-unchecked-insensitive@2.png
/usr/share/themes/Breeze/assets/check-unchecked.png
/usr/share/themes/Breeze/assets/check-unchecked@2.png
/usr/share/themes/Breeze/assets/combo-entry-active.png
/usr/share/themes/Breeze/assets/combo-entry-button-active.png
/usr/share/themes/Breeze/assets/combo-entry-button-insensitive.png
/usr/share/themes/Breeze/assets/combo-entry-button.png
/usr/share/themes/Breeze/assets/combo-entry-insensitive.png
/usr/share/themes/Breeze/assets/combo-entry.png
/usr/share/themes/Breeze/assets/entry-active.png
/usr/share/themes/Breeze/assets/entry-insensitive.png
/usr/share/themes/Breeze/assets/entry.png
/usr/share/themes/Breeze/assets/frame-gap-end.png
/usr/share/themes/Breeze/assets/frame-gap-start.png
/usr/share/themes/Breeze/assets/frame.png
/usr/share/themes/Breeze/assets/handle-h.png
/usr/share/themes/Breeze/assets/handle-v.png
/usr/share/themes/Breeze/assets/line-h.png
/usr/share/themes/Breeze/assets/line-v.png
/usr/share/themes/Breeze/assets/menu-arrow-insensitive.png
/usr/share/themes/Breeze/assets/menu-arrow-selected.png
/usr/share/themes/Breeze/assets/menu-arrow.png
/usr/share/themes/Breeze/assets/menubar-button.png
/usr/share/themes/Breeze/assets/notebook-frame-bottom.png
/usr/share/themes/Breeze/assets/notebook-frame-right.png
/usr/share/themes/Breeze/assets/notebook-frame-top.png
/usr/share/themes/Breeze/assets/notebook-gap-horizontal.png
/usr/share/themes/Breeze/assets/notebook-gap-vertical.png
/usr/share/themes/Breeze/assets/null.png
/usr/share/themes/Breeze/assets/progressbar-bar.png
/usr/share/themes/Breeze/assets/progressbar-trough.png
/usr/share/themes/Breeze/assets/radio-checked-active.png
/usr/share/themes/Breeze/assets/radio-checked-active@2.png
/usr/share/themes/Breeze/assets/radio-checked-backdrop-insensitive.png
/usr/share/themes/Breeze/assets/radio-checked-backdrop-insensitive@2.png
/usr/share/themes/Breeze/assets/radio-checked-backdrop.png
/usr/share/themes/Breeze/assets/radio-checked-backdrop@2.png
/usr/share/themes/Breeze/assets/radio-checked-hover.png
/usr/share/themes/Breeze/assets/radio-checked-hover@2.png
/usr/share/themes/Breeze/assets/radio-checked-insensitive.png
/usr/share/themes/Breeze/assets/radio-checked-insensitive@2.png
/usr/share/themes/Breeze/assets/radio-mixed-active.png
/usr/share/themes/Breeze/assets/radio-mixed-active@2.png
/usr/share/themes/Breeze/assets/radio-mixed-backdrop-insensitive.png
/usr/share/themes/Breeze/assets/radio-mixed-backdrop-insensitive@2.png
/usr/share/themes/Breeze/assets/radio-mixed-backdrop.png
/usr/share/themes/Breeze/assets/radio-mixed-backdrop@2.png
/usr/share/themes/Breeze/assets/radio-mixed-hover.png
/usr/share/themes/Breeze/assets/radio-mixed-hover@2.png
/usr/share/themes/Breeze/assets/radio-mixed-insensitive.png
/usr/share/themes/Breeze/assets/radio-mixed-insensitive@2.png
/usr/share/themes/Breeze/assets/radio-unchecked-active.png
/usr/share/themes/Breeze/assets/radio-unchecked-active@2.png
/usr/share/themes/Breeze/assets/radio-unchecked-backdrop-insensitive.png
/usr/share/themes/Breeze/assets/radio-unchecked-backdrop-insensitive@2.png
/usr/share/themes/Breeze/assets/radio-unchecked-backdrop.png
/usr/share/themes/Breeze/assets/radio-unchecked-backdrop@2.png
/usr/share/themes/Breeze/assets/radio-unchecked-hover.png
/usr/share/themes/Breeze/assets/radio-unchecked-hover@2.png
/usr/share/themes/Breeze/assets/radio-unchecked-insensitive.png
/usr/share/themes/Breeze/assets/radio-unchecked-insensitive@2.png
/usr/share/themes/Breeze/assets/radio-unchecked.png
/usr/share/themes/Breeze/assets/radio-unchecked@2.png
/usr/share/themes/Breeze/assets/scale-slider-active.png
/usr/share/themes/Breeze/assets/scale-slider-hover.png
/usr/share/themes/Breeze/assets/scale-slider-insensitive.png
/usr/share/themes/Breeze/assets/scale-slider.png
/usr/share/themes/Breeze/assets/scale-trough-horizontal.png
/usr/share/themes/Breeze/assets/scale-trough-vertical.png
/usr/share/themes/Breeze/assets/scrollbar-slider-horizontal-active.png
/usr/share/themes/Breeze/assets/scrollbar-slider-horizontal-active@2.png
/usr/share/themes/Breeze/assets/scrollbar-slider-horizontal-hover.png
/usr/share/themes/Breeze/assets/scrollbar-slider-horizontal-hover@2.png
/usr/share/themes/Breeze/assets/scrollbar-slider-horizontal.png
/usr/share/themes/Breeze/assets/scrollbar-slider-horizontal@2.png
/usr/share/themes/Breeze/assets/scrollbar-slider-vertical-active.png
/usr/share/themes/Breeze/assets/scrollbar-slider-vertical-active@2.png
/usr/share/themes/Breeze/assets/scrollbar-slider-vertical-hover.png
/usr/share/themes/Breeze/assets/scrollbar-slider-vertical-hover@2.png
/usr/share/themes/Breeze/assets/scrollbar-slider-vertical.png
/usr/share/themes/Breeze/assets/scrollbar-slider-vertical@2.png
/usr/share/themes/Breeze/assets/scrollbar-trough-horizontal.png
/usr/share/themes/Breeze/assets/scrollbar-trough-horizontal@2.png
/usr/share/themes/Breeze/assets/scrollbar-trough-vertical.png
/usr/share/themes/Breeze/assets/scrollbar-trough-vertical@2.png
/usr/share/themes/Breeze/assets/spinbutton-down-insensitive.png
/usr/share/themes/Breeze/assets/spinbutton-down-rtl-insensitive.png
/usr/share/themes/Breeze/assets/spinbutton-down-rtl.png
/usr/share/themes/Breeze/assets/spinbutton-down.png
/usr/share/themes/Breeze/assets/spinbutton-up-insensitive.png
/usr/share/themes/Breeze/assets/spinbutton-up-rtl-insensitive.png
/usr/share/themes/Breeze/assets/spinbutton-up-rtl.png
/usr/share/themes/Breeze/assets/spinbutton-up.png
/usr/share/themes/Breeze/assets/tab-bottom-active.png
/usr/share/themes/Breeze/assets/tab-bottom-inactive.png
/usr/share/themes/Breeze/assets/tab-left-active.png
/usr/share/themes/Breeze/assets/tab-left-inactive.png
/usr/share/themes/Breeze/assets/tab-right-active.png
/usr/share/themes/Breeze/assets/tab-right-inactive.png
/usr/share/themes/Breeze/assets/tab-top-active.png
/usr/share/themes/Breeze/assets/tab-top-inactive.png
/usr/share/themes/Breeze/assets/titlebutton-close-active-backdrop.png
/usr/share/themes/Breeze/assets/titlebutton-close-active-backdrop@2.png
/usr/share/themes/Breeze/assets/titlebutton-close-active.png
/usr/share/themes/Breeze/assets/titlebutton-close-active@2.png
/usr/share/themes/Breeze/assets/titlebutton-close-backdrop.png
/usr/share/themes/Breeze/assets/titlebutton-close-backdrop@2.png
/usr/share/themes/Breeze/assets/titlebutton-close-hover-backdrop.png
/usr/share/themes/Breeze/assets/titlebutton-close-hover-backdrop@2.png
/usr/share/themes/Breeze/assets/titlebutton-close-hover.png
/usr/share/themes/Breeze/assets/titlebutton-close-hover@2.png
/usr/share/themes/Breeze/assets/titlebutton-close.png
/usr/share/themes/Breeze/assets/titlebutton-close@2.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-active-backdrop.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-active-backdrop@2.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-active.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-active@2.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-backdrop.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-backdrop@2.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-hover-backdrop.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-hover-backdrop@2.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-hover.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-hover@2.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-maximized-active-backdrop.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-maximized-active-backdrop@2.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-maximized-active.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-maximized-active@2.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-maximized-backdrop.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-maximized-backdrop@2.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-maximized-hover-backdrop.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-maximized-hover-backdrop@2.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-maximized-hover.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-maximized-hover@2.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-maximized.png
/usr/share/themes/Breeze/assets/titlebutton-maximize-maximized@2.png
/usr/share/themes/Breeze/assets/titlebutton-maximize.png
/usr/share/themes/Breeze/assets/titlebutton-maximize@2.png
/usr/share/themes/Breeze/assets/titlebutton-minimize-active-backdrop.png
/usr/share/themes/Breeze/assets/titlebutton-minimize-active-backdrop@2.png
/usr/share/themes/Breeze/assets/titlebutton-minimize-active.png
/usr/share/themes/Breeze/assets/titlebutton-minimize-active@2.png
/usr/share/themes/Breeze/assets/titlebutton-minimize-backdrop.png
/usr/share/themes/Breeze/assets/titlebutton-minimize-backdrop@2.png
/usr/share/themes/Breeze/assets/titlebutton-minimize-hover-backdrop.png
/usr/share/themes/Breeze/assets/titlebutton-minimize-hover-backdrop@2.png
/usr/share/themes/Breeze/assets/titlebutton-minimize-hover.png
/usr/share/themes/Breeze/assets/titlebutton-minimize-hover@2.png
/usr/share/themes/Breeze/assets/titlebutton-minimize.png
/usr/share/themes/Breeze/assets/titlebutton-minimize@2.png
/usr/share/themes/Breeze/assets/togglebutton-active.png
/usr/share/themes/Breeze/assets/togglebutton-hover.png
/usr/share/themes/Breeze/assets/togglebutton-insensitive.png
/usr/share/themes/Breeze/assets/togglebutton.png
/usr/share/themes/Breeze/assets/toolbar-background.png
/usr/share/themes/Breeze/assets/toolbutton-active.png
/usr/share/themes/Breeze/assets/toolbutton-hover.png
/usr/share/themes/Breeze/assets/toolbutton-toggled.png
/usr/share/themes/Breeze/assets/tree-header.png
/usr/share/themes/Breeze/gtk-2.0/gtkrc
/usr/share/themes/Breeze/gtk-2.0/widgets/buttons
/usr/share/themes/Breeze/gtk-2.0/widgets/default
/usr/share/themes/Breeze/gtk-2.0/widgets/entry
/usr/share/themes/Breeze/gtk-2.0/widgets/menu
/usr/share/themes/Breeze/gtk-2.0/widgets/misc
/usr/share/themes/Breeze/gtk-2.0/widgets/notebook
/usr/share/themes/Breeze/gtk-2.0/widgets/progressbar
/usr/share/themes/Breeze/gtk-2.0/widgets/range
/usr/share/themes/Breeze/gtk-2.0/widgets/scrollbar
/usr/share/themes/Breeze/gtk-2.0/widgets/styles
/usr/share/themes/Breeze/gtk-2.0/widgets/toolbar
/usr/share/themes/Breeze/gtk-3.18/gtk-dark.css
/usr/share/themes/Breeze/gtk-3.18/gtk.css
/usr/share/themes/Breeze/gtk-3.20/gtk-dark.css
/usr/share/themes/Breeze/gtk-3.20/gtk.css

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/breeze-gtk/COPYING.LIB
