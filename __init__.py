# -*- coding: utf-8 -*-

"""UUID generator extension.

Generates 1 or more version 4 UUID(s).

Synopsis: <trigger> [amount]"""

from albert import *
import os
import uuid

__title__ = "UUID Generator"
__version__ = "0.0.1"
__triggers__ = "uuid"
__authors__ = "peterdb"
__py_deps__ = ["uuid"]

iconPath = os.path.dirname(__file__)+"/uuid.svg"

def handleQuery(query):
    if not query.isTriggered:
        return

    amountToGenerate = 1
    try:
        amountToGenerate = int(query.string.strip())
    except:
        pass

    results = []

    generatedUuids = [str(uuid.uuid4()) for i in range(amountToGenerate)]

    # show max 5 uuids in the Item text
    summary = '\n'.join(generatedUuids[:5])
    if amountToGenerate > 5:
        summary = summary + "\n(" + str(amountToGenerate - 5) + " more...)"

    results.append(Item(
        id = __title__,
        icon = iconPath,
        text = summary,
        subtext = 'Copy the generated uuid(s) to the clipboard',
        actions = [ClipAction("Copy uuid(s) to clipboard", '\n'.join(generatedUuids))]
    ))


    return results