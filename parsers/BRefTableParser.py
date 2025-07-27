def collectPropertiesForRow(tableRow):
    properties = {}
    rowDataItems = tableRow.find_all('td')
    for dataItem in rowDataItems:
        category = __determineColumnCategory(dataItem)
        value = __determineColumnValue(dataItem)
        if category is not None and value is not None:
            properties[category] = value
            if category == 'name_display':
                properties['data-append-csv'] = dataItem.attrs['data-append-csv']

    return properties

def __determineColumnCategory(tableCell):
    if 'data-stat' in tableCell.attrs:
        return tableCell.attrs['data-stat']
    else:
        return None

def __determineColumnValue(tableCell):
    if tableCell.a is not None:
        return tableCell.a.string
    else:
        return tableCell.string

def isNotTableHeaderRow(tableRow):
    if 'class' in tableRow.attrs:
        return 'thead' not in tableRow.attrs['class']
    return True