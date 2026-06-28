#!/bin/bash
# deploy-to-netlify.sh
# Run this from ~/Documents/Claude's Projects/ to deploy both landing pages.
# It copies files into your agency folder, then triggers Netlify deploy.

AGENCY=~/Documents/etsy-agent/agency
SRC=~/Documents/Claude\'s\ Projects

echo "📂 Creating agency folder if needed..."
mkdir -p "$AGENCY"

echo "📂 Copying landing pages..."
cp "$SRC/etsy-landing.html"    "$AGENCY/etsy.html"
cp "$SRC/shopify-landing.html" "$AGENCY/shopify.html"

echo "🖼  Copying Divine Collection images..."
mkdir -p "$AGENCY/divine_collection/jpeg_export"
cp "$SRC/divine_collection/jpeg_export/"*.jpg "$AGENCY/divine_collection/jpeg_export/"

echo "🖼  Copying Minimalist Art images..."
mkdir -p "$AGENCY/pinterest_pins"
cp "$SRC/pinterest_pins/"*.jpg "$AGENCY/pinterest_pins/"

echo "🚀 Deploying to Netlify..."
cd "$AGENCY"
npx -y netlify-cli deploy --prod --dir . --site 69d10228-919d-48d9-9016-fc0023089dde

echo "✅ Done! Pages live at:"
echo "   https://j2dao-automation.netlify.app/etsy"
echo "   https://j2dao-automation.netlify.app/shopify"
