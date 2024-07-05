/** @jsxImportSource @emotion/react */


import { Head, Html, Main, NextScript } from "next/document"
import Script from "next/script"



export default function Document() {
  return (
    <Html lang={`en`}>
  <Head>
  <Script strategy={`afterInteractive`}>
  {`/scripts/chatPageMain.js`}
</Script>
</Head>
  <body>
  <Main/>
  <NextScript/>
</body>
</Html>
  )
}
