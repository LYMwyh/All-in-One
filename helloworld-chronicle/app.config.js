import { defineConfig } from "@solidjs/start/config";
/* @ts-ignore */
import pkg from "@vinxi/plugin-mdx";
import tailwindcss from "@tailwindcss/vite";

const { default: mdx } = pkg;
export default defineConfig({
  extensions: ["mdx", "md"],
  vite: {
    plugins: [
      tailwindcss(),
      mdx.withImports({})({
        jsx: true,
        jsxImportSource: "solid-js",
        providerImportSource: "solid-mdx"
      })
    ]
  }
});
