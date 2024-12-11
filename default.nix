{
  pkgs ? import (fetchTarball {
    # nixos-unstable rev 2024-12-03
    url = "https://github.com/NixOS/nixpkgs/archive/55d15ad12a74eb7d4646254e13638ad0c4128776.tar.gz";
  }) { },
}:

pkgs.callPackage (
  {
    stdenv,
    python312Packages,
    yosys,
  }:
  pkgs.stdenv.mkDerivation (finalAttrs: {
    pname = "rtlil-corpus";
    version = "1";

    src = builtins.path {
      name = "rtlil-corpus-source";
      path = ./.;
    };

    nativeBuildInputs = [
      python312Packages.python
      python312Packages.amaranth
      yosys
    ];

    dontBuild = true;

    installPhase = ''
      runHook preInstall
      mkdir -p "$out"
      python3 rtlil_from_amaranth_examples.py --amaranth "${finalAttrs.src}/amaranth" --outdir "$out"
      python3 rtlil_from_vexriscv_sources.py --verilog "${finalAttrs.src}/VexRiscv-verilog" --outdir "$out"
      runHook postInstall
    '';
  })
) { }
