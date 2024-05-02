/** @jsxImportSource @emotion/react */


import { Fragment } from "react"
import { Box as RadixThemesBox, Container as RadixThemesContainer, Flex as RadixThemesFlex, TextField as RadixThemesTextField } from "@radix-ui/themes"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <RadixThemesFlex align={`start`} css={{"border-width": "1px", "border-color": "white", "height": "100vh", "display": "flex", "align-items": "center"}} direction={`row`} gap={`2`}>
  <RadixThemesContainer css={{"height": "90vh", "display": "flex", "border-width": "1px", "border-color": "white"}}/>
  <RadixThemesContainer css={{"height": "90vh", "display": "flex", "border-width": "1px", "border-color": "white"}}>
  <RadixThemesContainer css={{"border-width": "1px", "border-color": "white", "margin": "auto"}}>
  <Fragment>
  <RadixThemesBox>
  {`CSS color`}
</RadixThemesBox>
</Fragment>
</RadixThemesContainer>
  <RadixThemesContainer css={{"border-width": "1px", "border-color": "white", "margin": "auto", "bottom": "0"}}>
  <RadixThemesTextField.Input maxLength={`20`} placeholder={`Talk with your knowledge base...`}/>
</RadixThemesContainer>
</RadixThemesContainer>
</RadixThemesFlex>
  <NextHead>
  <title>
  {`Smootho App | Index`}
</title>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
