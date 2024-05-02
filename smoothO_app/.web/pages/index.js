/** @jsxImportSource @emotion/react */


import { Fragment } from "react"
import { Container as RadixThemesContainer, Flex as RadixThemesFlex, TextField as RadixThemesTextField } from "@radix-ui/themes"
import NextHead from "next/head"



export default function Component() {

  return (
    <Fragment>
  <RadixThemesContainer>
  <RadixThemesFlex align={`start`} direction={`column`} gap={`2`}>
  <RadixThemesTextField.Input maxLength={`20`} placeholder={`Talk with your knowledge base...`}/>
</RadixThemesFlex>
</RadixThemesContainer>
  <NextHead>
  <title>
  {`Smootho App | Index`}
</title>
  <meta content={`favicon.ico`} property={`og:image`}/>
</NextHead>
</Fragment>
  )
}
