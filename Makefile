# ===========================================
# DanSch Portfolio - Makefile
# ===========================================

.PHONY: serve dev stop open help

# Default port
PORT ?= 8080

# Default target
help:
	@echo "DanSch Portfolio - Available commands:"
	@echo ""
	@echo "  make serve    - Start local server on port $(PORT)"
	@echo "  make dev      - Start server and open browser"
	@echo "  make open     - Open browser at localhost:$(PORT)"
	@echo "  make stop     - Stop running server on port $(PORT)"
	@echo ""
	@echo "Custom port: make serve PORT=3000"

serve:
	@echo "🚀 Starting server at http://localhost:$(PORT)"
	@python3 -m http.server $(PORT)

dev: open serve

open:
	@echo "🌐 Opening browser..."
	@open http://localhost:$(PORT) 2>/dev/null || xdg-open http://localhost:$(PORT) 2>/dev/null || echo "Please open http://localhost:$(PORT) manually"

stop:
	@echo "🛑 Stopping server on port $(PORT)..."
	@lsof -ti:$(PORT) | xargs kill -9 2>/dev/null || echo "No server running on port $(PORT)"
