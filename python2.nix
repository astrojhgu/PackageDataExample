# default.nix
# 此文件仅在操作系统为nixos时有用，其余情况忽略
let a=import /etc/nixos/overlays/pkgs.nix; in 
with import <nixpkgs> {
    overlays=[
    a    
    ];
};
stdenv.mkDerivation {
    name = "controller"; # Probably put a more meaningful name here
    buildInputs =  [
    (python2Full.withPackages (ps: with ps; [
    setuptools
     ]))
    ];
}
