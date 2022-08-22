{
  inputs.nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
  let
    pkgs = nixpkgs.legacyPackages.x86_64-linux;
  in
  {
    packages.x86_64-linux.default = pkgs.python3.pkgs.buildPythonPackage {
      name = "mondaybot";
      format = "pyproject";

      src = ./.;

      nativeBuildInputs = [ pkgs.python3.pkgs.poetry-core ];

      propagatedBuildInputs = [ pkgs.python3.pkgs.discordpy ];
    };
  };
}
