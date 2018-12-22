#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : seahorse
Version  : 3.30.1.1
Release  : 5
URL      : https://download.gnome.org/sources/seahorse/3.30/seahorse-3.30.1.1.tar.xz
Source0  : https://download.gnome.org/sources/seahorse/3.30/seahorse-3.30.1.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.1 GPL-2.0 LGPL-2.1
Requires: seahorse-bin = %{version}-%{release}
Requires: seahorse-data = %{version}-%{release}
Requires: seahorse-libexec = %{version}-%{release}
Requires: seahorse-license = %{version}-%{release}
Requires: seahorse-locales = %{version}-%{release}
Requires: seahorse-man = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : gcr-data
BuildRequires : gnupg
BuildRequires : gpgme-dev
BuildRequires : libgpg-error-dev
BuildRequires : libsecret-dev
BuildRequires : libsoup-dev
BuildRequires : openldap-dev
BuildRequires : openssh
BuildRequires : p11-kit-dev
BuildRequires : pkgconfig(gcr-3)
BuildRequires : vala

%description
# Seahorse
Seahorse is a graphical interface for managing and using encryption keys.
Currently it supports PGP keys (using GPG/GPGME) and SSH keys. Its goal is to
provide an easy to use Key Management Tool, along with an easy to use interface
for encryption operations.

%package bin
Summary: bin components for the seahorse package.
Group: Binaries
Requires: seahorse-data = %{version}-%{release}
Requires: seahorse-libexec = %{version}-%{release}
Requires: seahorse-license = %{version}-%{release}
Requires: seahorse-man = %{version}-%{release}

%description bin
bin components for the seahorse package.


%package data
Summary: data components for the seahorse package.
Group: Data

%description data
data components for the seahorse package.


%package doc
Summary: doc components for the seahorse package.
Group: Documentation
Requires: seahorse-man = %{version}-%{release}

%description doc
doc components for the seahorse package.


%package libexec
Summary: libexec components for the seahorse package.
Group: Default
Requires: seahorse-license = %{version}-%{release}

%description libexec
libexec components for the seahorse package.


%package license
Summary: license components for the seahorse package.
Group: Default

%description license
license components for the seahorse package.


%package locales
Summary: locales components for the seahorse package.
Group: Default

%description locales
locales components for the seahorse package.


%package man
Summary: man components for the seahorse package.
Group: Default

%description man
man components for the seahorse package.


%prep
%setup -q -n seahorse-3.30.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545508734
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --prefix /usr --buildtype=plain -Dkey-sharing=false  builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/seahorse
cp COPYING %{buildroot}/usr/share/package-licenses/seahorse/COPYING
cp COPYING-DOCS %{buildroot}/usr/share/package-licenses/seahorse/COPYING-DOCS
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/seahorse/COPYING.LIB
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang seahorse

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/seahorse

%files data
%defattr(-,root,root,-)
/usr/share/applications/seahorse.desktop
/usr/share/dbus-1/services/org.gnome.seahorse.Application.service
/usr/share/glib-2.0/schemas/org.gnome.seahorse.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.seahorse.manager.gschema.xml
/usr/share/glib-2.0/schemas/org.gnome.seahorse.window.gschema.xml
/usr/share/gnome-shell/search-providers/seahorse-search-provider.ini
/usr/share/icons/hicolor/16x16/apps/seahorse-preferences.png
/usr/share/icons/hicolor/16x16/apps/seahorse.png
/usr/share/icons/hicolor/22x22/apps/seahorse-preferences.png
/usr/share/icons/hicolor/22x22/apps/seahorse.png
/usr/share/icons/hicolor/24x24/apps/seahorse-preferences.png
/usr/share/icons/hicolor/24x24/apps/seahorse.png
/usr/share/icons/hicolor/256x256/apps/seahorse.png
/usr/share/icons/hicolor/32x32/apps/seahorse-preferences.png
/usr/share/icons/hicolor/32x32/apps/seahorse.png
/usr/share/icons/hicolor/48x48/apps/seahorse-preferences.png
/usr/share/icons/hicolor/48x48/apps/seahorse.png
/usr/share/icons/hicolor/symbolic/apps/seahorse-symbolic.svg
/usr/share/metainfo/seahorse.appdata.xml
/usr/share/seahorse/icons/hicolor/22x22/apps/seahorse-key-personal.png
/usr/share/seahorse/icons/hicolor/22x22/apps/seahorse-key-ssh.png
/usr/share/seahorse/icons/hicolor/22x22/apps/seahorse-key.png
/usr/share/seahorse/icons/hicolor/22x22/apps/seahorse-person.png
/usr/share/seahorse/icons/hicolor/22x22/status/seahorse-sign-bad.png
/usr/share/seahorse/icons/hicolor/22x22/status/seahorse-sign-ok.png
/usr/share/seahorse/icons/hicolor/22x22/status/seahorse-sign.png
/usr/share/seahorse/icons/hicolor/48x48/apps/seahorse-key-personal.png
/usr/share/seahorse/icons/hicolor/48x48/apps/seahorse-key-ssh.png
/usr/share/seahorse/icons/hicolor/48x48/apps/seahorse-key.png
/usr/share/seahorse/icons/hicolor/48x48/apps/seahorse-person.png
/usr/share/seahorse/icons/hicolor/48x48/status/seahorse-sign-bad.png
/usr/share/seahorse/icons/hicolor/48x48/status/seahorse-sign-ok.png
/usr/share/seahorse/icons/hicolor/48x48/status/seahorse-sign-unknown.png
/usr/share/seahorse/icons/hicolor/48x48/status/seahorse-sign.png

