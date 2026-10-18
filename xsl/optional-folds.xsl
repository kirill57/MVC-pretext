<?xml version="1.0" encoding="UTF-8"?>
<!-- Use PreTeXt's native accessible details/summary rendering for optional blocks.
     The CLI places its matching core stylesheets in ./core at build time. -->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:exsl="http://exslt.org/common" exclude-result-prefixes="exsl">
  <xsl:import href="core/pretext-html.xsl"/>
  <xsl:param name="html.css.extra" select="'external/css/book.css'"/>
  <xsl:template match="exercise[starts-with(normalize-space(title), 'Optional:')]|proof[starts-with(normalize-space(title), 'Optional:')]|paragraphs[starts-with(normalize-space(title), 'Optional:')]" mode="is-hidden" priority="10">
    <xsl:text>true</xsl:text>
  </xsl:template>
  <!-- A WebGL frame inside a closed details element has zero layout size.
       Defer its initialization until visible to avoid Asymptote subdivision
       recursion at zero render tolerance. Keep core markup and accessibility. -->
  <xsl:template match="image[asymptote]" mode="image-inclusion" priority="10">
    <xsl:variable name="rendered"><xsl:apply-imports/></xsl:variable>
    <xsl:apply-templates select="exsl:node-set($rendered)/node()" mode="defer-asymptote"/>
  </xsl:template>
  <xsl:template match="@*|node()" mode="defer-asymptote">
    <xsl:copy><xsl:apply-templates select="@*|node()" mode="defer-asymptote"/></xsl:copy>
  </xsl:template>
  <xsl:template match="iframe[@class='asymptote']" mode="defer-asymptote">
    <xsl:copy>
      <xsl:copy-of select="@*"/>
      <xsl:attribute name="loading">lazy</xsl:attribute>
      <xsl:apply-templates select="node()" mode="defer-asymptote"/>
    </xsl:copy>
  </xsl:template>
</xsl:stylesheet>
