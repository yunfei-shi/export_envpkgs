#!/usr/bin/env python3

import os, shutil

pkg_root = '/home/ubuntu/miniconda3/pkgs'
pkgs = os.popen('conda list').read().split('\n')
pkgs = pkgs[3:-1]

pkg_names = []
pkg_paths = []
for pkg in pkgs:
    name = ' '.join(pkg.split()[:3]).replace(' ', '-')
    pkg_names.append(name)
    pkg_paths.append(os.path.join(pkg_root, name))

if not os.path.exists('pkgs'):
    os.mkdir('./pkgs')

dst = './pkgs/'
for pkg in pkg_paths:
    tar_file = pkg + '.tar.bz2'
    conda_file = pkg + '.conda'
    if os.path.isfile(tar_file):
        shutil.copyfile(tar_file, dst+tar_file.split('/')[-1])
    if os.path.isfile(conda_file):
        shutil.copyfile(conda_file, dst+tar_file.split('/')[-1])
