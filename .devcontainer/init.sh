echo 'alias serve="/workspaces/pygeoapi/start.sh"' >> /root/.bashrc
source /root/.bashrc
chmod +x /workspaces/pygeoapi/start.sh

pip install -e .
python3 setup.py install

cp pygeoapi-config.yml example-config.yml
