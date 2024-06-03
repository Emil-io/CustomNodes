# This is a collection of Custom Nodes for Haystack

<details>
  <summary>MetaFieldAdder</summary>
  <h2>What does this component do?</h2>
  <p>This component adds meta fields to Documents in the indexing pipeline.
  
  The meta values are specified in a seperate json file. The name of the json file is the name of the Document the meta data is intended for, plus the ending ".meta.json".
  
  *Example: The name of a pdf file is: "Information.pdf". Then, the name of the json file is "Information.pdf.meta.json". The MetaFieldAdder extracts the meta values from this json file and adds them to the Document.*</p>
</details>
