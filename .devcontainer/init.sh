echo 'alias serve="/workspaces/pygeoapi/start.sh"' >> /root/.bashrc
echo 'alias setup="python3 /workspaces/pygeoapi/setup.py install"' >> /root/.bashrc
echo 'alias reinit="/workspaces/pygeoapi/reinit.sh"' >> /root/.bashrc

chmod +x /workspaces/pygeoapi/start.sh
chmod +x /workspaces/pygeoapi/reinit.sh

source /root/.bashrc

pip install -e .
python3 setup.py install

cp pygeoapi-config.yml example-config.yml
