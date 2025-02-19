{
  description = "Development environment for web projects";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs";

  outputs = { self, nixpkgs }: {
    devShells.x86_64-linux.default = nixpkgs.legacyPackages.x86_64-linux.mkShell {
      buildInputs = [
        nixpkgs.nodejs_18   # Gunakan Node.js versi 18
        nixpkgs.python3      # Jika ingin pakai Python Simple Server
      ];

      shellHook = ''
        echo "🚀 Web Server otomatis berjalan di http://localhost:8080"
        python3 -m http.server 8080 &
      '';
    };
  };
}