%files doc
%defattr(0644,root,root,0755)
/usr/share/help/C/seahorse/about-diff-private-public.page
/usr/share/help/C/seahorse/about-pgp.page
/usr/share/help/C/seahorse/about-ssh.page
/usr/share/help/C/seahorse/concepts.page
/usr/share/help/C/seahorse/glossary.page
/usr/share/help/C/seahorse/index.page
/usr/share/help/C/seahorse/introduction.page
/usr/share/help/C/seahorse/key-servers-add.page
/usr/share/help/C/seahorse/keyring-change-default.page
/usr/share/help/C/seahorse/keyring-create.page
/usr/share/help/C/seahorse/keyring-lock.page
/usr/share/help/C/seahorse/keyring-unlock.page
/usr/share/help/C/seahorse/keyring-update-password.page
/usr/share/help/C/seahorse/keyring.page
/usr/share/help/C/seahorse/legal.xml
/usr/share/help/C/seahorse/media/seahorse.png
/usr/share/help/C/seahorse/misc-key-backup.page
/usr/share/help/C/seahorse/misc-key-fingerprint.page
/usr/share/help/C/seahorse/passwords-stored-create.page
/usr/share/help/C/seahorse/passwords-view.page
/usr/share/help/C/seahorse/pgp-create.page
/usr/share/help/C/seahorse/pgp-delete.page
/usr/share/help/C/seahorse/pgp-expiration-change.page
/usr/share/help/C/seahorse/pgp-expired.page
/usr/share/help/C/seahorse/pgp-export.page
/usr/share/help/C/seahorse/pgp-import.page
/usr/share/help/C/seahorse/pgp-photoid.page
/usr/share/help/C/seahorse/pgp-publish.page
/usr/share/help/C/seahorse/pgp-retrieve-remote.page
/usr/share/help/C/seahorse/pgp-sign.page
/usr/share/help/C/seahorse/pgp-subkeys.page
/usr/share/help/C/seahorse/pgp-sync.page
/usr/share/help/C/seahorse/pgp-userid-add.page
/usr/share/help/C/seahorse/pgp-userid-primary.page
/usr/share/help/C/seahorse/pgp-userid-remove.page
/usr/share/help/C/seahorse/pgp-userid.page
/usr/share/help/C/seahorse/ssh-connect-remote.page
/usr/share/help/C/seahorse/ssh-create.page
/usr/share/help/C/seahorse/ssh-export.page
/usr/share/help/C/seahorse/ssh-import.page
/usr/share/help/C/seahorse/subkeys-add.page
/usr/share/help/C/seahorse/subkeys-examine.page
/usr/share/help/C/seahorse/subkeys-revoke.page
/usr/share/help/cs/seahorse/about-diff-private-public.page
/usr/share/help/cs/seahorse/about-pgp.page
/usr/share/help/cs/seahorse/about-ssh.page
/usr/share/help/cs/seahorse/concepts.page
/usr/share/help/cs/seahorse/glossary.page
/usr/share/help/cs/seahorse/index.page
/usr/share/help/cs/seahorse/introduction.page
/usr/share/help/cs/seahorse/key-servers-add.page
/usr/share/help/cs/seahorse/keyring-change-default.page
/usr/share/help/cs/seahorse/keyring-create.page
/usr/share/help/cs/seahorse/keyring-lock.page
/usr/share/help/cs/seahorse/keyring-unlock.page
/usr/share/help/cs/seahorse/keyring-update-password.page
/usr/share/help/cs/seahorse/keyring.page
/usr/share/help/cs/seahorse/legal.xml
/usr/share/help/cs/seahorse/media/seahorse.png
/usr/share/help/cs/seahorse/misc-key-backup.page
/usr/share/help/cs/seahorse/misc-key-fingerprint.page
/usr/share/help/cs/seahorse/passwords-stored-create.page
/usr/share/help/cs/seahorse/passwords-view.page
/usr/share/help/cs/seahorse/pgp-create.page
/usr/share/help/cs/seahorse/pgp-delete.page
/usr/share/help/cs/seahorse/pgp-expiration-change.page
/usr/share/help/cs/seahorse/pgp-expired.page
/usr/share/help/cs/seahorse/pgp-export.page
/usr/share/help/cs/seahorse/pgp-import.page
/usr/share/help/cs/seahorse/pgp-photoid.page
/usr/share/help/cs/seahorse/pgp-publish.page
/usr/share/help/cs/seahorse/pgp-retrieve-remote.page
/usr/share/help/cs/seahorse/pgp-sign.page
/usr/share/help/cs/seahorse/pgp-subkeys.page
/usr/share/help/cs/seahorse/pgp-sync.page
/usr/share/help/cs/seahorse/pgp-userid-add.page
/usr/share/help/cs/seahorse/pgp-userid-primary.page
/usr/share/help/cs/seahorse/pgp-userid-remove.page
/usr/share/help/cs/seahorse/pgp-userid.page
/usr/share/help/cs/seahorse/ssh-connect-remote.page
/usr/share/help/cs/seahorse/ssh-create.page
/usr/share/help/cs/seahorse/ssh-export.page
/usr/share/help/cs/seahorse/ssh-import.page
/usr/share/help/cs/seahorse/subkeys-add.page
/usr/share/help/cs/seahorse/subkeys-examine.page
/usr/share/help/cs/seahorse/subkeys-revoke.page
/usr/share/help/de/seahorse/about-diff-private-public.page
/usr/share/help/de/seahorse/about-pgp.page
/usr/share/help/de/seahorse/about-ssh.page
/usr/share/help/de/seahorse/concepts.page
/usr/share/help/de/seahorse/glossary.page
/usr/share/help/de/seahorse/index.page
/usr/share/help/de/seahorse/introduction.page
/usr/share/help/de/seahorse/key-servers-add.page
/usr/share/help/de/seahorse/keyring-change-default.page
/usr/share/help/de/seahorse/keyring-create.page
/usr/share/help/de/seahorse/keyring-lock.page
/usr/share/help/de/seahorse/keyring-unlock.page
/usr/share/help/de/seahorse/keyring-update-password.page
/usr/share/help/de/seahorse/keyring.page
/usr/share/help/de/seahorse/legal.xml
/usr/share/help/de/seahorse/media/seahorse.png
/usr/share/help/de/seahorse/misc-key-backup.page
/usr/share/help/de/seahorse/misc-key-fingerprint.page
/usr/share/help/de/seahorse/passwords-stored-create.page
/usr/share/help/de/seahorse/passwords-view.page
/usr/share/help/de/seahorse/pgp-create.page
/usr/share/help/de/seahorse/pgp-delete.page
/usr/share/help/de/seahorse/pgp-expiration-change.page
/usr/share/help/de/seahorse/pgp-expired.page
/usr/share/help/de/seahorse/pgp-export.page
/usr/share/help/de/seahorse/pgp-import.page
/usr/share/help/de/seahorse/pgp-photoid.page
/usr/share/help/de/seahorse/pgp-publish.page
/usr/share/help/de/seahorse/pgp-retrieve-remote.page
/usr/share/help/de/seahorse/pgp-sign.page
/usr/share/help/de/seahorse/pgp-subkeys.page
/usr/share/help/de/seahorse/pgp-sync.page
/usr/share/help/de/seahorse/pgp-userid-add.page
/usr/share/help/de/seahorse/pgp-userid-primary.page
/usr/share/help/de/seahorse/pgp-userid-remove.page
/usr/share/help/de/seahorse/pgp-userid.page
/usr/share/help/de/seahorse/ssh-connect-remote.page
/usr/share/help/de/seahorse/ssh-create.page
/usr/share/help/de/seahorse/ssh-export.page
/usr/share/help/de/seahorse/ssh-import.page
/usr/share/help/de/seahorse/subkeys-add.page
/usr/share/help/de/seahorse/subkeys-examine.page
/usr/share/help/de/seahorse/subkeys-revoke.page
/usr/share/help/el/seahorse/about-diff-private-public.page
/usr/share/help/el/seahorse/about-pgp.page
/usr/share/help/el/seahorse/about-ssh.page
/usr/share/help/el/seahorse/concepts.page
/usr/share/help/el/seahorse/glossary.page
/usr/share/help/el/seahorse/index.page
/usr/share/help/el/seahorse/introduction.page
/usr/share/help/el/seahorse/key-servers-add.page
/usr/share/help/el/seahorse/keyring-change-default.page
/usr/share/help/el/seahorse/keyring-create.page
/usr/share/help/el/seahorse/keyring-lock.page
/usr/share/help/el/seahorse/keyring-unlock.page
/usr/share/help/el/seahorse/keyring-update-password.page
/usr/share/help/el/seahorse/keyring.page
/usr/share/help/el/seahorse/legal.xml
/usr/share/help/el/seahorse/media/seahorse.png
/usr/share/help/el/seahorse/misc-key-backup.page
/usr/share/help/el/seahorse/misc-key-fingerprint.page
/usr/share/help/el/seahorse/passwords-stored-create.page
/usr/share/help/el/seahorse/passwords-view.page
/usr/share/help/el/seahorse/pgp-create.page
/usr/share/help/el/seahorse/pgp-delete.page
/usr/share/help/el/seahorse/pgp-expiration-change.page
/usr/share/help/el/seahorse/pgp-expired.page
/usr/share/help/el/seahorse/pgp-export.page
/usr/share/help/el/seahorse/pgp-import.page
/usr/share/help/el/seahorse/pgp-photoid.page
/usr/share/help/el/seahorse/pgp-publish.page
/usr/share/help/el/seahorse/pgp-retrieve-remote.page
/usr/share/help/el/seahorse/pgp-sign.page
/usr/share/help/el/seahorse/pgp-subkeys.page
/usr/share/help/el/seahorse/pgp-sync.page
/usr/share/help/el/seahorse/pgp-userid-add.page
/usr/share/help/el/seahorse/pgp-userid-primary.page
/usr/share/help/el/seahorse/pgp-userid-remove.page
/usr/share/help/el/seahorse/pgp-userid.page
/usr/share/help/el/seahorse/ssh-connect-remote.page
/usr/share/help/el/seahorse/ssh-create.page
/usr/share/help/el/seahorse/ssh-export.page
/usr/share/help/el/seahorse/ssh-import.page
/usr/share/help/el/seahorse/subkeys-add.page
/usr/share/help/el/seahorse/subkeys-examine.page
/usr/share/help/el/seahorse/subkeys-revoke.page
/usr/share/help/es/seahorse/about-diff-private-public.page
/usr/share/help/es/seahorse/about-pgp.page
/usr/share/help/es/seahorse/about-ssh.page
/usr/share/help/es/seahorse/concepts.page
/usr/share/help/es/seahorse/glossary.page
/usr/share/help/es/seahorse/index.page
/usr/share/help/es/seahorse/introduction.page
/usr/share/help/es/seahorse/key-servers-add.page
/usr/share/help/es/seahorse/keyring-change-default.page
/usr/share/help/es/seahorse/keyring-create.page
/usr/share/help/es/seahorse/keyring-lock.page
/usr/share/help/es/seahorse/keyring-unlock.page
/usr/share/help/es/seahorse/keyring-update-password.page
/usr/share/help/es/seahorse/keyring.page
/usr/share/help/es/seahorse/legal.xml
/usr/share/help/es/seahorse/media/seahorse.png
/usr/share/help/es/seahorse/misc-key-backup.page
/usr/share/help/es/seahorse/misc-key-fingerprint.page
/usr/share/help/es/seahorse/passwords-stored-create.page
/usr/share/help/es/seahorse/passwords-view.page
/usr/share/help/es/seahorse/pgp-create.page
/usr/share/help/es/seahorse/pgp-delete.page
/usr/share/help/es/seahorse/pgp-expiration-change.page
/usr/share/help/es/seahorse/pgp-expired.page
/usr/share/help/es/seahorse/pgp-export.page
/usr/share/help/es/seahorse/pgp-import.page
/usr/share/help/es/seahorse/pgp-photoid.page
/usr/share/help/es/seahorse/pgp-publish.page
/usr/share/help/es/seahorse/pgp-retrieve-remote.page
/usr/share/help/es/seahorse/pgp-sign.page
/usr/share/help/es/seahorse/pgp-subkeys.page
/usr/share/help/es/seahorse/pgp-sync.page
/usr/share/help/es/seahorse/pgp-userid-add.page
/usr/share/help/es/seahorse/pgp-userid-primary.page
/usr/share/help/es/seahorse/pgp-userid-remove.page
/usr/share/help/es/seahorse/pgp-userid.page
/usr/share/help/es/seahorse/ssh-connect-remote.page
/usr/share/help/es/seahorse/ssh-create.page
/usr/share/help/es/seahorse/ssh-export.page
/usr/share/help/es/seahorse/ssh-import.page
/usr/share/help/es/seahorse/subkeys-add.page
/usr/share/help/es/seahorse/subkeys-examine.page
/usr/share/help/es/seahorse/subkeys-revoke.page
/usr/share/help/fr/seahorse/about-diff-private-public.page
/usr/share/help/fr/seahorse/about-pgp.page
/usr/share/help/fr/seahorse/about-ssh.page
/usr/share/help/fr/seahorse/concepts.page
/usr/share/help/fr/seahorse/glossary.page
/usr/share/help/fr/seahorse/index.page
/usr/share/help/fr/seahorse/introduction.page
/usr/share/help/fr/seahorse/key-servers-add.page
/usr/share/help/fr/seahorse/keyring-change-default.page
/usr/share/help/fr/seahorse/keyring-create.page
/usr/share/help/fr/seahorse/keyring-lock.page
/usr/share/help/fr/seahorse/keyring-unlock.page
/usr/share/help/fr/seahorse/keyring-update-password.page
/usr/share/help/fr/seahorse/keyring.page
/usr/share/help/fr/seahorse/legal.xml
/usr/share/help/fr/seahorse/media/seahorse.png
/usr/share/help/fr/seahorse/misc-key-backup.page
/usr/share/help/fr/seahorse/misc-key-fingerprint.page
/usr/share/help/fr/seahorse/passwords-stored-create.page
/usr/share/help/fr/seahorse/passwords-view.page
/usr/share/help/fr/seahorse/pgp-create.page
/usr/share/help/fr/seahorse/pgp-delete.page
/usr/share/help/fr/seahorse/pgp-expiration-change.page
/usr/share/help/fr/seahorse/pgp-expired.page
/usr/share/help/fr/seahorse/pgp-export.page
/usr/share/help/fr/seahorse/pgp-import.page
/usr/share/help/fr/seahorse/pgp-photoid.page
/usr/share/help/fr/seahorse/pgp-publish.page
/usr/share/help/fr/seahorse/pgp-retrieve-remote.page
/usr/share/help/fr/seahorse/pgp-sign.page
/usr/share/help/fr/seahorse/pgp-subkeys.page
/usr/share/help/fr/seahorse/pgp-sync.page
/usr/share/help/fr/seahorse/pgp-userid-add.page
/usr/share/help/fr/seahorse/pgp-userid-primary.page
/usr/share/help/fr/seahorse/pgp-userid-remove.page
/usr/share/help/fr/seahorse/pgp-userid.page
/usr/share/help/fr/seahorse/ssh-connect-remote.page
/usr/share/help/fr/seahorse/ssh-create.page
/usr/share/help/fr/seahorse/ssh-export.page
/usr/share/help/fr/seahorse/ssh-import.page
/usr/share/help/fr/seahorse/subkeys-add.page
/usr/share/help/fr/seahorse/subkeys-examine.page
/usr/share/help/fr/seahorse/subkeys-revoke.page
/usr/share/help/hu/seahorse/about-diff-private-public.page
/usr/share/help/hu/seahorse/about-pgp.page
/usr/share/help/hu/seahorse/about-ssh.page
/usr/share/help/hu/seahorse/concepts.page
/usr/share/help/hu/seahorse/glossary.page
/usr/share/help/hu/seahorse/index.page
/usr/share/help/hu/seahorse/introduction.page
/usr/share/help/hu/seahorse/key-servers-add.page
/usr/share/help/hu/seahorse/keyring-change-default.page
/usr/share/help/hu/seahorse/keyring-create.page
/usr/share/help/hu/seahorse/keyring-lock.page
/usr/share/help/hu/seahorse/keyring-unlock.page
/usr/share/help/hu/seahorse/keyring-update-password.page
/usr/share/help/hu/seahorse/keyring.page
/usr/share/help/hu/seahorse/legal.xml
/usr/share/help/hu/seahorse/media/seahorse.png
/usr/share/help/hu/seahorse/misc-key-backup.page
/usr/share/help/hu/seahorse/misc-key-fingerprint.page
/usr/share/help/hu/seahorse/passwords-stored-create.page
/usr/share/help/hu/seahorse/passwords-view.page
/usr/share/help/hu/seahorse/pgp-create.page
/usr/share/help/hu/seahorse/pgp-delete.page
/usr/share/help/hu/seahorse/pgp-expiration-change.page
/usr/share/help/hu/seahorse/pgp-expired.page
/usr/share/help/hu/seahorse/pgp-export.page
/usr/share/help/hu/seahorse/pgp-import.page
/usr/share/help/hu/seahorse/pgp-photoid.page
/usr/share/help/hu/seahorse/pgp-publish.page
/usr/share/help/hu/seahorse/pgp-retrieve-remote.page
/usr/share/help/hu/seahorse/pgp-sign.page
/usr/share/help/hu/seahorse/pgp-subkeys.page
/usr/share/help/hu/seahorse/pgp-sync.page
/usr/share/help/hu/seahorse/pgp-userid-add.page
/usr/share/help/hu/seahorse/pgp-userid-primary.page
/usr/share/help/hu/seahorse/pgp-userid-remove.page
/usr/share/help/hu/seahorse/pgp-userid.page
/usr/share/help/hu/seahorse/ssh-connect-remote.page
/usr/share/help/hu/seahorse/ssh-create.page
/usr/share/help/hu/seahorse/ssh-export.page
/usr/share/help/hu/seahorse/ssh-import.page
/usr/share/help/hu/seahorse/subkeys-add.page
/usr/share/help/hu/seahorse/subkeys-examine.page
/usr/share/help/hu/seahorse/subkeys-revoke.page
/usr/share/help/pl/seahorse/about-diff-private-public.page
/usr/share/help/pl/seahorse/about-pgp.page
/usr/share/help/pl/seahorse/about-ssh.page
/usr/share/help/pl/seahorse/concepts.page
/usr/share/help/pl/seahorse/glossary.page
/usr/share/help/pl/seahorse/index.page
/usr/share/help/pl/seahorse/introduction.page
/usr/share/help/pl/seahorse/key-servers-add.page
/usr/share/help/pl/seahorse/keyring-change-default.page
/usr/share/help/pl/seahorse/keyring-create.page
/usr/share/help/pl/seahorse/keyring-lock.page
/usr/share/help/pl/seahorse/keyring-unlock.page
/usr/share/help/pl/seahorse/keyring-update-password.page
/usr/share/help/pl/seahorse/keyring.page
/usr/share/help/pl/seahorse/legal.xml
/usr/share/help/pl/seahorse/media/seahorse.png
/usr/share/help/pl/seahorse/misc-key-backup.page
/usr/share/help/pl/seahorse/misc-key-fingerprint.page
/usr/share/help/pl/seahorse/passwords-stored-create.page
/usr/share/help/pl/seahorse/passwords-view.page
/usr/share/help/pl/seahorse/pgp-create.page
/usr/share/help/pl/seahorse/pgp-delete.page
/usr/share/help/pl/seahorse/pgp-expiration-change.page
/usr/share/help/pl/seahorse/pgp-expired.page
/usr/share/help/pl/seahorse/pgp-export.page
/usr/share/help/pl/seahorse/pgp-import.page
/usr/share/help/pl/seahorse/pgp-photoid.page
/usr/share/help/pl/seahorse/pgp-publish.page
/usr/share/help/pl/seahorse/pgp-retrieve-remote.page
/usr/share/help/pl/seahorse/pgp-sign.page
/usr/share/help/pl/seahorse/pgp-subkeys.page
/usr/share/help/pl/seahorse/pgp-sync.page
/usr/share/help/pl/seahorse/pgp-userid-add.page
/usr/share/help/pl/seahorse/pgp-userid-primary.page
/usr/share/help/pl/seahorse/pgp-userid-remove.page
/usr/share/help/pl/seahorse/pgp-userid.page
/usr/share/help/pl/seahorse/ssh-connect-remote.page
/usr/share/help/pl/seahorse/ssh-create.page
/usr/share/help/pl/seahorse/ssh-export.page
/usr/share/help/pl/seahorse/ssh-import.page
/usr/share/help/pl/seahorse/subkeys-add.page
/usr/share/help/pl/seahorse/subkeys-examine.page
/usr/share/help/pl/seahorse/subkeys-revoke.page
/usr/share/help/pt_BR/seahorse/about-diff-private-public.page
/usr/share/help/pt_BR/seahorse/about-pgp.page
/usr/share/help/pt_BR/seahorse/about-ssh.page
/usr/share/help/pt_BR/seahorse/concepts.page
/usr/share/help/pt_BR/seahorse/glossary.page
/usr/share/help/pt_BR/seahorse/index.page
/usr/share/help/pt_BR/seahorse/introduction.page
/usr/share/help/pt_BR/seahorse/key-servers-add.page
/usr/share/help/pt_BR/seahorse/keyring-change-default.page
/usr/share/help/pt_BR/seahorse/keyring-create.page
/usr/share/help/pt_BR/seahorse/keyring-lock.page
/usr/share/help/pt_BR/seahorse/keyring-unlock.page
/usr/share/help/pt_BR/seahorse/keyring-update-password.page
/usr/share/help/pt_BR/seahorse/keyring.page
/usr/share/help/pt_BR/seahorse/legal.xml
/usr/share/help/pt_BR/seahorse/media/seahorse.png
/usr/share/help/pt_BR/seahorse/misc-key-backup.page
/usr/share/help/pt_BR/seahorse/misc-key-fingerprint.page
/usr/share/help/pt_BR/seahorse/passwords-stored-create.page
/usr/share/help/pt_BR/seahorse/passwords-view.page
/usr/share/help/pt_BR/seahorse/pgp-create.page
/usr/share/help/pt_BR/seahorse/pgp-delete.page
/usr/share/help/pt_BR/seahorse/pgp-expiration-change.page
/usr/share/help/pt_BR/seahorse/pgp-expired.page
/usr/share/help/pt_BR/seahorse/pgp-export.page
/usr/share/help/pt_BR/seahorse/pgp-import.page
/usr/share/help/pt_BR/seahorse/pgp-photoid.page
/usr/share/help/pt_BR/seahorse/pgp-publish.page
/usr/share/help/pt_BR/seahorse/pgp-retrieve-remote.page
/usr/share/help/pt_BR/seahorse/pgp-sign.page
/usr/share/help/pt_BR/seahorse/pgp-subkeys.page
/usr/share/help/pt_BR/seahorse/pgp-sync.page
/usr/share/help/pt_BR/seahorse/pgp-userid-add.page
/usr/share/help/pt_BR/seahorse/pgp-userid-primary.page
/usr/share/help/pt_BR/seahorse/pgp-userid-remove.page
/usr/share/help/pt_BR/seahorse/pgp-userid.page
/usr/share/help/pt_BR/seahorse/ssh-connect-remote.page
/usr/share/help/pt_BR/seahorse/ssh-create.page
/usr/share/help/pt_BR/seahorse/ssh-export.page
/usr/share/help/pt_BR/seahorse/ssh-import.page
/usr/share/help/pt_BR/seahorse/subkeys-add.page
/usr/share/help/pt_BR/seahorse/subkeys-examine.page
/usr/share/help/pt_BR/seahorse/subkeys-revoke.page
/usr/share/help/ru/seahorse/about-diff-private-public.page
/usr/share/help/ru/seahorse/about-pgp.page
/usr/share/help/ru/seahorse/about-ssh.page
/usr/share/help/ru/seahorse/concepts.page
/usr/share/help/ru/seahorse/glossary.page
/usr/share/help/ru/seahorse/index.page
/usr/share/help/ru/seahorse/introduction.page
/usr/share/help/ru/seahorse/key-servers-add.page
/usr/share/help/ru/seahorse/keyring-change-default.page
/usr/share/help/ru/seahorse/keyring-create.page
/usr/share/help/ru/seahorse/keyring-lock.page
/usr/share/help/ru/seahorse/keyring-unlock.page
/usr/share/help/ru/seahorse/keyring-update-password.page
/usr/share/help/ru/seahorse/keyring.page
/usr/share/help/ru/seahorse/legal.xml
/usr/share/help/ru/seahorse/media/seahorse.png
/usr/share/help/ru/seahorse/misc-key-backup.page
/usr/share/help/ru/seahorse/misc-key-fingerprint.page
/usr/share/help/ru/seahorse/passwords-stored-create.page
/usr/share/help/ru/seahorse/passwords-view.page
/usr/share/help/ru/seahorse/pgp-create.page
/usr/share/help/ru/seahorse/pgp-delete.page
/usr/share/help/ru/seahorse/pgp-expiration-change.page
/usr/share/help/ru/seahorse/pgp-expired.page
/usr/share/help/ru/seahorse/pgp-export.page
/usr/share/help/ru/seahorse/pgp-import.page
/usr/share/help/ru/seahorse/pgp-photoid.page
/usr/share/help/ru/seahorse/pgp-publish.page
/usr/share/help/ru/seahorse/pgp-retrieve-remote.page
/usr/share/help/ru/seahorse/pgp-sign.page
/usr/share/help/ru/seahorse/pgp-subkeys.page
/usr/share/help/ru/seahorse/pgp-sync.page
/usr/share/help/ru/seahorse/pgp-userid-add.page
/usr/share/help/ru/seahorse/pgp-userid-primary.page
/usr/share/help/ru/seahorse/pgp-userid-remove.page
/usr/share/help/ru/seahorse/pgp-userid.page
/usr/share/help/ru/seahorse/ssh-connect-remote.page
/usr/share/help/ru/seahorse/ssh-create.page
/usr/share/help/ru/seahorse/ssh-export.page
/usr/share/help/ru/seahorse/ssh-import.page
/usr/share/help/ru/seahorse/subkeys-add.page
/usr/share/help/ru/seahorse/subkeys-examine.page
/usr/share/help/ru/seahorse/subkeys-revoke.page
/usr/share/help/sv/seahorse/about-diff-private-public.page
/usr/share/help/sv/seahorse/about-pgp.page
/usr/share/help/sv/seahorse/about-ssh.page
/usr/share/help/sv/seahorse/concepts.page
/usr/share/help/sv/seahorse/glossary.page
/usr/share/help/sv/seahorse/index.page
/usr/share/help/sv/seahorse/introduction.page
/usr/share/help/sv/seahorse/key-servers-add.page
/usr/share/help/sv/seahorse/keyring-change-default.page
/usr/share/help/sv/seahorse/keyring-create.page
/usr/share/help/sv/seahorse/keyring-lock.page
/usr/share/help/sv/seahorse/keyring-unlock.page
/usr/share/help/sv/seahorse/keyring-update-password.page
/usr/share/help/sv/seahorse/keyring.page
/usr/share/help/sv/seahorse/legal.xml
/usr/share/help/sv/seahorse/media/seahorse.png
/usr/share/help/sv/seahorse/misc-key-backup.page
/usr/share/help/sv/seahorse/misc-key-fingerprint.page
/usr/share/help/sv/seahorse/passwords-stored-create.page
/usr/share/help/sv/seahorse/passwords-view.page
/usr/share/help/sv/seahorse/pgp-create.page
/usr/share/help/sv/seahorse/pgp-delete.page
/usr/share/help/sv/seahorse/pgp-expiration-change.page
/usr/share/help/sv/seahorse/pgp-expired.page
/usr/share/help/sv/seahorse/pgp-export.page
/usr/share/help/sv/seahorse/pgp-import.page
/usr/share/help/sv/seahorse/pgp-photoid.page
/usr/share/help/sv/seahorse/pgp-publish.page
/usr/share/help/sv/seahorse/pgp-retrieve-remote.page
/usr/share/help/sv/seahorse/pgp-sign.page
/usr/share/help/sv/seahorse/pgp-subkeys.page
/usr/share/help/sv/seahorse/pgp-sync.page
/usr/share/help/sv/seahorse/pgp-userid-add.page
/usr/share/help/sv/seahorse/pgp-userid-primary.page
/usr/share/help/sv/seahorse/pgp-userid-remove.page
/usr/share/help/sv/seahorse/pgp-userid.page
/usr/share/help/sv/seahorse/ssh-connect-remote.page
/usr/share/help/sv/seahorse/ssh-create.page
/usr/share/help/sv/seahorse/ssh-export.page
/usr/share/help/sv/seahorse/ssh-import.page
/usr/share/help/sv/seahorse/subkeys-add.page
/usr/share/help/sv/seahorse/subkeys-examine.page
/usr/share/help/sv/seahorse/subkeys-revoke.page

%files libexec
%defattr(-,root,root,-)
/usr/libexec/seahorse/ssh-askpass
/usr/libexec/seahorse/xloadimage

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/seahorse/COPYING
/usr/share/package-licenses/seahorse/COPYING-DOCS
/usr/share/package-licenses/seahorse/COPYING.LIB

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/seahorse.1

%files locales -f seahorse.lang
%defattr(-,root,root,-)

