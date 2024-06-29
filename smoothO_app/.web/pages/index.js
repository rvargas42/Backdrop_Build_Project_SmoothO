/** @jsxImportSource @emotion/react */


import { Fragment, useCallback, useContext, useRef } from "react"
import { Box as RadixThemesBox, Container as RadixThemesContainer, Flex as RadixThemesFlex, ScrollArea as RadixThemesScrollArea, Text as RadixThemesText, TextField as RadixThemesTextField } from "@radix-ui/themes"
import { Event, refs } from "/utils/state"
import ReactDropzone from "react-dropzone"
import { EventLoopContext, UploadFilesContext } from "/utils/context"
import NextHead from "next/head"



export function Reactdropzone_06e5cf99746bb031d38ec09d5a59dcc0 () {
  const ref_documentUpload = useRef(null); refs['ref_documentUpload'] = ref_documentUpload;
  const [filesById, setFilesById] = useContext(UploadFilesContext);
  const [addEvents, connectErrors] = useContext(EventLoopContext);

  const on_drop_5a6b112f6ad6b9d075d92693862e3d4d = useCallback(e => setFilesById(filesById => {
    const updatedFilesById = Object.assign({}, filesById);
    updatedFilesById[`documentUpload`] = e;
    return updatedFilesById;
  })
    , [addEvents, Event, filesById, setFilesById])


  return (
    <ReactDropzone id={`documentUpload`} multiple={true} onDrop={on_drop_5a6b112f6ad6b9d075d92693862e3d4d} ref={ref_documentUpload}>
  {({ getRootProps, getInputProps }) => (
    <RadixThemesBox className={`rx-Upload`} css={{"display": "flex", "border-style": "dotted", "margin": "auto", "width": "80%", "height": "10%", "align-items": "center", "border": "1px dashed var(--accent-12)", "padding": "5em", "textAlign": "center"}} id={`documentUpload`} ref={ref_documentUpload} {...getRootProps()}>
    <input type={`file`} {...getInputProps()}/>
    <RadixThemesText as={`p`}>
    {`Drag and drop files here or click to select files`}
  </RadixThemesText>
  </RadixThemesBox>
  )}
</ReactDropzone>
  )
}

export default function Component() {
  const ref_LLMResponse = useRef(null); refs['ref_LLMResponse'] = ref_LLMResponse;

  return (
    <Fragment>
  <RadixThemesFlex align={`start`} className={`rx-Stack`} css={{"border-width": "1px", "border-color": "white", "height": "100vh", "display": "flex", "align-items": "center"}} direction={`row`} gap={`3`}>
  <RadixThemesContainer css={{"width": "41%", "height": "90vh", "display": "flex", "border-width": "1px", "border-color": "white", "margin": "auto", "padding": "16px"}} size={`3`}>
  <Reactdropzone_06e5cf99746bb031d38ec09d5a59dcc0/>
</RadixThemesContainer>
  <RadixThemesContainer css={{"width": "59%", "height": "90vh", "display": "flex", "border-width": "1px", "border-color": "white", "padding": "16px"}} size={`3`}>
  <RadixThemesContainer css={{"padding": "16px"}} size={`3`}>
  <RadixThemesScrollArea css={{"height": "45rem", "border-width": "1px", "border-color": "white", "margin": "auto"}} scrollbars={`vertical`} type={`always`}>
  <RadixThemesFlex direction={`column`} gap={`4`}>
  <RadixThemesText as={`p`} id={`LLMResponse`} ref={ref_LLMResponse}/>
</RadixThemesFlex>
</RadixThemesScrollArea>
</RadixThemesContainer>
  <RadixThemesContainer css={{"border-width": "1px", "border-color": "white", "display": "flex", "margin-top": "auto", "bottom": "0", "padding": "16px"}} size={`3`}>
  <RadixThemesTextField.Root css={{"position": "relative", "bottom": "0"}} placeholder={`Talk with your knowledge base...`}/>
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
