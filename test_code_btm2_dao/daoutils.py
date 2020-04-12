def createSqlQuery(tableName, listOfUserDetailsDict, listOfColumns):

    query = "INSERT INTO {} (".format(tableName.strip()) + listOfColumns[0] + ', ' + listOfColumns[1] + ', ' + listOfColumns[2] + ') VALUES ( %s, %s, %s)'

    listOfValues = []
    for userDetailsDict in listOfUserDetailsDict:
        if userDetailsDict is not None:

            if userDetailsDict[listOfColumns[0]] is not None:
                CarColor = userDetailsDict[listOfColumns[0]]

            if userDetailsDict[listOfColumns[1]] is not None:
                CarPrice = userDetailsDict[listOfColumns[1]]

            if userDetailsDict[listOfColumns[2]] is not None:
                CarModel = userDetailsDict[listOfColumns[2]]

        listOfValues.append((CarColor, CarPrice, CarModel,))

    return query, listOfValues

