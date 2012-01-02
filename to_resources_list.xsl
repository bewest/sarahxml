<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet
  version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <!-- match root level, first generally -->
  <xsl:template match="/">
    <!-- create our new xml outline here -->
    <resources>
      <string-array name="pcms_list">
        <!-- find all checked elements, and apply any templates that match them
         -->
        <xsl:apply-templates select=".//checked" />
      </string-array>
    </resources>
  </xsl:template>

  <!-- this template transforms all elements called "checked" into an element
       called "item" with the same node value -->
  <xsl:template match="checked">
    <item><xsl:value-of select="."/></item>
  </xsl:template>

</xsl:stylesheet>

<!--
EOF -->
