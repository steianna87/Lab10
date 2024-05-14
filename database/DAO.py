from database.DB_connect import DBConnect
from model.contiguity import Contiguity
from model.country import Country


class DAO():
    def __init__(self):
        pass
    @staticmethod
    def getAllCountry():
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = 'select * from country'

        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getContiguity(year):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = ''' select *
                    from countries.contiguity c 
                    where c.`year` <= %s'''

        cursor.execute(query, (year, ))
        result = []
        for row in cursor:
            result.append(Contiguity(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllCountry_by_year(year):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """ select distinct c.StateAbb , c.CCode , c.StateNme 
                    from countries.country c, countries.contiguity ct
                    where ct.`year` <= %s and (c.CCode = ct.state1no or c.CCode  = ct.state2no ) """

        cursor.execute(query, (year, ))
        result = []
        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        conn.close()
        return result
