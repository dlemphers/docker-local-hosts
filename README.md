Docker /etc/hosts sync
======================

Simple CLI tool for updating your local /etc/hosts file with a .local pointer to a Docker container's internal IP address.

Use Case
--------

Say you're developing a Nodejs app, and you want to run that inside a Docker container during development, but access it from your desktop browser. 

You could publish the container port to a well known port, but that might cause conflicts with other services, and isn't great in terms of isolation. The other option is to inspect the container's internal IP address and use that, but if you want to reference this container in another project, that's going to become tedios.

`docker-local-hosts` solves that problem by inspecting the container, grabbing it's IP address, and safely updating your /etc/hosts file with a .local based pointer. You can run this inside your Makefile to sync the container address each time you create the container, for example, as part of docker compose. 

Usage
-----

`docker-local-hosts map -c <container_name> -l </etc/hosts name>`

This will create an entry in your `/etc/hosts` file that points the internal IP address of the container to a hostname you provided with `.local` appended to it.

You can now access that container from your desktop using the `.local` hostname.
