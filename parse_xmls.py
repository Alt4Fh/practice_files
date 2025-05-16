import marimo

__generated_with = "0.13.6"
app = marimo.App(width="medium")


app._unparsable_cell(
    r"""
    from lxml import etree
    xml_data = '''
    <products>
      <product>
        <item id=\"product_name\">Dark Red Energy Potion</item>
        <item class=\"pricing\">
          <item>Price with discount: $4.99</item>
          <item>Price without discount: $11.99</item>
        </item>
        <item id=\"product_rate\" review_count=\"774\">4.7</item>
        <item id=\"product_description\">Bring out the best in your gaming performance.</item>
      </product>
    </products

    root = etree.fromstring(xml_data)
    """,
    name="_"
)


@app.cell
def _(root):
    for parent in root:
        print(f'Parent tag: {parent.tag}')
        for child in parent:
            print(f'Child tag: {child.tag}')
            for grandchild in child:
                print(f'Grand child tag: {grandchild.tag}')
    return


if __name__ == "__main__":
    app.run()
