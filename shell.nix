{ pkgs ? import (fetchTarball {
  url = "https://github.com/NixOS/nixpkgs/archive/refs/tags/24.05.tar.gz";
}) {} }:

pkgs.mkShell {
  buildInputs = [ 
    pkgs.python312Packages.amaranth
    ];
  shellHook = ''
    ./mkcorpus.sh
  '';
}