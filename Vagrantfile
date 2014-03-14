#
# video annotation autodeploy
#

# config options
ip = '10.0.0.53'
hostname = 'vidlabel'
ram = '1024'

# provision script
$script = <<SCRIPT
sudo apt-get -y -qq update
sudo apt-get install -y -qq python3-pip
sudo pip3 install -q Django==1.6
sudo locale-gen en_GB.UTF-8
wget --quiet -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | sudo apt-key add -
if [ ! -f /etc/apt/sources.list.d/pgdg.list ]
then
    sudo bash -c "echo 'deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main' >> /etc/apt/sources.list.d/pgdg.list"
    sudo apt-get -qq update
fi
sudo apt-get install -y -qq postgresql
sudo apt-get install -y -qq libpq-dev
sudo pip3 install -q psycopg2
sed -i -e "s/;32m/;35m/" .bashrc
sed -i -e "s/\#force/force/" .bashrc
sudo locale-gen en_GB.UTF-8
SCRIPT

Vagrant.configure("2") do |config|
    config.vm.box = 'saucy'
    config.vm.box_url = 'http://cloud-images.ubuntu.com/vagrant/saucy/current/saucy-server-cloudimg-i386-vagrant-disk1.box'
    config.vm.hostname = hostname
    config.vm.network :private_network, ip: ip
    config.vm.network :forwarded_port, guest: 31337, host: 31337

    config.vm.provider :virtualbox do |vb|
        vb.customize [
            'modifyvm', :id,
            '--name', hostname,
            '--memory', ram
        ]
    end
    config.vm.provision :shell, :inline => $script
end
