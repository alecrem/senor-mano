import chokidar from "chokidar";
import { spawn } from "child_process";
import { join, dirname } from "path";
import { fileURLToPath } from "url";
import { setTimeout, clearTimeout } from "timers";
import { utimesSync } from "fs";

const __dirname = dirname(fileURLToPath(import.meta.url));

// Path to the markdown source files
const markdownSourcePath = join(__dirname, "..", "ejercicios-src", "markdown");

console.log("🔍 Watching for markdown file changes...");
console.log(`📁 Watching: ${markdownSourcePath}`);

let isGenerating = false;

function generateMarkdownImports() {
  if (isGenerating) {
    console.log("⏳ Generation already in progress, skipping...");
    return;
  }

  isGenerating = true;
  console.log("🔄 Markdown files changed, regenerating imports...");

  const child = spawn("node", ["generate-markdown-imports.js"], {
    stdio: "inherit",
    cwd: __dirname,
  });

  child.on("close", (code) => {
    isGenerating = false;
    if (code === 0) {
      console.log("✅ Markdown imports regenerated successfully!");
      
      // Touch the markdown-content.ts file after a small delay to trigger Vite hot reload
      setTimeout(() => {
        const markdownContentPath = join(__dirname, "app", "data", "markdown-content.ts");
        try {
          const now = new Date();
          utimesSync(markdownContentPath, now, now);
          console.log("🔄 Triggered Vite hot reload for markdown content");
        } catch (error) {
          console.warn("⚠️  Could not trigger hot reload:", error.message);
        }
      }, 100);
    } else {
      console.error("❌ Failed to regenerate markdown imports");
    }
  });

  child.on("error", (err) => {
    isGenerating = false;
    console.error("❌ Error running generate-markdown-imports.js:", err);
  });
}

// Watch for changes in markdown files
const watcher = chokidar.watch(markdownSourcePath, {
  ignoreInitial: true,
  ignored: /(^|[/\\])\../, // ignore dotfiles
});

// Debug: log when watcher is ready
watcher.on('ready', () => {
  console.log(`🎯 Watcher is ready and watching: ${markdownSourcePath}`);
});

// Debounce multiple changes that happen quickly
let debounceTimer;
function debouncedGenerate() {
  clearTimeout(debounceTimer);
  debounceTimer = setTimeout(() => {
    generateMarkdownImports();
  }, 300); // Wait 300ms after the last change
}

watcher
  .on("add", (path) => {
    if (path.endsWith('.md')) {
      console.log(`📝 File added: ${path}`);
      debouncedGenerate();
    }
  })
  .on("change", (path) => {
    if (path.endsWith('.md')) {
      console.log(`📝 File changed: ${path}`);
      debouncedGenerate();
    }
  })
  .on("unlink", (path) => {
    if (path.endsWith('.md')) {
      console.log(`🗑️  File removed: ${path}`);
      debouncedGenerate();
    }
  })
  .on("error", (error) => {
    console.error("❌ Watcher error:", error);
  });

console.log(
  "✅ File watcher started! Make changes to markdown files to see auto-regeneration."
);

// Handle graceful shutdown
process.on("SIGINT", () => {
  console.log("\n🛑 Shutting down file watcher...");
  watcher.close().then(() => {
    console.log("✅ File watcher stopped.");
    process.exit(0);
  });
});
