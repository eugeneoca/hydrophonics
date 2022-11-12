pyuic5 -x ui/dashboard.ui -o ./dashboard.py
pyuic5 -x ui/settings.ui -o ./settings.py
pyrcc5 ui/assets/assets.qrc -o assets_rc.py