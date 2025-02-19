{
  description = "Project IDX with Nix Flakes";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }: {
    devShells.default = nixpkgs.legacyPackages.x86_64-linux.mkShell {
      buildInputs = [
        nixpkgs.legacyPackages.x86_64-linux.nodejs_18
        nixpkgs.legacyPackages.x86_64-linux.git
        nixpkgs.legacyPackages.x86_64-linux.python3
      ];
    };
  };
}
