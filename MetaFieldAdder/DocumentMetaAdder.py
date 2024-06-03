import os
import json

from typing import List
from haystack import Document, component, logging


@component
class DocumentMetaAdder:
    """
    This component adds meta fields to Documents in the indexing pipeline.
    The meta values are specified in a seperate json file.
    The name of the json file is the name of the Document the meta data is intended for, plus the ending ".meta.json".

    Example: The name of a pdf file is: "Information.pdf".
    Then, the name of the json file is "Information.pdf.meta.json".
    The MetaFieldAdder extracts the meta values from this json file and adds them to the Document.
    """

    def __init__(
        self
    ):
        """
        no arguments
        """
        pass

    @component.output_types(documents=List[Document])
    def run(self, documents: List[Document]):
        """
        It is recommended, to add the component between the FileTypeRouter and the DocumentSplitter.
        """

        for doc in documents:
            path = doc.meta["file_path"] + ".meta.json"

            if os.path.exists(path):
                with open(path, 'r') as file:
                    meta_data = json.load(file)
                doc.meta.update(meta_data)

        return {"documents": documents}
