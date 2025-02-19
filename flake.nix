{
  description = "Development environment for web projects";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs";
  };

  outputs = { self, nixpkgs }: 
  let 
    pkgs = import nixpkgs { system = "x86_64-linux"; };
  in {
    devShells.x86_64-linux.default = pkgs.mkShell {
      buildInputs = [
        pkgs.nodejs_18   # Node.js untuk development web
        pkgs.python3      # Python3 jika ingin pakai Simple Server
      ];

      shellHook = ''
        echo "🚀 Web Server otomatis berjalan di http://localhost:8080"
        python3 -m http.server 8080 &
      '';
    };
  };
}
