import pandas as pd
import pickle
with open("alco2009.pickle","wb") as oFile:
    pickle.dump(alco2009,oFile)
alco2009=pd.read_csv("niaa-report2009.csv", index_col="State")

print(alco2009.max())
print(alco2009.min(axis=1))
print(alco2009.sum())

alco=pd.read_csv("niaaa-report.csv", index_col=["State","Year"])
multi = pd.MultiIndex.from_tuples((
("Alabama", 1977),
("Alabama", 1978), 
("Alabama", 1979), 
("Alabama", 1980), 
("Alabama", 1981), 
("Alabama", 1982), 
("Alabama", 1983), 
("Alabama", 1984), 
("Alabama", 1985), 
("Alabama", 1986), 
("Alabama", 1987), 
("Alabama", 1988), 
("Alabama", 1989), 
("Alabama", 1990), 
("Alabama", 1991), 
("Alabama", 1992), 
("Alabama", 1993), 
("Alabama", 1994), 
("Alabama", 1995), 
("Alabama", 1996), 
("Alabama", 1997), 
("Alabama", 1998), 
("Alabama", 1999), 
("Alabama", 2000), 
("Alabama", 2001), 
("Alabama", 2002), 
("Alabama", 2003), 
("Alabama", 2004), 
("Alabama", 2005), 
("Alabama", 2006), 
("Alabama", 2007), 
("Alabama", 2008), 
("Alabama", 2009), 
("Alaska", 1977), 
("Alaska", 1978), 
("Alaska", 1979), 
("Alaska", 1980), 
("Alaska", 1981), 
("Alaska", 1982), 
("Alaska", 1983), 
("Alaska", 1984), 
("Alaska", 1985), 
("Alaska", 1986), 
("Alaska", 1987), 
("Alaska", 1988), 
("Alaska", 1989), 
("Alaska", 1990), 
("Alaska", 1991), 
("Alaska", 1992), 
("Alaska", 1993), 
("Alaska", 1994), 
("Alaska", 1995), 
("Alaska", 1996), 
("Alaska", 1997), 
("Alaska", 1998), 
("Alaska", 1999), 
("Alaska", 2000), 
("Alaska", 2001), 
("Alaska", 2002), 
("Alaska", 2003), 
("Alaska", 2004), 
("Alaska", 2005), 
("Alaska", 2006), 
("Alaska", 2007), 
("Alaska", 2008), 
("Alaska", 2009), 
("Arizona", 1977),
("Arizona", 1978), 
("Arizona", 1979), 
("Arizona", 1980), 
("Arizona", 1981), 
("Arizona", 1982), 
("Arizona", 1983), 
("Arizona", 1984), 
("Arizona", 1985), 
("Arizona", 1986), 
("Arizona", 1987), 
("Arizona", 1988), 
("Arizona", 1989), 
("Arizona", 1990), 
("Arizona", 1991), 
("Arizona", 1992), 
("Arizona", 1993), 
("Arizona", 1994), 
("Arizona", 1995), 
("Arizona", 1996), 
("Arizona", 1997), 
("Arizona", 1998), 
("Arizona", 1999), 
("Arizona", 2000), 
("Arizona", 2001), 
("Arizona", 2002), 
("Arizona", 2003), 
("Arizona", 2004), 
("Arizona", 2005), 
("Arizona", 2006), 
("Arizona", 2007), 
("Arizona", 2008), 
("Arizona", 2009), 
("Arkansas", 1977), 
("Arkansas", 1978), 
("Arkansas", 1979), 
("Arkansas", 1980), 
("Arkansas", 1981), 
("Arkansas", 1982), 
("Arkansas", 1983), 
("Arkansas", 1984), 
("Arkansas", 1985), 
("Arkansas", 1986), 
("Arkansas", 1987), 
("Arkansas", 1988), 
("Arkansas", 1989), 
("Arkansas", 1990), 
("Arkansas", 1991), 
("Arkansas", 1992), 
("Arkansas", 1993), 
("Arkansas", 1994), 
("Arkansas", 1995), 
("Arkansas", 1996), 
("Arkansas", 1997), 
("Arkansas", 1998), 
("Arkansas", 1999), 
("Arkansas", 2000), 
("Arkansas", 2001), 
("Arkansas", 2002), 
("Arkansas", 2003), 
("Arkansas", 2004), 
("Arkansas", 2005), 
("Arkansas", 2006), 
("Arkansas", 2007), 
("Arkansas", 2008), 
("Arkansas", 2009), 
("California", 1977),
("California", 1978), 
("California", 1979), 
("California", 1980), 
("California", 1981), 
("California", 1982), 
("California", 1983), 
("California", 1984), 
("California", 1985), 
("California", 1986), 
("California", 1987), 
("California", 1988), 
("California", 1989), 
("California", 1990), 
("California", 1991), 
("California", 1992), 
("California", 1993), 
("California", 1994), 
("California", 1995), 
("California", 1996), 
("California", 1997), 
("California", 1998), 
("California", 1999), 
("California", 2000), 
("California", 2001), 
("California", 2002), 
("California", 2003), 
("California", 2004), 
("California", 2005), 
("California", 2006), 
("California", 2007), 
("California", 2008), 
("California", 2009), 
("Colorado", 1977), 
("Colorado", 1978), 
("Colorado", 1979), 
("Colorado", 1980), 
("Colorado", 1981), 
("Colorado", 1982), 
("Colorado", 1983), 
("Colorado", 1984), 
("Colorado", 1985), 
("Colorado", 1986), 
("Colorado", 1987), 
("Colorado", 1988), 
("Colorado", 1989), 
("Colorado", 1990), 
("Colorado", 1991), 
("Colorado", 1992), 
("Colorado", 1993), 
("Colorado", 1994), 
("Colorado", 1995), 
("Colorado", 1996), 
("Colorado", 1997), 
("Colorado", 1998), 
("Colorado", 1999), 
("Colorado", 2000), 
("Colorado", 2001), 
("Colorado", 2002), 
("Colorado", 2003), 
("Colorado", 2004), 
("Colorado", 2005), 
("Colorado", 2006), 
("Colorado", 2007), 
("Colorado", 2008), 
("Colorado", 2009), 
("Connecticut", 1977),
("Connecticut", 1978), 
("Connecticut", 1979), 
("Connecticut", 1980), 
("Connecticut", 1981), 
("Connecticut", 1982), 
("Connecticut", 1983), 
("Connecticut", 1984), 
("Connecticut", 1985), 
("Connecticut", 1986), 
("Connecticut", 1987), 
("Connecticut", 1988), 
("Connecticut", 1989), 
("Connecticut", 1990), 
("Connecticut", 1991), 
("Connecticut", 1992), 
("Connecticut", 1993), 
("Connecticut", 1994), 
("Connecticut", 1995), 
("Connecticut", 1996), 
("Connecticut", 1997), 
("Connecticut", 1998), 
("Connecticut", 1999), 
("Connecticut", 2000), 
("Connecticut", 2001), 
("Connecticut", 2002), 
("Connecticut", 2003), 
("Connecticut", 2004), 
("Connecticut", 2005), 
("Connecticut", 2006), 
("Connecticut", 2007), 
("Connecticut", 2008), 
("Connecticut", 2009), 
("Delaware", 1977), 
("Delaware", 1978), 
("Delaware", 1979), 
("Delaware", 1980), 
("Delaware", 1981), 
("Delaware", 1982), 
("Delaware", 1983), 
("Delaware", 1984), 
("Delaware", 1985), 
("Delaware", 1986), 
("Delaware", 1987), 
("Delaware", 1988), 
("Delaware", 1989), 
("Delaware", 1990), 
("Delaware", 1991), 
("Delaware", 1992), 
("Delaware", 1993), 
("Delaware", 1994), 
("Delaware", 1995), 
("Delaware", 1996), 
("Delaware", 1997), 
("Delaware", 1998), 
("Delaware", 1999), 
("Delaware", 2000), 
("Delaware", 2001), 
("Delaware", 2002), 
("Delaware", 2003), 
("Delaware", 2004), 
("Delaware", 2005), 
("Delaware", 2006), 
("Delaware", 2007), 
("Delaware", 2008), 
("Delaware", 2009), 
("District of Columbia", 1977),
("District of Columbia", 1978), 
("District of Columbia", 1979), 
("District of Columbia", 1980), 
("District of Columbia", 1981), 
("District of Columbia", 1982), 
("District of Columbia", 1983), 
("District of Columbia", 1984), 
("District of Columbia", 1985), 
("District of Columbia", 1986), 
("District of Columbia", 1987), 
("District of Columbia", 1988), 
("District of Columbia", 1989), 
("District of Columbia", 1990), 
("District of Columbia", 1991), 
("District of Columbia", 1992), 
("District of Columbia", 1993), 
("District of Columbia", 1994), 
("District of Columbia", 1995), 
("District of Columbia", 1996), 
("District of Columbia", 1997), 
("District of Columbia", 1998), 
("District of Columbia", 1999), 
("District of Columbia", 2000), 
("District of Columbia", 2001), 
("District of Columbia", 2002), 
("District of Columbia", 2003), 
("District of Columbia", 2004), 
("District of Columbia", 2005), 
("District of Columbia", 2006), 
("District of Columbia", 2007), 
("District of Columbia", 2008), 
("District of Columbia", 2009), 
("Florida", 1977), 
("Florida", 1978), 
("Florida", 1979), 
("Florida", 1980), 
("Florida", 1981), 
("Florida", 1982), 
("Florida", 1983), 
("Florida", 1984), 
("Florida", 1985), 
("Florida", 1986), 
("Florida", 1987), 
("Florida", 1988), 
("Florida", 1989), 
("Florida", 1990), 
("Florida", 1991), 
("Florida", 1992), 
("Florida", 1993), 
("Florida", 1994), 
("Florida", 1995), 
("Florida", 1996), 
("Florida", 1997), 
("Florida", 1998), 
("Florida", 1999), 
("Florida", 2000), 
("Florida", 2001), 
("Florida", 2002), 
("Florida", 2003), 
("Florida", 2004), 
("Florida", 2005), 
("Florida", 2006), 
("Florida", 2007), 
("Florida", 2008), 
("Florida", 2009), 
("Georgia", 1977),
("Georgia", 1978), 
("Georgia", 1979), 
("Georgia", 1980), 
("Georgia", 1981), 
("Georgia", 1982), 
("Georgia", 1983), 
("Georgia", 1984), 
("Georgia", 1985), 
("Georgia", 1986), 
("Georgia", 1987), 
("Georgia", 1988), 
("Georgia", 1989), 
("Georgia", 1990), 
("Georgia", 1991), 
("Georgia", 1992), 
("Georgia", 1993), 
("Georgia", 1994), 
("Georgia", 1995), 
("Georgia", 1996), 
("Georgia", 1997), 
("Georgia", 1998), 
("Georgia", 1999), 
("Georgia", 2000), 
("Georgia", 2001), 
("Georgia", 2002), 
("Georgia", 2003), 
("Georgia", 2004), 
("Georgia", 2005), 
("Georgia", 2006), 
("Georgia", 2007), 
("Georgia", 2008), 
("Georgia", 2009), 
("Hawaii", 1977), 
("Hawaii", 1978), 
("Hawaii", 1979), 
("Hawaii", 1980), 
("Hawaii", 1981), 
("Hawaii", 1982), 
("Hawaii", 1983), 
("Hawaii", 1984), 
("Hawaii", 1985), 
("Hawaii", 1986), 
("Hawaii", 1987), 
("Hawaii", 1988), 
("Hawaii", 1989), 
("Hawaii", 1990), 
("Hawaii", 1991), 
("Hawaii", 1992), 
("Hawaii", 1993), 
("Hawaii", 1994), 
("Hawaii", 1995), 
("Hawaii", 1996), 
("Hawaii", 1997), 
("Hawaii", 1998), 
("Hawaii", 1999), 
("Hawaii", 2000), 
("Hawaii", 2001), 
("Hawaii", 2002), 
("Hawaii", 2003), 
("Hawaii", 2004), 
("Hawaii", 2005), 
("Hawaii", 2006), 
("Hawaii", 2007), 
("Hawaii", 2008), 
("Hawaii", 2009), 
("Idaho", 1977),
("Idaho", 1978), 
("Idaho", 1979), 
("Idaho", 1980), 
("Idaho", 1981), 
("Idaho", 1982), 
("Idaho", 1983), 
("Idaho", 1984), 
("Idaho", 1985), 
("Idaho", 1986), 
("Idaho", 1987), 
("Idaho", 1988), 
("Idaho", 1989), 
("Idaho", 1990), 
("Idaho", 1991), 
("Idaho", 1992), 
("Idaho", 1993), 
("Idaho", 1994), 
("Idaho", 1995), 
("Idaho", 1996), 
("Idaho", 1997), 
("Idaho", 1998), 
("Idaho", 1999), 
("Idaho", 2000), 
("Idaho", 2001), 
("Idaho", 2002), 
("Idaho", 2003), 
("Idaho", 2004), 
("Idaho", 2005), 
("Idaho", 2006), 
("Idaho", 2007), 
("Idaho", 2008), 
("Idaho", 2009), 
("Illinois", 1977), 
("Illinois", 1978), 
("Illinois", 1979), 
("Illinois", 1980), 
("Illinois", 1981), 
("Illinois", 1982), 
("Illinois", 1983), 
("Illinois", 1984), 
("Illinois", 1985), 
("Illinois", 1986), 
("Illinois", 1987), 
("Illinois", 1988), 
("Illinois", 1989), 
("Illinois", 1990), 
("Illinois", 1991), 
("Illinois", 1992), 
("Illinois", 1993), 
("Illinois", 1994), 
("Illinois", 1995), 
("Illinois", 1996), 
("Illinois", 1997), 
("Illinois", 1998), 
("Illinois", 1999), 
("Illinois", 2000), 
("Illinois", 2001), 
("Illinois", 2002), 
("Illinois", 2003), 
("Illinois", 2004), 
("Illinois", 2005), 
("Illinois", 2006), 
("Illinois", 2007), 
("Illinois", 2008), 
("Illinois", 2009), 
("Indiana", 1977),
("Indiana", 1978), 
("Indiana", 1979), 
("Indiana", 1980), 
("Indiana", 1981), 
("Indiana", 1982), 
("Indiana", 1983), 
("Indiana", 1984), 
("Indiana", 1985), 
("Indiana", 1986), 
("Indiana", 1987), 
("Indiana", 1988), 
("Indiana", 1989), 
("Indiana", 1990), 
("Indiana", 1991), 
("Indiana", 1992), 
("Indiana", 1993), 
("Indiana", 1994), 
("Indiana", 1995), 
("Indiana", 1996), 
("Indiana", 1997), 
("Indiana", 1998), 
("Indiana", 1999), 
("Indiana", 2000), 
("Indiana", 2001), 
("Indiana", 2002), 
("Indiana", 2003), 
("Indiana", 2004), 
("Indiana", 2005), 
("Indiana", 2006), 
("Indiana", 2007), 
("Indiana", 2008), 
("Indiana", 2009), 
("Iowa", 1977), 
("Iowa", 1978), 
("Iowa", 1979), 
("Iowa", 1980), 
("Iowa", 1981), 
("Iowa", 1982), 
("Iowa", 1983), 
("Iowa", 1984), 
("Iowa", 1985), 
("Iowa", 1986), 
("Iowa", 1987), 
("Iowa", 1988), 
("Iowa", 1989), 
("Iowa", 1990), 
("Iowa", 1991), 
("Iowa", 1992), 
("Iowa", 1993), 
("Iowa", 1994), 
("Iowa", 1995), 
("Iowa", 1996), 
("Iowa", 1997), 
("Iowa", 1998), 
("Iowa", 1999), 
("Iowa", 2000), 
("Iowa", 2001), 
("Iowa", 2002), 
("Iowa", 2003), 
("Iowa", 2004), 
("Iowa", 2005), 
("Iowa", 2006), 
("Iowa", 2007), 
("Iowa", 2008), 
("Iowa", 2009), 
("Kansas", 1977),
("Kansas", 1978), 
("Kansas", 1979), 
("Kansas", 1980), 
("Kansas", 1981), 
("Kansas", 1982), 
("Kansas", 1983), 
("Kansas", 1984), 
("Kansas", 1985), 
("Kansas", 1986), 
("Kansas", 1987), 
("Kansas", 1988), 
("Kansas", 1989), 
("Kansas", 1990), 
("Kansas", 1991), 
("Kansas", 1992), 
("Kansas", 1993), 
("Kansas", 1994), 
("Kansas", 1995), 
("Kansas", 1996), 
("Kansas", 1997), 
("Kansas", 1998), 
("Kansas", 1999), 
("Kansas", 2000), 
("Kansas", 2001), 
("Kansas", 2002), 
("Kansas", 2003), 
("Kansas", 2004), 
("Kansas", 2005), 
("Kansas", 2006), 
("Kansas", 2007), 
("Kansas", 2008), 
("Kansas", 2009), 
("Kentucky", 1977), 
("Kentucky", 1978), 
("Kentucky", 1979), 
("Kentucky", 1980), 
("Kentucky", 1981), 
("Kentucky", 1982), 
("Kentucky", 1983), 
("Kentucky", 1984), 
("Kentucky", 1985), 
("Kentucky", 1986), 
("Kentucky", 1987), 
("Kentucky", 1988), 
("Kentucky", 1989), 
("Kentucky", 1990), 
("Kentucky", 1991), 
("Kentucky", 1992), 
("Kentucky", 1993), 
("Kentucky", 1994), 
("Kentucky", 1995), 
("Kentucky", 1996), 
("Kentucky", 1997), 
("Kentucky", 1998), 
("Kentucky", 1999), 
("Kentucky", 2000), 
("Kentucky", 2001), 
("Kentucky", 2002), 
("Kentucky", 2003), 
("Kentucky", 2004), 
("Kentucky", 2005), 
("Kentucky", 2006), 
("Kentucky", 2007), 
("Kentucky", 2008), 
("Kentucky", 2009), 
("Louisiana", 1977),
("Louisiana", 1978), 
("Louisiana", 1979), 
("Louisiana", 1980), 
("Louisiana", 1981), 
("Louisiana", 1982), 
("Louisiana", 1983), 
("Louisiana", 1984), 
("Louisiana", 1985), 
("Louisiana", 1986), 
("Louisiana", 1987), 
("Louisiana", 1988), 
("Louisiana", 1989), 
("Louisiana", 1990), 
("Louisiana", 1991), 
("Louisiana", 1992), 
("Louisiana", 1993), 
("Louisiana", 1994), 
("Louisiana", 1995), 
("Louisiana", 1996), 
("Louisiana", 1997), 
("Louisiana", 1998), 
("Louisiana", 1999), 
("Louisiana", 2000), 
("Louisiana", 2001), 
("Louisiana", 2002), 
("Louisiana", 2003), 
("Louisiana", 2004), 
("Louisiana", 2005), 
("Louisiana", 2006), 
("Louisiana", 2007), 
("Louisiana", 2008), 
("Louisiana", 2009), 
("Maine", 1977), 
("Maine", 1978), 
("Maine", 1979), 
("Maine", 1980), 
("Maine", 1981), 
("Maine", 1982), 
("Maine", 1983), 
("Maine", 1984), 
("Maine", 1985), 
("Maine", 1986), 
("Maine", 1987), 
("Maine", 1988), 
("Maine", 1989), 
("Maine", 1990), 
("Maine", 1991), 
("Maine", 1992), 
("Maine", 1993), 
("Maine", 1994), 
("Maine", 1995), 
("Maine", 1996), 
("Maine", 1997), 
("Maine", 1998), 
("Maine", 1999), 
("Maine", 2000), 
("Maine", 2001), 
("Maine", 2002), 
("Maine", 2003), 
("Maine", 2004), 
("Maine", 2005), 
("Maine", 2006), 
("Maine", 2007), 
("Maine", 2008), 
("Maine", 2009), 
("Maryland", 1977),
("Maryland", 1978), 
("Maryland", 1979), 
("Maryland", 1980), 
("Maryland", 1981), 
("Maryland", 1982), 
("Maryland", 1983), 
("Maryland", 1984), 
("Maryland", 1985), 
("Maryland", 1986), 
("Maryland", 1987), 
("Maryland", 1988), 
("Maryland", 1989), 
("Maryland", 1990), 
("Maryland", 1991), 
("Maryland", 1992), 
("Maryland", 1993), 
("Maryland", 1994), 
("Maryland", 1995), 
("Maryland", 1996), 
("Maryland", 1997), 
("Maryland", 1998), 
("Maryland", 1999), 
("Maryland", 2000), 
("Maryland", 2001), 
("Maryland", 2002), 
("Maryland", 2003), 
("Maryland", 2004), 
("Maryland", 2005), 
("Maryland", 2006), 
("Maryland", 2007), 
("Maryland", 2008), 
("Maryland", 2009), 
("Massachusetts", 1977), 
("Massachusetts", 1978), 
("Massachusetts", 1979), 
("Massachusetts", 1980), 
("Massachusetts", 1981), 
("Massachusetts", 1982), 
("Massachusetts", 1983), 
("Massachusetts", 1984), 
("Massachusetts", 1985), 
("Massachusetts", 1986), 
("Massachusetts", 1987), 
("Massachusetts", 1988), 
("Massachusetts", 1989), 
("Massachusetts", 1990), 
("Massachusetts", 1991), 
("Massachusetts", 1992), 
("Massachusetts", 1993), 
("Massachusetts", 1994), 
("Massachusetts", 1995), 
("Massachusetts", 1996), 
("Massachusetts", 1997), 
("Massachusetts", 1998), 
("Massachusetts", 1999), 
("Massachusetts", 2000), 
("Massachusetts", 2001), 
("Massachusetts", 2002), 
("Massachusetts", 2003), 
("Massachusetts", 2004), 
("Massachusetts", 2005), 
("Massachusetts", 2006), 
("Massachusetts", 2007), 
("Massachusetts", 2008), 
("Massachusetts", 2009), 
("Michigan", 1977),
("Michigan", 1978), 
("Michigan", 1979), 
("Michigan", 1980), 
("Michigan", 1981), 
("Michigan", 1982), 
("Michigan", 1983), 
("Michigan", 1984), 
("Michigan", 1985), 
("Michigan", 1986), 
("Michigan", 1987), 
("Michigan", 1988), 
("Michigan", 1989), 
("Michigan", 1990), 
("Michigan", 1991), 
("Michigan", 1992), 
("Michigan", 1993), 
("Michigan", 1994), 
("Michigan", 1995), 
("Michigan", 1996), 
("Michigan", 1997), 
("Michigan", 1998), 
("Michigan", 1999), 
("Michigan", 2000), 
("Michigan", 2001), 
("Michigan", 2002), 
("Michigan", 2003), 
("Michigan", 2004), 
("Michigan", 2005), 
("Michigan", 2006), 
("Michigan", 2007), 
("Michigan", 2008), 
("Michigan", 2009), 
("Minnesota", 1977), 
("Minnesota", 1978), 
("Minnesota", 1979), 
("Minnesota", 1980), 
("Minnesota", 1981), 
("Minnesota", 1982), 
("Minnesota", 1983), 
("Minnesota", 1984), 
("Minnesota", 1985), 
("Minnesota", 1986), 
("Minnesota", 1987), 
("Minnesota", 1988), 
("Minnesota", 1989), 
("Minnesota", 1990), 
("Minnesota", 1991), 
("Minnesota", 1992), 
("Minnesota", 1993), 
("Minnesota", 1994), 
("Minnesota", 1995), 
("Minnesota", 1996), 
("Minnesota", 1997), 
("Minnesota", 1998), 
("Minnesota", 1999), 
("Minnesota", 2000), 
("Minnesota", 2001), 
("Minnesota", 2002), 
("Minnesota", 2003), 
("Minnesota", 2004), 
("Minnesota", 2005), 
("Minnesota", 2006), 
("Minnesota", 2007), 
("Minnesota", 2008), 
("Minnesota", 2009), 
("Mississippi", 1977),
("Mississippi", 1978), 
("Mississippi", 1979), 
("Mississippi", 1980), 
("Mississippi", 1981), 
("Mississippi", 1982), 
("Mississippi", 1983), 
("Mississippi", 1984), 
("Mississippi", 1985), 
("Mississippi", 1986), 
("Mississippi", 1987), 
("Mississippi", 1988), 
("Mississippi", 1989), 
("Mississippi", 1990), 
("Mississippi", 1991), 
("Mississippi", 1992), 
("Mississippi", 1993), 
("Mississippi", 1994), 
("Mississippi", 1995), 
("Mississippi", 1996), 
("Mississippi", 1997), 
("Mississippi", 1998), 
("Mississippi", 1999), 
("Mississippi", 2000), 
("Mississippi", 2001), 
("Mississippi", 2002), 
("Mississippi", 2003), 
("Mississippi", 2004), 
("Mississippi", 2005), 
("Mississippi", 2006), 
("Mississippi", 2007), 
("Mississippi", 2008), 
("Mississippi", 2009), 
("Missouri", 1977), 
("Missouri", 1978), 
("Missouri", 1979), 
("Missouri", 1980), 
("Missouri", 1981), 
("Missouri", 1982), 
("Missouri", 1983), 
("Missouri", 1984), 
("Missouri", 1985), 
("Missouri", 1986), 
("Missouri", 1987), 
("Missouri", 1988), 
("Missouri", 1989), 
("Missouri", 1990), 
("Missouri", 1991), 
("Missouri", 1992), 
("Missouri", 1993), 
("Missouri", 1994), 
("Missouri", 1995), 
("Missouri", 1996), 
("Missouri", 1997), 
("Missouri", 1998), 
("Missouri", 1999), 
("Missouri", 2000), 
("Missouri", 2001), 
("Missouri", 2002), 
("Missouri", 2003), 
("Missouri", 2004), 
("Missouri", 2005), 
("Missouri", 2006), 
("Missouri", 2007), 
("Missouri", 2008), 
("Missouri", 2009), 
("Montana", 1977),
("Montana", 1978), 
("Montana", 1979), 
("Montana", 1980), 
("Montana", 1981), 
("Montana", 1982), 
("Montana", 1983), 
("Montana", 1984), 
("Montana", 1985), 
("Montana", 1986), 
("Montana", 1987), 
("Montana", 1988), 
("Montana", 1989), 
("Montana", 1990), 
("Montana", 1991), 
("Montana", 1992), 
("Montana", 1993), 
("Montana", 1994), 
("Montana", 1995), 
("Montana", 1996), 
("Montana", 1997), 
("Montana", 1998), 
("Montana", 1999), 
("Montana", 2000), 
("Montana", 2001), 
("Montana", 2002), 
("Montana", 2003), 
("Montana", 2004), 
("Montana", 2005), 
("Montana", 2006), 
("Montana", 2007), 
("Montana", 2008), 
("Montana", 2009), 
("Nebraska", 1977), 
("Nebraska", 1978), 
("Nebraska", 1979), 
("Nebraska", 1980), 
("Nebraska", 1981), 
("Nebraska", 1982), 
("Nebraska", 1983), 
("Nebraska", 1984), 
("Nebraska", 1985), 
("Nebraska", 1986), 
("Nebraska", 1987), 
("Nebraska", 1988), 
("Nebraska", 1989), 
("Nebraska", 1990), 
("Nebraska", 1991), 
("Nebraska", 1992), 
("Nebraska", 1993), 
("Nebraska", 1994), 
("Nebraska", 1995), 
("Nebraska", 1996), 
("Nebraska", 1997), 
("Nebraska", 1998), 
("Nebraska", 1999), 
("Nebraska", 2000), 
("Nebraska", 2001), 
("Nebraska", 2002), 
("Nebraska", 2003), 
("Nebraska", 2004), 
("Nebraska", 2005), 
("Nebraska", 2006), 
("Nebraska", 2007), 
("Nebraska", 2008), 
("Nebraska", 2009), 
("Nevada", 1977),
("Nevada", 1978), 
("Nevada", 1979), 
("Nevada", 1980), 
("Nevada", 1981), 
("Nevada", 1982), 
("Nevada", 1983), 
("Nevada", 1984), 
("Nevada", 1985), 
("Nevada", 1986), 
("Nevada", 1987), 
("Nevada", 1988), 
("Nevada", 1989), 
("Nevada", 1990), 
("Nevada", 1991), 
("Nevada", 1992), 
("Nevada", 1993), 
("Nevada", 1994), 
("Nevada", 1995), 
("Nevada", 1996), 
("Nevada", 1997), 
("Nevada", 1998), 
("Nevada", 1999), 
("Nevada", 2000), 
("Nevada", 2001), 
("Nevada", 2002), 
("Nevada", 2003), 
("Nevada", 2004), 
("Nevada", 2005), 
("Nevada", 2006), 
("Nevada", 2007), 
("Nevada", 2008), 
("Nevada", 2009), 
("New Hampshire", 1977), 
("New Hampshire", 1978), 
("New Hampshire", 1979), 
("New Hampshire", 1980), 
("New Hampshire", 1981), 
("New Hampshire", 1982), 
("New Hampshire", 1983), 
("New Hampshire", 1984), 
("New Hampshire", 1985), 
("New Hampshire", 1986), 
("New Hampshire", 1987), 
("New Hampshire", 1988), 
("New Hampshire", 1989), 
("New Hampshire", 1990), 
("New Hampshire", 1991), 
("New Hampshire", 1992), 
("New Hampshire", 1993), 
("New Hampshire", 1994), 
("New Hampshire", 1995), 
("New Hampshire", 1996), 
("New Hampshire", 1997), 
("New Hampshire", 1998), 
("New Hampshire", 1999), 
("New Hampshire", 2000), 
("New Hampshire", 2001), 
("New Hampshire", 2002), 
("New Hampshire", 2003), 
("New Hampshire", 2004), 
("New Hampshire", 2005), 
("New Hampshire", 2006), 
("New Hampshire", 2007), 
("New Hampshire", 2008), 
("New Hampshire", 2009), 
("New Jersey", 1977),
("New Jersey", 1978), 
("New Jersey", 1979), 
("New Jersey", 1980), 
("New Jersey", 1981), 
("New Jersey", 1982), 
("New Jersey", 1983), 
("New Jersey", 1984), 
("New Jersey", 1985), 
("New Jersey", 1986), 
("New Jersey", 1987), 
("New Jersey", 1988), 
("New Jersey", 1989), 
("New Jersey", 1990), 
("New Jersey", 1991), 
("New Jersey", 1992), 
("New Jersey", 1993), 
("New Jersey", 1994), 
("New Jersey", 1995), 
("New Jersey", 1996), 
("New Jersey", 1997), 
("New Jersey", 1998), 
("New Jersey", 1999), 
("New Jersey", 2000), 
("New Jersey", 2001), 
("New Jersey", 2002), 
("New Jersey", 2003), 
("New Jersey", 2004), 
("New Jersey", 2005), 
("New Jersey", 2006), 
("New Jersey", 2007), 
("New Jersey", 2008), 
("New Jersey", 2009), 
("New Mexico", 1977), 
("New Mexico", 1978), 
("New Mexico", 1979), 
("New Mexico", 1980), 
("New Mexico", 1981), 
("New Mexico", 1982), 
("New Mexico", 1983), 
("New Mexico", 1984), 
("New Mexico", 1985), 
("New Mexico", 1986), 
("New Mexico", 1987), 
("New Mexico", 1988), 
("New Mexico", 1989), 
("New Mexico", 1990), 
("New Mexico", 1991), 
("New Mexico", 1992), 
("New Mexico", 1993), 
("New Mexico", 1994), 
("New Mexico", 1995), 
("New Mexico", 1996), 
("New Mexico", 1997), 
("New Mexico", 1998), 
("New Mexico", 1999), 
("New Mexico", 2000), 
("New Mexico", 2001), 
("New Mexico", 2002), 
("New Mexico", 2003), 
("New Mexico", 2004), 
("New Mexico", 2005), 
("New Mexico", 2006), 
("New Mexico", 2007), 
("New Mexico", 2008), 
("New Mexico", 2009), 
("New York", 1977),
("New York", 1978), 
("New York", 1979), 
("New York", 1980), 
("New York", 1981), 
("New York", 1982), 
("New York", 1983), 
("New York", 1984), 
("New York", 1985), 
("New York", 1986), 
("New York", 1987), 
("New York", 1988), 
("New York", 1989), 
("New York", 1990), 
("New York", 1991), 
("New York", 1992), 
("New York", 1993), 
("New York", 1994), 
("New York", 1995), 
("New York", 1996), 
("New York", 1997), 
("New York", 1998), 
("New York", 1999), 
("New York", 2000), 
("New York", 2001), 
("New York", 2002), 
("New York", 2003), 
("New York", 2004), 
("New York", 2005), 
("New York", 2006), 
("New York", 2007), 
("New York", 2008), 
("New York", 2009), 
("North Carolina", 1977), 
("North Carolina", 1978), 
("North Carolina", 1979), 
("North Carolina", 1980), 
("North Carolina", 1981), 
("North Carolina", 1982), 
("North Carolina", 1983), 
("North Carolina", 1984), 
("North Carolina", 1985), 
("North Carolina", 1986), 
("North Carolina", 1987), 
("North Carolina", 1988), 
("North Carolina", 1989), 
("North Carolina", 1990), 
("North Carolina", 1991), 
("North Carolina", 1992), 
("North Carolina", 1993), 
("North Carolina", 1994), 
("North Carolina", 1995), 
("North Carolina", 1996), 
("North Carolina", 1997), 
("North Carolina", 1998), 
("North Carolina", 1999), 
("North Carolina", 2000), 
("North Carolina", 2001), 
("North Carolina", 2002), 
("North Carolina", 2003), 
("North Carolina", 2004), 
("North Carolina", 2005), 
("North Carolina", 2006), 
("North Carolina", 2007), 
("North Carolina", 2008), 
("North Carolina", 2009), 
("North Dakota", 1977),
("North Dakota", 1978), 
("North Dakota", 1979), 
("North Dakota", 1980), 
("North Dakota", 1981), 
("North Dakota", 1982), 
("North Dakota", 1983), 
("North Dakota", 1984), 
("North Dakota", 1985), 
("North Dakota", 1986), 
("North Dakota", 1987), 
("North Dakota", 1988), 
("North Dakota", 1989), 
("North Dakota", 1990), 
("North Dakota", 1991), 
("North Dakota", 1992), 
("North Dakota", 1993), 
("North Dakota", 1994), 
("North Dakota", 1995), 
("North Dakota", 1996), 
("North Dakota", 1997), 
("North Dakota", 1998), 
("North Dakota", 1999), 
("North Dakota", 2000), 
("North Dakota", 2001), 
("North Dakota", 2002), 
("North Dakota", 2003), 
("North Dakota", 2004), 
("North Dakota", 2005), 
("North Dakota", 2006), 
("North Dakota", 2007), 
("North Dakota", 2008), 
("North Dakota", 2009), 
("Ohio", 1977), 
("Ohio", 1978), 
("Ohio", 1979), 
("Ohio", 1980), 
("Ohio", 1981), 
("Ohio", 1982), 
("Ohio", 1983), 
("Ohio", 1984), 
("Ohio", 1985), 
("Ohio", 1986), 
("Ohio", 1987), 
("Ohio", 1988), 
("Ohio", 1989), 
("Ohio", 1990), 
("Ohio", 1991), 
("Ohio", 1992), 
("Ohio", 1993), 
("Ohio", 1994), 
("Ohio", 1995), 
("Ohio", 1996), 
("Ohio", 1997), 
("Ohio", 1998), 
("Ohio", 1999), 
("Ohio", 2000), 
("Ohio", 2001), 
("Ohio", 2002), 
("Ohio", 2003), 
("Ohio", 2004), 
("Ohio", 2005), 
("Ohio", 2006), 
("Ohio", 2007), 
("Ohio", 2008), 
("Ohio", 2009), 
("Oklahoma", 1977),
("Oklahoma", 1978), 
("Oklahoma", 1979), 
("Oklahoma", 1980), 
("Oklahoma", 1981), 
("Oklahoma", 1982), 
("Oklahoma", 1983), 
("Oklahoma", 1984), 
("Oklahoma", 1985), 
("Oklahoma", 1986), 
("Oklahoma", 1987), 
("Oklahoma", 1988), 
("Oklahoma", 1989), 
("Oklahoma", 1990), 
("Oklahoma", 1991), 
("Oklahoma", 1992), 
("Oklahoma", 1993), 
("Oklahoma", 1994), 
("Oklahoma", 1995), 
("Oklahoma", 1996), 
("Oklahoma", 1997), 
("Oklahoma", 1998), 
("Oklahoma", 1999), 
("Oklahoma", 2000), 
("Oklahoma", 2001), 
("Oklahoma", 2002), 
("Oklahoma", 2003), 
("Oklahoma", 2004), 
("Oklahoma", 2005), 
("Oklahoma", 2006), 
("Oklahoma", 2007), 
("Oklahoma", 2008), 
("Oklahoma", 2009), 
("Oregon", 1977), 
("Oregon", 1978), 
("Oregon", 1979), 
("Oregon", 1980), 
("Oregon", 1981), 
("Oregon", 1982), 
("Oregon", 1983), 
("Oregon", 1984), 
("Oregon", 1985), 
("Oregon", 1986), 
("Oregon", 1987), 
("Oregon", 1988), 
("Oregon", 1989), 
("Oregon", 1990), 
("Oregon", 1991), 
("Oregon", 1992), 
("Oregon", 1993), 
("Oregon", 1994), 
("Oregon", 1995), 
("Oregon", 1996), 
("Oregon", 1997), 
("Oregon", 1998), 
("Oregon", 1999), 
("Oregon", 2000), 
("Oregon", 2001), 
("Oregon", 2002), 
("Oregon", 2003), 
("Oregon", 2004), 
("Oregon", 2005), 
("Oregon", 2006), 
("Oregon", 2007), 
("Oregon", 2008), 
("Oregon", 2009), 
("Pennsylvania", 1977),
("Pennsylvania", 1978), 
("Pennsylvania", 1979), 
("Pennsylvania", 1980), 
("Pennsylvania", 1981), 
("Pennsylvania", 1982), 
("Pennsylvania", 1983), 
("Pennsylvania", 1984), 
("Pennsylvania", 1985), 
("Pennsylvania", 1986), 
("Pennsylvania", 1987), 
("Pennsylvania", 1988), 
("Pennsylvania", 1989), 
("Pennsylvania", 1990), 
("Pennsylvania", 1991), 
("Pennsylvania", 1992), 
("Pennsylvania", 1993), 
("Pennsylvania", 1994), 
("Pennsylvania", 1995), 
("Pennsylvania", 1996), 
("Pennsylvania", 1997), 
("Pennsylvania", 1998), 
("Pennsylvania", 1999), 
("Pennsylvania", 2000), 
("Pennsylvania", 2001), 
("Pennsylvania", 2002), 
("Pennsylvania", 2003), 
("Pennsylvania", 2004), 
("Pennsylvania", 2005), 
("Pennsylvania", 2006), 
("Pennsylvania", 2007), 
("Pennsylvania", 2008), 
("Pennsylvania", 2009), 
("Rhode Island", 1977), 
("Rhode Island", 1978), 
("Rhode Island", 1979), 
("Rhode Island", 1980), 
("Rhode Island", 1981), 
("Rhode Island", 1982), 
("Rhode Island", 1983), 
("Rhode Island", 1984), 
("Rhode Island", 1985), 
("Rhode Island", 1986), 
("Rhode Island", 1987), 
("Rhode Island", 1988), 
("Rhode Island", 1989), 
("Rhode Island", 1990), 
("Rhode Island", 1991), 
("Rhode Island", 1992), 
("Rhode Island", 1993), 
("Rhode Island", 1994), 
("Rhode Island", 1995), 
("Rhode Island", 1996), 
("Rhode Island", 1997), 
("Rhode Island", 1998), 
("Rhode Island", 1999), 
("Rhode Island", 2000), 
("Rhode Island", 2001), 
("Rhode Island", 2002), 
("Rhode Island", 2003), 
("Rhode Island", 2004), 
("Rhode Island", 2005), 
("Rhode Island", 2006), 
("Rhode Island", 2007), 
("Rhode Island", 2008), 
("Rhode Island", 2009), 
("South Carolina", 1977),
("South Carolina", 1978), 
("South Carolina", 1979), 
("South Carolina", 1980), 
("South Carolina", 1981), 
("South Carolina", 1982), 
("South Carolina", 1983), 
("South Carolina", 1984), 
("South Carolina", 1985), 
("South Carolina", 1986), 
("South Carolina", 1987), 
("South Carolina", 1988), 
("South Carolina", 1989), 
("South Carolina", 1990), 
("South Carolina", 1991), 
("South Carolina", 1992), 
("South Carolina", 1993), 
("South Carolina", 1994), 
("South Carolina", 1995), 
("South Carolina", 1996), 
("South Carolina", 1997), 
("South Carolina", 1998), 
("South Carolina", 1999), 
("South Carolina", 2000), 
("South Carolina", 2001), 
("South Carolina", 2002), 
("South Carolina", 2003), 
("South Carolina", 2004), 
("South Carolina", 2005), 
("South Carolina", 2006), 
("South Carolina", 2007), 
("South Carolina", 2008), 
("South Carolina", 2009), 
("South Dakota", 1977), 
("South Dakota", 1978), 
("South Dakota", 1979), 
("South Dakota", 1980), 
("South Dakota", 1981), 
("South Dakota", 1982), 
("South Dakota", 1983), 
("South Dakota", 1984), 
("South Dakota", 1985), 
("South Dakota", 1986), 
("South Dakota", 1987), 
("South Dakota", 1988), 
("South Dakota", 1989), 
("South Dakota", 1990), 
("South Dakota", 1991), 
("South Dakota", 1992), 
("South Dakota", 1993), 
("South Dakota", 1994), 
("South Dakota", 1995), 
("South Dakota", 1996), 
("South Dakota", 1997), 
("South Dakota", 1998), 
("South Dakota", 1999), 
("South Dakota", 2000), 
("South Dakota", 2001), 
("South Dakota", 2002), 
("South Dakota", 2003), 
("South Dakota", 2004), 
("South Dakota", 2005), 
("South Dakota", 2006), 
("South Dakota", 2007), 
("South Dakota", 2008), 
("South Dakota", 2009), 
("Tennessee", 1977),
("Tennessee", 1978), 
("Tennessee", 1979), 
("Tennessee", 1980), 
("Tennessee", 1981), 
("Tennessee", 1982), 
("Tennessee", 1983), 
("Tennessee", 1984), 
("Tennessee", 1985), 
("Tennessee", 1986), 
("Tennessee", 1987), 
("Tennessee", 1988), 
("Tennessee", 1989), 
("Tennessee", 1990), 
("Tennessee", 1991), 
("Tennessee", 1992), 
("Tennessee", 1993), 
("Tennessee", 1994), 
("Tennessee", 1995), 
("Tennessee", 1996), 
("Tennessee", 1997), 
("Tennessee", 1998), 
("Tennessee", 1999), 
("Tennessee", 2000), 
("Tennessee", 2001), 
("Tennessee", 2002), 
("Tennessee", 2003), 
("Tennessee", 2004), 
("Tennessee", 2005), 
("Tennessee", 2006), 
("Tennessee", 2007), 
("Tennessee", 2008), 
("Tennessee", 2009), 
("Texas", 1977), 
("Texas", 1978), 
("Texas", 1979), 
("Texas", 1980), 
("Texas", 1981), 
("Texas", 1982), 
("Texas", 1983), 
("Texas", 1984), 
("Texas", 1985), 
("Texas", 1986), 
("Texas", 1987), 
("Texas", 1988), 
("Texas", 1989), 
("Texas", 1990), 
("Texas", 1991), 
("Texas", 1992), 
("Texas", 1993), 
("Texas", 1994), 
("Texas", 1995), 
("Texas", 1996), 
("Texas", 1997), 
("Texas", 1998), 
("Texas", 1999), 
("Texas", 2000), 
("Texas", 2001), 
("Texas", 2002), 
("Texas", 2003), 
("Texas", 2004), 
("Texas", 2005), 
("Texas", 2006), 
("Texas", 2007), 
("Texas", 2008), 
("Texas", 2009), 
("Utah", 1977),
("Utah", 1978), 
("Utah", 1979), 
("Utah", 1980), 
("Utah", 1981), 
("Utah", 1982), 
("Utah", 1983), 
("Utah", 1984), 
("Utah", 1985), 
("Utah", 1986), 
("Utah", 1987), 
("Utah", 1988), 
("Utah", 1989), 
("Utah", 1990), 
("Utah", 1991), 
("Utah", 1992), 
("Utah", 1993), 
("Utah", 1994), 
("Utah", 1995), 
("Utah", 1996), 
("Utah", 1997), 
("Utah", 1998), 
("Utah", 1999), 
("Utah", 2000), 
("Utah", 2001), 
("Utah", 2002), 
("Utah", 2003), 
("Utah", 2004), 
("Utah", 2005), 
("Utah", 2006), 
("Utah", 2007), 
("Utah", 2008), 
("Utah", 2009), 
("Vermont", 1977), 
("Vermont", 1978), 
("Vermont", 1979), 
("Vermont", 1980), 
("Vermont", 1981), 
("Vermont", 1982), 
("Vermont", 1983), 
("Vermont", 1984), 
("Vermont", 1985), 
("Vermont", 1986), 
("Vermont", 1987), 
("Vermont", 1988), 
("Vermont", 1989), 
("Vermont", 1990), 
("Vermont", 1991), 
("Vermont", 1992), 
("Vermont", 1993), 
("Vermont", 1994), 
("Vermont", 1995), 
("Vermont", 1996), 
("Vermont", 1997), 
("Vermont", 1998), 
("Vermont", 1999), 
("Vermont", 2000), 
("Vermont", 2001), 
("Vermont", 2002), 
("Vermont", 2003), 
("Vermont", 2004), 
("Vermont", 2005), 
("Vermont", 2006), 
("Vermont", 2007), 
("Vermont", 2008), 
("Vermont", 2009), 
("Virginia", 1977),
("Virginia", 1978), 
("Virginia", 1979), 
("Virginia", 1980), 
("Virginia", 1981), 
("Virginia", 1982), 
("Virginia", 1983), 
("Virginia", 1984), 
("Virginia", 1985), 
("Virginia", 1986), 
("Virginia", 1987), 
("Virginia", 1988), 
("Virginia", 1989), 
("Virginia", 1990), 
("Virginia", 1991), 
("Virginia", 1992), 
("Virginia", 1993), 
("Virginia", 1994), 
("Virginia", 1995), 
("Virginia", 1996), 
("Virginia", 1997), 
("Virginia", 1998), 
("Virginia", 1999), 
("Virginia", 2000), 
("Virginia", 2001), 
("Virginia", 2002), 
("Virginia", 2003), 
("Virginia", 2004), 
("Virginia", 2005), 
("Virginia", 2006), 
("Virginia", 2007), 
("Virginia", 2008), 
("Virginia", 2009), 
("Washington", 1977), 
("Washington", 1978), 
("Washington", 1979), 
("Washington", 1980), 
("Washington", 1981), 
("Washington", 1982), 
("Washington", 1983), 
("Washington", 1984), 
("Washington", 1985), 
("Washington", 1986), 
("Washington", 1987), 
("Washington", 1988), 
("Washington", 1989), 
("Washington", 1990), 
("Washington", 1991), 
("Washington", 1992), 
("Washington", 1993), 
("Washington", 1994), 
("Washington", 1995), 
("Washington", 1996), 
("Washington", 1997), 
("Washington", 1998), 
("Washington", 1999), 
("Washington", 2000), 
("Washington", 2001), 
("Washington", 2002), 
("Washington", 2003), 
("Washington", 2004), 
("Washington", 2005), 
("Washington", 2006), 
("Washington", 2007), 
("Washington", 2008), 
("Washington", 2009), 
("West Virginia", 1977),
("West Virginia", 1978), 
("West Virginia", 1979), 
("West Virginia", 1980), 
("West Virginia", 1981), 
("West Virginia", 1982), 
("West Virginia", 1983), 
("West Virginia", 1984), 
("West Virginia", 1985), 
("West Virginia", 1986), 
("West Virginia", 1987), 
("West Virginia", 1988), 
("West Virginia", 1989), 
("West Virginia", 1990), 
("West Virginia", 1991), 
("West Virginia", 1992), 
("West Virginia", 1993), 
("West Virginia", 1994), 
("West Virginia", 1995), 
("West Virginia", 1996), 
("West Virginia", 1997), 
("West Virginia", 1998), 
("West Virginia", 1999), 
("West Virginia", 2000), 
("West Virginia", 2001), 
("West Virginia", 2002), 
("West Virginia", 2003), 
("West Virginia", 2004), 
("West Virginia", 2005), 
("West Virginia", 2006), 
("West Virginia", 2007), 
("West Virginia", 2008), 
("West Virginia", 2009), 
("Wisconsin", 1977), 
("Wisconsin", 1978), 
("Wisconsin", 1979), 
("Wisconsin", 1980), 
("Wisconsin", 1981), 
("Wisconsin", 1982), 
("Wisconsin", 1983), 
("Wisconsin", 1984), 
("Wisconsin", 1985), 
("Wisconsin", 1986), 
("Wisconsin", 1987), 
("Wisconsin", 1988), 
("Wisconsin", 1989), 
("Wisconsin", 1990), 
("Wisconsin", 1991), 
("Wisconsin", 1992), 
("Wisconsin", 1993), 
("Wisconsin", 1994), 
("Wisconsin", 1995), 
("Wisconsin", 1996), 
("Wisconsin", 1997), 
("Wisconsin", 1998), 
("Wisconsin", 1999), 
("Wisconsin", 2000), 
("Wisconsin", 2001), 
("Wisconsin", 2002), 
("Wisconsin", 2003), 
("Wisconsin", 2004), 
("Wisconsin", 2005), 
("Wisconsin", 2006), 
("Wisconsin", 2007), 
("Wisconsin", 2008), 
("Wisconsin", 2009), 
("Wyoming", 1977),
("Wyoming", 1978), 
("Wyoming", 1979), 
("Wyoming", 1980), 
("Wyoming", 1981), 
("Wyoming", 1982), 
("Wyoming", 1983), 
("Wyoming", 1984), 
("Wyoming", 1985), 
("Wyoming", 1986), 
("Wyoming", 1987), 
("Wyoming", 1988), 
("Wyoming", 1989), 
("Wyoming", 1990), 
("Wyoming", 1991), 
("Wyoming", 1992), 
("Wyoming", 1993), 
("Wyoming", 1994), 
("Wyoming", 1995), 
("Wyoming", 1996), 
("Wyoming", 1997), 
("Wyoming", 1998), 
("Wyoming", 1999), 
("Wyoming", 2000), 
("Wyoming", 2001), 
("Wyoming", 2002), 
("Wyoming", 2003), 
("Wyoming", 2004), 
("Wyoming", 2005), 
("Wyoming", 2006), 
("Wyoming", 2007), 
("Wyoming", 2008), 
("Wyoming", 2009)), 
names = ["State", "Year"])

alco.index=multi

alco["Total"]=alco.Wine+alco.Spirits+alco.Beer
print(alco.head())

cats=pd.cut(alco2009["Wine"],3).lables
print(cats)
wine_state=alco2009["Wine"]>alco2009["Wine"].mean()
beer_state=alco2009["Beer"]>alco2009["Beer"].mean()
pd.crosstab(wine_state,beer_state)
