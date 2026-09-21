<?xml version="1.0" encoding="UTF-8"?>
<!-- Use PreTeXt's native accessible details/summary rendering for optional blocks.
     The CLI places its matching core stylesheets in ./core at build time. -->
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:import href="core/pretext-html.xsl"/>
  <xsl:template match="exercise[starts-with(normalize-space(title), 'Optional:')]|proof[starts-with(normalize-space(title), 'Optional:')]|paragraphs[starts-with(normalize-space(title), 'Optional:')]" mode="is-hidden" priority="10">
    <xsl:text>true</xsl:text>
  </xsl:template>
</xsl:stylesheet>
