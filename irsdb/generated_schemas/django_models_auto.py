from django.db import models

#######
#
# IRS990 -  Part 0 Prefatory material 
#
#######

class part_0(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    PrncplOfcrBsnssNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: F  Description:  Business name line 1  most recent xpath: /IRS990/PrincipalOfcrBusinessName/BusinessNameLine1Txt 

    FrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number: F  Description:  Postal code  most recent xpath: /IRS990/ForeignAddress/ForeignPostalCd 

    ApplctnPndngInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: B  Description: Indicates this return has an application pending  most recent xpath: /IRS990/ApplicationPendingInd 

    OfOrgnztnTrstInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: K  Description: Type of organization - trust  most recent xpath: /IRS990/TypeOfOrganizationTrustInd 

    OthrOrgnztnDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: K  Description: Type of organization - other description  most recent xpath: /IRS990/OtherOrganizationDsc 

    PrncplOfcrBsnssNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: F  Description:  Business name line 2  most recent xpath: /IRS990/PrincipalOfcrBusinessName/BusinessNameLine2Txt 

    AddrssChngInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: B  Description: Indicates this return has an address change  most recent xpath: /IRS990/AddressChangeInd 

    FrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: F  Description:  Address line 1  most recent xpath: /IRS990/ForeignAddress/AddressLine1Txt 

    NmChngInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: B  Description: Indicates this return has a name change  most recent xpath: /IRS990/NameChangeInd 

    GrpExmptnNm = models.TextField(null=True, blank=True)
    # Line number: H(c)  Description: Group exemption number  most recent xpath: /IRS990/GroupExemptionNum 

    OfOrgnztnCrpInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: K  Description: Type of organization - corporation  most recent xpath: /IRS990/TypeOfOrganizationCorpInd 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: F  Description:  State  most recent xpath: /IRS990/USAddress/StateAbbreviationCd 

    FrmtnYr = models.IntegerField(null=True, blank=True)
    # Line number: L  Description: Year of formation  most recent xpath: /IRS990/FormationYr 

    Orgnztn527Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: I  Description: Indicates a 527 organization  most recent xpath: /IRS990/Organization527Ind 

    GrpRtrnFrAffltsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: H(a)  Description: Group return for affiliates?  most recent xpath: /IRS990/GroupReturnForAffiliatesInd 

    FrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: F  Description:  Country  most recent xpath: /IRS990/ForeignAddress/CountryCd 

    DngBsnssAsNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: C  Description:  Business name line 1  most recent xpath: /IRS990/DoingBusinessAsName/BusinessNameLine1Txt 

    Orgnztn501cInd = models.TextField(null=True, blank=True)
    # Line number: I  Description: Indicates a 501(c) organization  most recent xpath: /IRS990/Organization501cInd 

    Orgnztn501cType = models.BigIntegerField(null=True, blank=True)
    # Line number: I  Description: Insert 501(c) no  most recent xpath: /IRS990/Organization501cInd/@organization501cTypeTxt 

    OfOrgnztnOthrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: K  Description: Type of organization - other  most recent xpath: /IRS990/TypeOfOrganizationOtherInd 

    FnlRtrnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: B  Description: Indicates this return is a terminated return  most recent xpath: /IRS990/FinalReturnInd 

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number: F  Description:  ZIP code  most recent xpath: /IRS990/USAddress/ZIPCd 

    LglDmclSttCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: M  Description: State of legal domicile  most recent xpath: /IRS990/LegalDomicileStateCd 

    GrssRcptsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: G  Description: Gross receipts  most recent xpath: /IRS990/GrossReceiptsAmt 

    FrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number: F  Description:  Province or state  most recent xpath: /IRS990/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: F  Description:  Address line 2  most recent xpath: /IRS990/ForeignAddress/AddressLine2Txt 

    DngBsnssAsNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: C  Description:  Business name line 2  most recent xpath: /IRS990/DoingBusinessAsName/BusinessNameLine2Txt 

    AmnddRtrnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: B  Description: Indicates this return is an amended return  most recent xpath: /IRS990/AmendedReturnInd 

    AllAffltsInclddInd = models.TextField(null=True, blank=True)
    # Line number: H(b)  Description: All affiliates included?  most recent xpath: /IRS990/AllAffiliatesIncludedInd 

    Orgnztn49471NtPFInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: I  Description: Indicates a 4947(a)(1) organization  most recent xpath: /IRS990/Organization4947a1NotPFInd 

    Orgnztn501c3Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: I  Description: Indicates a 501(c)(3) organization  most recent xpath: /IRS990/Organization501c3Ind 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number: F  Description:  City  most recent xpath: /IRS990/USAddress/CityNm 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: F  Description:  Address line 2  most recent xpath: /IRS990/USAddress/AddressLine2Txt 

    LglDmclCntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: M  Description: Country of legal domicile  most recent xpath: /IRS990/LegalDomicileCountryCd 

    OfOrgnztnAsscInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: K  Description: Type of organization - association  most recent xpath: /IRS990/TypeOfOrganizationAssocInd 

    WbstAddrssTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: J  Description: Web site  most recent xpath: /IRS990/WebsiteAddressTxt 

    IntlRtrnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: B  Description: Indicates this is an initial return  most recent xpath: /IRS990/InitialReturnInd 

    FrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number: F  Description:  City  most recent xpath: /IRS990/ForeignAddress/CityNm 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: F  Description:  Address line 1  most recent xpath: /IRS990/USAddress/AddressLine1Txt 

    PrncplOffcrNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number: F  Description: Name of principal officer - Person  most recent xpath: /IRS990/PrincipalOfficerNm 

#######
#
# IRS990 -  Part I Summary 
#
#######

class part_i(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    TtlEmplyCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 5  Description: total Number employees  most recent xpath: /IRS990/TotalEmployeeCnt 

    PYTtlPrfFndrsngExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 16a  Description: Total professional fundraising expense - prior year  most recent xpath: /IRS990/PYTotalProfFndrsngExpnsAmt 

    PYInvstmntIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 10  Description: Investment income - prior year  most recent xpath: /IRS990/PYInvestmentIncomeAmt 

    VtngMmbrsGvrnngBdyCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 3  Description: Number voting members governing body  most recent xpath: /IRS990/VotingMembersGoverningBodyCnt 

    CYPrgrmSrvcRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 9  Description: Program service revenue - current year  most recent xpath: /IRS990/CYProgramServiceRevenueAmt 

    CYBnftsPdTMmbrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 14  Description: Benefits paid to members - current year  most recent xpath: /IRS990/CYBenefitsPaidToMembersAmt 

    TtlAsstsBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 20  Description: Total Assets, BOY  most recent xpath: /IRS990/TotalAssetsBOYAmt 

    PYSlrsCmpEmpBnftPdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 15  Description: Salaries, etc - prior year  most recent xpath: /IRS990/PYSalariesCompEmpBnftPaidAmt 

    CYOthrExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 17  Description: Other expenses - current year  most recent xpath: /IRS990/CYOtherExpensesAmt 

    NtAsstsOrFndBlncsBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 22  Description: Net Assets or Fund Balances, BOY  most recent xpath: /IRS990/NetAssetsOrFundBalancesBOYAmt 

    CYTtlFndrsngExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 16b  Description: Total fundraising expense - current year  most recent xpath: /IRS990/CYTotalFundraisingExpenseAmt 

    PYOthrExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 17  Description: Other expenses - prior year  most recent xpath: /IRS990/PYOtherExpensesAmt 

    CYTtlExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 18  Description: Total Expenses - current year  most recent xpath: /IRS990/CYTotalExpensesAmt 

    VtngMmbrsIndpndntCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 4  Description: Number independent voting members  most recent xpath: /IRS990/VotingMembersIndependentCnt 

    TtlGrssUBIAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 7a  Description: Total gross UBI  most recent xpath: /IRS990/TotalGrossUBIAmt 

    TtlVlntrsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 6  Description: Total number volunteers  most recent xpath: /IRS990/TotalVolunteersCnt 

    TtlLbltsEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 21  Description: Total Liabilities, EOY  most recent xpath: /IRS990/TotalLiabilitiesEOYAmt 

    CYInvstmntIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 10  Description: Investment income - current year  most recent xpath: /IRS990/CYInvestmentIncomeAmt 

    PYBnftsPdTMmbrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 14  Description: Benefits paid to members - prior year  most recent xpath: /IRS990/PYBenefitsPaidToMembersAmt 

    PYTtlRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 12  Description: Total revenue - prior year  most recent xpath: /IRS990/PYTotalRevenueAmt 

    TtlLbltsBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 21  Description: Total Liabilities, BOY  most recent xpath: /IRS990/TotalLiabilitiesBOYAmt 

    NtAsstsOrFndBlncsEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 22  Description: Net Assets or Fund Balances, EOY  most recent xpath: /IRS990/NetAssetsOrFundBalancesEOYAmt 

    PYRvnsLssExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 19  Description: Revenues less expenses - prior year  most recent xpath: /IRS990/PYRevenuesLessExpensesAmt 

    CYCntrbtnsGrntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 8  Description: Contributions and grants - current year  most recent xpath: /IRS990/CYContributionsGrantsAmt 

    PYCntrbtnsGrntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 8  Description: Contributions and grants - prior year  most recent xpath: /IRS990/PYContributionsGrantsAmt 

    CYGrntsAndSmlrPdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 13  Description: Grants and similar amounts - current year  most recent xpath: /IRS990/CYGrantsAndSimilarPaidAmt 

    PYGrntsAndSmlrPdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 13  Description: Grants and similar amounts - prior year  most recent xpath: /IRS990/PYGrantsAndSimilarPaidAmt 

    CYRvnsLssExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 19  Description: Revenues less expenses - current year  most recent xpath: /IRS990/CYRevenuesLessExpensesAmt 

    CYTtlPrfFndrsngExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 16a  Description: Total professional fundraising expense - current year  most recent xpath: /IRS990/CYTotalProfFndrsngExpnsAmt 

    CYOthrRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 11  Description: Other revenue - current year  most recent xpath: /IRS990/CYOtherRevenueAmt 

    ActvtyOrMssnDsc = models.TextField(null=True, blank=True)
    # Line number: Part I Line 1  Description: Activity or mission description  most recent xpath: /IRS990/ActivityOrMissionDesc 

    TtlAsstsEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 20  Description: Total Assets, EOY  most recent xpath: /IRS990/TotalAssetsEOYAmt 

    CYTtlRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 12  Description: Total revenue - current year  most recent xpath: /IRS990/CYTotalRevenueAmt 

    PYPrgrmSrvcRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 9  Description: Program service revenue - prior year  most recent xpath: /IRS990/PYProgramServiceRevenueAmt 

    PYTtlExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 18  Description: Total Expenses - prior year  most recent xpath: /IRS990/PYTotalExpensesAmt 

    PYOthrRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 11  Description: Other revenue - prior year  most recent xpath: /IRS990/PYOtherRevenueAmt 

    CntrctTrmntnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 2  Description: Termination or contraction  most recent xpath: /IRS990/ContractTerminationInd 

    CYSlrsCmpEmpBnftPdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 15  Description: Salaries, etc - current year  most recent xpath: /IRS990/CYSalariesCompEmpBnftPaidAmt 

    NtUnrltdBsTxblIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 7b  Description: Net unrelated business taxable income  most recent xpath: /IRS990/NetUnrelatedBusTxblIncmAmt 

#######
#
# IRS990 -  Part III Program Service Accomplishments 
#
#######

class part_iii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    ActvtyCd = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Line 4a  Description: Activity code  most recent xpath: /IRS990/ActivityCd 

    TtlOthrPrgSrvcRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Line 4d  Description: Total of other program service revenue  most recent xpath: /IRS990/TotalOtherProgSrvcRevenueAmt 

    Dsc = models.TextField(null=True, blank=True)
    # Line number: Part III Line 4a  Description: Description  most recent xpath: /IRS990/Desc 

    PrgSrvcAccmActy3_ActvtyCd = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part III  Description:  Activity code  most recent xpath: /IRS990/ProgSrvcAccomActy3Grp/ActivityCd 

    PrgSrvcAccmActy2_Dsc = models.TextField(null=True, blank=True)
    # Line number:  Part III  Description:  Description  most recent xpath: /IRS990/ProgSrvcAccomActy2Grp/Desc 

    RvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Line 4a  Description: Revenue  most recent xpath: /IRS990/RevenueAmt 

    PrgSrvcAccmActy3_ExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part III  Description:  Expense  most recent xpath: /IRS990/ProgSrvcAccomActy3Grp/ExpenseAmt 

    InfInSkdOPrtIIIInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part III  Description: Schedule O contains a response to a question in Part III  most recent xpath: /IRS990/InfoInScheduleOPartIIIInd 

    PrgSrvcAccmActy3_RvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part III  Description:  Revenue  most recent xpath: /IRS990/ProgSrvcAccomActy3Grp/RevenueAmt 

    TtlOthrPrgSrvcExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Line 4d  Description: Total of other program service expense  most recent xpath: /IRS990/TotalOtherProgSrvcExpenseAmt 

    TtlOthrPrgSrvcGrntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Line 4d  Description: Total of other program service grants  most recent xpath: /IRS990/TotalOtherProgSrvcGrantAmt 

    PrgSrvcAccmActy2_ActvtyCd = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part III  Description:  Activity code  most recent xpath: /IRS990/ProgSrvcAccomActy2Grp/ActivityCd 

    PrgSrvcAccmActy2_RvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part III  Description:  Revenue  most recent xpath: /IRS990/ProgSrvcAccomActy2Grp/RevenueAmt 

    SgnfcntNwPrgrmSrvcInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part III Line 2  Description: Significant new program services?  most recent xpath: /IRS990/SignificantNewProgramSrvcInd 

    TtlPrgrmSrvcExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Line 4e  Description: Total program service expense  most recent xpath: /IRS990/TotalProgramServiceExpensesAmt 

    MssnDsc = models.TextField(null=True, blank=True)
    # Line number: Part III Line 1  Description: Mission description  most recent xpath: /IRS990/MissionDesc 

    PrgSrvcAccmActy2_GrntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part III  Description:  Grants  most recent xpath: /IRS990/ProgSrvcAccomActy2Grp/GrantAmt 

    PrgSrvcAccmActy2_ExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part III  Description:  Expense  most recent xpath: /IRS990/ProgSrvcAccomActy2Grp/ExpenseAmt 

    PrgSrvcAccmActy3_Dsc = models.TextField(null=True, blank=True)
    # Line number:  Part III  Description:  Description  most recent xpath: /IRS990/ProgSrvcAccomActy3Grp/Desc 

    SgnfcntChngInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part III Line 3  Description: Significant change?  most recent xpath: /IRS990/SignificantChangeInd 

    GrntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Line 4a  Description: Grants  most recent xpath: /IRS990/GrantAmt 

    ExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Line 4a  Description: Expense  most recent xpath: /IRS990/ExpenseAmt 

    PrgSrvcAccmActy3_GrntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part III  Description:  Grants  most recent xpath: /IRS990/ProgSrvcAccomActy3Grp/GrantAmt 

#######
#
# IRS990 -  Part IV Required Schedules 
#
#######

class part_iv(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    DnrAdvsdFndInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 6  Description: Donor advised funds?  most recent xpath: /IRS990/DonorAdvisedFundInd 

    TrnsctnWthCntrlEntInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 35b  Description: Payment from or engage in transaction with a controlled entity?  most recent xpath: /IRS990/TransactionWithControlEntInd 

    CllctnsOfArtInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 8  Description: Collections of art?  most recent xpath: /IRS990/CollectionsOfArtInd 

    SkdBRqrdInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 2  Description: Schedule B required?  most recent xpath: /IRS990/ScheduleBRequiredInd 

    FrgnOffcInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part IV Line 14a  Description: Foreign office?  most recent xpath: /IRS990/ForeignOfficeInd 

    FndrsngActvtsInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 18  Description: Fundraising activities?  most recent xpath: /IRS990/FundraisingActivitiesInd 

    DdctblNnCshCntrInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 29  Description: Deductible non-cash contributions?  most recent xpath: /IRS990/DeductibleNonCashContriInd 

    InvstTxExmptBndsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part IV Line 24b  Description: Investment income?  most recent xpath: /IRS990/InvestTaxExemptBondsInd 

    BsnssRlnWthOffcrEntInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 28c  Description: Officer, etc. of entity with business relationship?  most recent xpath: /IRS990/BusinessRlnWith35CtrlEntInd 

    RltdOrgnztnCtrlEntInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part IV Line 35a  Description: Related organization a controlled entity?  most recent xpath: /IRS990/RelatedOrganizationCtrlEntInd 

    BsnssRlnWthOrgMmInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 28a  Description: Business relationship with organization?  most recent xpath: /IRS990/BusinessRlnWithOrgMemInd 

    TrnsfrExmptNnChrtblRltdOrgInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 36  Description: Any transfers to exempt non-charitable org?  most recent xpath: /IRS990/TrnsfrExmptNonChrtblRltdOrgInd 

    SbjctTPrxyTxInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 5  Description: Subject to proxy tax?  most recent xpath: /IRS990/SubjectToProxyTaxInd 

    DscrbdInSctn501c3Ind = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 1  Description: Described in 501(c)(3)?  most recent xpath: /IRS990/DescribedInSection501c3Ind 

    LnOtstndngInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 26  Description: Loan to officer or DQP?  most recent xpath: /IRS990/LoanOutstandingInd 

    DsrgrddEnttyInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 33  Description: Disregarded entity?  most recent xpath: /IRS990/DisregardedEntityInd 

    LbbyngActvtsInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 4  Description: Lobbying activities?  most recent xpath: /IRS990/LobbyingActivitiesInd 

    TmpOrPrmnntEndwmntsInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 10  Description: Term or permanent endowments?  most recent xpath: /IRS990/DonorRstrOrQuasiEndowmentsInd 

    MrThn5000KTOrgInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 15  Description: More than $5000 to organizations Part IX, line 3?  most recent xpath: /IRS990/MoreThan5000KToOrgInd 

    CnsrvtnEsmntsInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 7  Description: Conservation easements?  most recent xpath: /IRS990/ConservationEasementsInd 

    MrThn5000KTIndvdlsInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 16  Description: More than $5000 to individuals Part IX, line 3?  most recent xpath: /IRS990/MoreThan5000KToIndividualsInd 

    AdtdFnnclStmtAttInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 20b  Description: Audited financial statement attached?  most recent xpath: /IRS990/AuditedFinancialStmtAttInd 

    OprtHsptlInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 20a  Description: Hospital?  most recent xpath: /IRS990/OperateHospitalInd 

    TrmntOprtnsInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 31  Description: Terminated?  most recent xpath: /IRS990/TerminateOperationsInd 

    FrgnActvtsInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 14b  Description: Foreign activities, etc?  most recent xpath: /IRS990/ForeignActivitiesInd 

    CrdtCnslngInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 9  Description: Credit counseling?  most recent xpath: /IRS990/CreditCounselingInd 

    RprtInvstmntsOthrScInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 11b  Description: Balance sheet investments - other securities amounts reported?  most recent xpath: /IRS990/ReportInvestmentsOtherSecInd 

    PrtlLqdtnInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 32  Description: Partial liquidation?  most recent xpath: /IRS990/PartialLiquidationInd 

    GrntsTIndvdlsInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 22  Description: Grants to individuals?  most recent xpath: /IRS990/GrantsToIndividualsInd 

    BsnssRlnWthOffcrEntInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 28c  Description: Officer, etc. of entity with business relationship?  most recent xpath: /IRS990/BusinessRlnWithOfficerEntInd 

    RltdEnttyInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 34  Description: Related entity?  most recent xpath: /IRS990/RelatedEntityInd 

    RprtOthrAsstsInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 11d  Description: Balance sheet other assets amounts reported?  most recent xpath: /IRS990/ReportOtherAssetsInd 

    BsnssRlnWthFmMmInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 28b  Description: Business relationship thru family member?  most recent xpath: /IRS990/BusinessRlnWithFamMemInd 

    GrntsTOrgnztnsInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 21  Description: Grants to organizations?  most recent xpath: /IRS990/GrantsToOrganizationsInd 

    TmpOrPrmnntEndwmntsInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 10  Description: Term or permanent endowments?  most recent xpath: /IRS990/TempOrPermanentEndowmentsInd 

    TxExmptBndsInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 24a  Description: Tax exempt bonds?  most recent xpath: /IRS990/TaxExemptBondsInd 

    GrntTRltdPrsnInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 27  Description: Grant to related person?  most recent xpath: /IRS990/GrantToRelatedPersonInd 

    PrfssnlFndrsngInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 17  Description: Professional fundraising?  most recent xpath: /IRS990/ProfessionalFundraisingInd 

    OnBhlfOfIssrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part IV Line 24d  Description: On behalf of issuer?  most recent xpath: /IRS990/OnBehalfOfIssuerInd 

    SkdORqrdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part IV Line 38  Description: Governing body and public disclosure explained in Schedule O?  most recent xpath: /IRS990/ScheduleORequiredInd 

    IndpndntAdtFnclStmtInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 12a  Description: Independent audited financial statements?  most recent xpath: /IRS990/IndependentAuditFinclStmtInd 

    PYExcssBnftTrnsInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 25b  Description: Prior excess benefit transaction?  most recent xpath: /IRS990/PYExcessBenefitTransInd 

    SchlOprtngInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 13  Description: School?  most recent xpath: /IRS990/SchoolOperatingInd 

    ActvtsCndctdPrtshpInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 37  Description: Activities conducted thru partnership?  most recent xpath: /IRS990/ActivitiesConductedPrtshpInd 

    EscrwAccntInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part IV Line 24c  Description: Escrow account?  most recent xpath: /IRS990/EscrowAccountInd 

    IncldFIN48FtntInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 11f  Description: Balance sheet footnote for liability under FIN 48?  most recent xpath: /IRS990/IncludeFIN48FootnoteInd 

    DdctblArtCntrbtnInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 30  Description: Deductible contributions of art, etc?  most recent xpath: /IRS990/DeductibleArtContributionInd 

    GmngActvtsInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 19  Description: Gaming?  most recent xpath: /IRS990/GamingActivitiesInd 

    RprtPrgrmRltdInvstInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 11c  Description: Balance sheet investments - program related amounts reported?  most recent xpath: /IRS990/ReportProgramRelatedInvstInd 

    CnsldtdAdtFnclStmtInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 12b  Description: Consolidated audited financial statement?  most recent xpath: /IRS990/ConsolidatedAuditFinclStmtInd 

    RprtOthrLbltsInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 11e  Description: Balance sheet other liabilities amounts reported?  most recent xpath: /IRS990/ReportOtherLiabilitiesInd 

    EnggdInExcssBnftTrnsInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 25a  Description: Excess benefit transaction?  most recent xpath: /IRS990/EngagedInExcessBenefitTransInd 

    PltclCmpgnActyInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 3  Description: Political activities?  most recent xpath: /IRS990/PoliticalCampaignActyInd 

    RprtLndBldngEqpmntInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 11a  Description: Balance sheet land, buildings, equipment amounts reported?  most recent xpath: /IRS990/ReportLandBuildingEquipmentInd 

    SkdJRqrdInd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 23  Description: Part VII, Lines 3, 4, or 5 = "Yes"?  most recent xpath: /IRS990/ScheduleJRequiredInd 

#######
#
# IRS990 -  Part V Other Filings 
#
#######

class part_v(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    LcnsdMrThnOnSttInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 13a  Description: Is the organization licensed to issue qualified health plans in more than one state?  most recent xpath: /IRS990/LicensedMoreThanOneStateInd 

    GrssRcptsFrPblcUsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part V Line 10b  Description: Gross receipts amount  most recent xpath: /IRS990/GrossReceiptsForPublicUseAmt 

    TxblPrtyNtfctnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 5b  Description: Taxable party notification?  most recent xpath: /IRS990/TaxablePartyNotificationInd 

    SbjTTxRmnrtnExPrchtPymtInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 15  Description: Subject to the section 4960 tax on remuneration or excess parachute payments?  most recent xpath: /IRS990/SubjToTaxRmnrtnExPrchtPymtInd 

    IRPDcmntCnt = models.IntegerField(null=True, blank=True)
    # Line number: Part V Line 1a  Description: Number forms transmitted with 1096  most recent xpath: /IRS990/IRPDocumentCnt 

    Frm990TFldInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 3b  Description: Form 990-T filed?  most recent xpath: /IRS990/Form990TFiledInd 

    InfInSkdOPrtVInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V  Description: Schedule O contains a response to a question in Part V  most recent xpath: /IRS990/InfoInScheduleOPartVInd 

    UnrltdBsIncmOvrLmtInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 3a  Description: Unrelated business income?  most recent xpath: /IRS990/UnrelatedBusIncmOverLimitInd 

    Frm720FldInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 14b  Description: Form 720 filed and taxes paid on indoor tanning services?  most recent xpath: /IRS990/Form720FiledInd 

    PrhbtdTxShltrTrnsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 5a  Description: Prohibited tax shelter transaction?  most recent xpath: /IRS990/ProhibitedTaxShelterTransInd 

    NnddctblCntrDsclInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 6b  Description: Non-deduct. disclosure?  most recent xpath: /IRS990/NondeductibleContriDisclInd 

    TxExmptIntrstAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part V Line 12b  Description: Amount of tax exempt interest  most recent xpath: /IRS990/TaxExemptInterestAmt 

    IRPDcmntW2GCnt = models.IntegerField(null=True, blank=True)
    # Line number: Part V Line 1b  Description: Number W-2Gs included in 1a  most recent xpath: /IRS990/IRPDocumentW2GCnt 

    ExcsTxSct4951Or4952Or4953Ind = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 17  Description: Did the trust, any disqualified person, or mine operator engage in any activities that would result in the imposition of an excise tax under section 4951, 4952 or 4953?  most recent xpath: /IRS990/ExcsTaxSect4951Or4952Or4953Ind 

    EmplymntTxRtrnsFldInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 2b  Description: Employment tax returns filed?  most recent xpath: /IRS990/EmploymentTaxReturnsFiledInd 

    MmbrsAndShrGrssIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part V Line 11a  Description: Gross income from members  most recent xpath: /IRS990/MembersAndShrGrossIncomeAmt 

    BckpWthldCmplncInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1c  Description: Compliance with backup witholding?  most recent xpath: /IRS990/BackupWthldComplianceInd 

    SbjctTExcsTxNtInvstIncInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 16  Description: Subject to the section 4968 excise tax on net investment income?  most recent xpath: /IRS990/SubjectToExcsTaxNetInvstIncInd 

    DAFExcssBsnssHldngsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 8  Description: Donor advised fund have excess business holdings?  most recent xpath: /IRS990/DAFExcessBusinessHoldingsInd 

    Frm1098CFldInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 7h  Description: Form 1098-C filed?  most recent xpath: /IRS990/Form1098CFiledInd 

    RsrvsMntndAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part V Line 13c  Description: Reserves maintained amount  most recent xpath: /IRS990/ReservesMaintainedAmt 

    QdPrQCntrDsclInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 7b  Description: Quid pro quo disclosure?  most recent xpath: /IRS990/QuidProQuoContriDisclInd 

    Frm8282PrprtyDspsdOfInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 7c  Description: Form 8282 property disposed of?  most recent xpath: /IRS990/Form8282PropertyDisposedOfInd 

    EmplyCnt = models.IntegerField(null=True, blank=True)
    # Line number: Part V Line 2a  Description: Number of employees  most recent xpath: /IRS990/EmployeeCnt 

    SttRqrdRsrvsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part V Line 13b  Description: State required reserves amount  most recent xpath: /IRS990/StateRequiredReservesAmt 

    Frm8886TFldInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 5c  Description: Form 8886-T filed?  most recent xpath: /IRS990/Form8886TFiledInd 

    DstrbtnTDnrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 9b  Description: Distribution to donor?  most recent xpath: /IRS990/DistributionToDonorInd 

    QdPrQCntrbtnsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 7a  Description: Quid pro quo contributions?  most recent xpath: /IRS990/QuidProQuoContributionsInd 

    OrgFldInLOfFrm1041Ind = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 12a  Description: Filed lieu 1041?  most recent xpath: /IRS990/OrgFiledInLieuOfForm1041Ind 

    Frm8899Fldnd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 7g  Description: Form 8899 filed?  most recent xpath: /IRS990/Form8899Filedind 

    RcvFndsTPyPrsnlBnftCntrctInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 7e  Description: Funds to pay premiums?  most recent xpath: /IRS990/RcvFndsToPayPrsnlBnftCntrctInd 

    PyPrmmsPrsnlBnftCntrctInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 7f  Description: Premiums paid?  most recent xpath: /IRS990/PayPremiumsPrsnlBnftCntrctInd 

    IndrTnnngSrvcsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 14a  Description: Payments received for indoor tanning services?  most recent xpath: /IRS990/IndoorTanningServicesInd 

    InttnFsAndCpCntrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part V Line 10a  Description: Initiation fees amount  most recent xpath: /IRS990/InitiationFeesAndCapContriAmt 

    FrgnFnnclAccntInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 4a  Description: Foreign financial account?  most recent xpath: /IRS990/ForeignFinancialAccountInd 

    NnddctblCntrbtnsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 6a  Description: Non-deductible contributions?  most recent xpath: /IRS990/NondeductibleContributionsInd 

    Frm8282FldCnt = models.IntegerField(null=True, blank=True)
    # Line number: Part V Line 7d  Description: Number of 8282s filed  most recent xpath: /IRS990/Form8282FiledCnt 

    OthrSrcsGrssIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part V Line 11b  Description: Gross income, other sources  most recent xpath: /IRS990/OtherSourcesGrossIncomeAmt 

    TxblDstrbtnsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 9a  Description: Taxable distributions?  most recent xpath: /IRS990/TaxableDistributionsInd 

#######
#
# IRS990 -  Part VI Governance 
#
#######

class part_vi(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    OthrWbstInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part VI Section C Line 18  Description: Other website  most recent xpath: /IRS990/OtherWebsiteInd 

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number: Part VI Section C Line 20  Description:  ZIP code  most recent xpath: /IRS990/BooksInCareOfDetail/USAddress/ZIPCd 

    FrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number: Part VI Section C Line 20  Description:  City  most recent xpath: /IRS990/BooksInCareOfDetail/ForeignAddress/CityNm 

    FrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number: Part VI Section C Line 20  Description:  Postal code  most recent xpath: /IRS990/BooksInCareOfDetail/ForeignAddress/ForeignPostalCd 

    FmlyOrBsnssRlnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section A Line 2  Description: Family or business relationship?  most recent xpath: /IRS990/FamilyOrBusinessRlnInd 

    CnflctOfIntrstPlcyInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section B Line 12a  Description: Conflict of interest policy?  most recent xpath: /IRS990/ConflictOfInterestPolicyInd 

    InvstmntInJntVntrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section B Line 16a  Description: Investment in joint venture?  most recent xpath: /IRS990/InvestmentInJointVentureInd 

    IndpndntVtngMmbrCnt = models.IntegerField(null=True, blank=True)
    # Line number: Part VI Section A Line 1b  Description: Number of independent voting members  most recent xpath: /IRS990/IndependentVotingMemberCnt 

    PlcsRfrncChptrsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section B Line 10b  Description: Policies reference chapters?  most recent xpath: /IRS990/PoliciesReferenceChaptersInd 

    LclChptrsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section B Line 10a  Description: Local chapters?  most recent xpath: /IRS990/LocalChaptersInd 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part VI Section C Line 20  Description:  State  most recent xpath: /IRS990/BooksInCareOfDetail/USAddress/StateAbbreviationCd 

    InfInSkdOPrtVIInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part VI  Description: Schedule O contains a response to a question in Part VI  most recent xpath: /IRS990/InfoInScheduleOPartVIInd 

    FrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part VI Section C Line 20  Description:  Country  most recent xpath: /IRS990/BooksInCareOfDetail/ForeignAddress/CountryCd 

    BsnssNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part VI Section C Line 20  Description:  Business name line 2  most recent xpath: /IRS990/BooksInCareOfDetail/BusinessName/BusinessNameLine2Txt 

    DlgtnOfMgmtDtsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section A Line 3  Description: Delegation of management duties?  most recent xpath: /IRS990/DelegationOfMgmtDutiesInd 

    BsnssNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part VI Section C Line 20  Description:  Business name line 1  most recent xpath: /IRS990/BooksInCareOfDetail/BusinessName/BusinessNameLine1Txt 

    MtrlDvrsnOrMssInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section A Line 5  Description: Material diversion or misuse?  most recent xpath: /IRS990/MaterialDiversionOrMisuseInd 

    ChngTOrgDcmntsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section A Line 4  Description: Changes to organizing docs?  most recent xpath: /IRS990/ChangeToOrgDocumentsInd 

    UpnRqstInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part VI Section C Line 18  Description: Upon request  most recent xpath: /IRS990/UponRequestInd 

    Frm990PrvddTGvrnBdyInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section B Line 11  Description: Form 990 provided to governing body?  most recent xpath: /IRS990/Form990ProvidedToGvrnBodyInd 

    CmpnstnPrcssOthrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section B Line 15b  Description: Compensation process other?  most recent xpath: /IRS990/CompensationProcessOtherInd 

    OwnWbstInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part VI Section C Line 18  Description: Own website  most recent xpath: /IRS990/OwnWebsiteInd 

    CmpnstnPrcssCEOInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section B Line 15a  Description: Compensation process CEO?  most recent xpath: /IRS990/CompensationProcessCEOInd 

    OthrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part VI Section C Line 18  Description: Other (Explain in Schedule O)  most recent xpath: /IRS990/OtherInd 

    AnnlDsclsrCvrdPrsnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section B Line 12b  Description: Annual disclosure by covered persons?  most recent xpath: /IRS990/AnnualDisclosureCoveredPrsnInd 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part VI Section C Line 20  Description:  Address line 1  most recent xpath: /IRS990/BooksInCareOfDetail/USAddress/AddressLine1Txt 

    FrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number: Part VI Section C Line 20  Description:  Province or state  most recent xpath: /IRS990/BooksInCareOfDetail/ForeignAddress/ProvinceOrStateNm 

    GvrnngBdyVtngMmbrsCnt = models.IntegerField(null=True, blank=True)
    # Line number: Part VI Section A Line 1a  Description: Number of voting governing body members  most recent xpath: /IRS990/GoverningBodyVotingMembersCnt 

    RglrMntrngEnfrcInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section B Line 12c  Description: Regular monitoring and enforcement?  most recent xpath: /IRS990/RegularMonitoringEnfrcInd 

    OffcrMlngAddrssInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section A Line 9  Description: Officer mailing address?  most recent xpath: /IRS990/OfficerMailingAddressInd 

    DcsnsSbjctTApprvInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section A Line 7b  Description: decisions subject to approval?  most recent xpath: /IRS990/DecisionsSubjectToApprovaInd 

    ElctnOfBrdMmbrsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section A Line 7a  Description: election of board members?  most recent xpath: /IRS990/ElectionOfBoardMembersInd 

    MntsOfCmmttsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section A Line 8b  Description: Minutes of committees?  most recent xpath: /IRS990/MinutesOfCommitteesInd 

    WrttnPlcyOrPrcdrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section B Line 16b  Description: Written policy or procedure?  most recent xpath: /IRS990/WrittenPolicyOrProcedureInd 

    FrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part VI Section C Line 20  Description:  Address line 2  most recent xpath: /IRS990/BooksInCareOfDetail/ForeignAddress/AddressLine2Txt 

    BksInCrOfDtl_PrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part VI Section C Line 20  Description:  Name - Person  most recent xpath: /IRS990/BooksInCareOfDetail/PersonNm 

    WhstlblwrPlcyInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section B Line 13  Description: Whistleblower policy?  most recent xpath: /IRS990/WhistleblowerPolicyInd 

    MntsOfGvrnngBdyInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section A Line 8a  Description: Minutes of governing body?  most recent xpath: /IRS990/MinutesOfGoverningBodyInd 

    BksInCrOfDtl_PhnNm = models.CharField(null=True, blank=True, max_length=10)
    # Line number: Part VI Section C Line 20  Description:  Telephone number  most recent xpath: /IRS990/BooksInCareOfDetail/PhoneNum 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number: Part VI Section C Line 20  Description:  City  most recent xpath: /IRS990/BooksInCareOfDetail/USAddress/CityNm 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part VI Section C Line 20  Description:  Address line 2  most recent xpath: /IRS990/BooksInCareOfDetail/USAddress/AddressLine2Txt 

    MmbrsOrStckhldrsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section A Line 6  Description: Members or stockholders?  most recent xpath: /IRS990/MembersOrStockholdersInd 

    FrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part VI Section C Line 20  Description:  Address line 1  most recent xpath: /IRS990/BooksInCareOfDetail/ForeignAddress/AddressLine1Txt 

    DcmntRtntnPlcyInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Section B Line 14  Description: Document retention policy?  most recent xpath: /IRS990/DocumentRetentionPolicyInd 

#######
#
# IRS990 -  Part VII Compensation 
#
#######

class part_vii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    TtlRprtblCmpFrmOrgAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VII Section A Line 1d D  Description: Total, column D  most recent xpath: /IRS990/TotalReportableCompFromOrgAmt 

    TtRprtblCmpRltdOrgAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VII Section A Line 1d E  Description: Total, column E  most recent xpath: /IRS990/TotReportableCompRltdOrgAmt 

    IndvRcvdGrtrThn100KCnt = models.IntegerField(null=True, blank=True)
    # Line number: Part VII Section A Line 2  Description: Number individuals greater than $100K  most recent xpath: /IRS990/IndivRcvdGreaterThan100KCnt 

    InfInSkdOPrtVIIInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part VII  Description: Schedule O contains a response to a question in Part VII  most recent xpath: /IRS990/InfoInScheduleOPartVIIInd 

    CntrctRcvdGrtrThn100KCnt = models.IntegerField(null=True, blank=True)
    # Line number: Part VII Section B Line 2  Description: Number of contractors greater than $100K  most recent xpath: /IRS990/CntrctRcvdGreaterThan100KCnt 

    TtlOthrCmpnstnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VII Section A Line 1d F  Description: Total, column F  most recent xpath: /IRS990/TotalOtherCompensationAmt 

    FrmrOfcrEmplysLstdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII Section A Line 3  Description: Formers listed in 1a?  most recent xpath: /IRS990/FormerOfcrEmployeesListedInd 

    NLstdPrsnsCmpnstdInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part VII Section A  Description: No listed persons compensated  most recent xpath: /IRS990/NoListedPersonsCompensatedInd 

    TtlCmpGrtrThn150KInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII Section A Line 4  Description: Line1a, total greater than $150K?  most recent xpath: /IRS990/TotalCompGreaterThan150KInd 

    CmpnstnFrmOthrSrcsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII Section A Line 5  Description: Compensation from other sources?  most recent xpath: /IRS990/CompensationFromOtherSrcsInd 

#######
#
# IRS990 -  Part VIII Revenue 
#
#######

class part_viii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    GnOrLss_OthrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (ii)  Description:  Other amount  most recent xpath: /IRS990/GainOrLossGrp/OtherAmt 

    LssCstOthBssSlsExpnss_ScrtsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (i)  Description:  Securities amount  most recent xpath: /IRS990/LessCostOthBasisSalesExpnssGrp/SecuritiesAmt 

    OthrRvnTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VIII Line 11e  Description: Other miscellaneous revenue total  most recent xpath: /IRS990/OtherRevenueTotalAmt 

    RyltsRvn_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  most recent xpath: /IRS990/RoyaltiesRevenueGrp/ExclusionAmt 

    NtIncmFrmGmng_TtlRvnClmnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  most recent xpath: /IRS990/NetIncomeFromGamingGrp/TotalRevenueColumnAmt 

    NtRntlIncmOrLss_TtlRvnClmnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  most recent xpath: /IRS990/NetRentalIncomeOrLossGrp/TotalRevenueColumnAmt 

    RyltsRvn_RltdOrExmptFncIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  most recent xpath: /IRS990/RoyaltiesRevenueGrp/RelatedOrExemptFuncIncomeAmt 

    NtIncmOrLss_TtlRvnClmnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  most recent xpath: /IRS990/NetIncomeOrLossGrp/TotalRevenueColumnAmt 

    TtlOthPrgrmSrvcRv_TtlRvnClmnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  most recent xpath: /IRS990/TotalOthProgramServiceRevGrp/TotalRevenueColumnAmt 

    NtRntlIncmOrLss_UnrltdBsnssRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  most recent xpath: /IRS990/NetRentalIncomeOrLossGrp/UnrelatedBusinessRevenueAmt 

    NtIncmOrLss_RltdOrExmptFncIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  most recent xpath: /IRS990/NetIncomeOrLossGrp/RelatedOrExemptFuncIncomeAmt 

    TtlOthPrgrmSrvcRv_UnrltdBsnssRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  most recent xpath: /IRS990/TotalOthProgramServiceRevGrp/UnrelatedBusinessRevenueAmt 

    IncmFrmInvstBndPrcds_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  most recent xpath: /IRS990/IncmFromInvestBondProceedsGrp/ExclusionAmt 

    InvstmntIncm_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  most recent xpath: /IRS990/InvestmentIncomeGrp/ExclusionAmt 

    FndrsngDrctExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VIII Line 8b  Description: Direct expenses  most recent xpath: /IRS990/FundraisingDirectExpensesAmt 

    CstOfGdsSldAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VIII Line 10b  Description: Less cost of goods sold  most recent xpath: /IRS990/CostOfGoodsSoldAmt 

    NtIncmFrmGmng_UnrltdBsnssRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  most recent xpath: /IRS990/NetIncomeFromGamingGrp/UnrelatedBusinessRevenueAmt 

    GrssAmntSlsAssts_ScrtsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (i)  Description:  Securities amount  most recent xpath: /IRS990/GrossAmountSalesAssetsGrp/SecuritiesAmt 

    InfInSkdOPrtVIIIInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part VIII  Description: Schedule O contains a response to a question in Part VIII  most recent xpath: /IRS990/InfoInScheduleOPartVIIIInd 

    TtlOthPrgrmSrvcRv_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  most recent xpath: /IRS990/TotalOthProgramServiceRevGrp/ExclusionAmt 

    MscRvn_RltdOrExmptFncIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  most recent xpath: /IRS990/MiscellaneousRevenueGrp/RelatedOrExemptFuncIncomeAmt 

    RntlIncmOrLss_RlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (i)  Description:  Real amount  most recent xpath: /IRS990/RentalIncomeOrLossGrp/RealAmt 

    InvstmntIncm_UnrltdBsnssRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  most recent xpath: /IRS990/InvestmentIncomeGrp/UnrelatedBusinessRevenueAmt 

    RntlIncmOrLss_PrsnlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (ii)  Description:  Amount  most recent xpath: /IRS990/RentalIncomeOrLossGrp/PersonalAmt 

    NtIncmFrmGmng_RltdOrExmptFncIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  most recent xpath: /IRS990/NetIncomeFromGamingGrp/RelatedOrExemptFuncIncomeAmt 

    AllOthrCntrbtnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VIII Line 1f  Description: All other contributions, gifts, grants, and similar amounts not included in above  most recent xpath: /IRS990/AllOtherContributionsAmt 

    TtlRvn_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  most recent xpath: /IRS990/TotalRevenueGrp/ExclusionAmt 

    MscRvn_TtlRvnClmnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  most recent xpath: /IRS990/MiscellaneousRevenueGrp/TotalRevenueColumnAmt 

    RltdOrgnztnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VIII Line 1d  Description: Related organizations  most recent xpath: /IRS990/RelatedOrganizationsAmt 

    GrssAmntSlsAssts_OthrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (ii)  Description:  Other amount  most recent xpath: /IRS990/GrossAmountSalesAssetsGrp/OtherAmt 

    GrssRnts_PrsnlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (ii)  Description:  Amount  most recent xpath: /IRS990/GrossRentsGrp/PersonalAmt 

    RyltsRvn_TtlRvnClmnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  most recent xpath: /IRS990/RoyaltiesRevenueGrp/TotalRevenueColumnAmt 

    MscRvn_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  most recent xpath: /IRS990/MiscellaneousRevenueGrp/ExclusionAmt 

    FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VIII Line 1c  Description: Fundraising events  most recent xpath: /IRS990/FundraisingAmt 

    GmngDrctExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VIII Line 9b  Description: Direct expenses  most recent xpath: /IRS990/GamingDirectExpensesAmt 

    IncmFrmInvstBndPrcds_TtlRvnClmnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  most recent xpath: /IRS990/IncmFromInvestBondProceedsGrp/TotalRevenueColumnAmt 

    NtIncmFrmFndrsngEvt_UnrltdBsnssRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  most recent xpath: /IRS990/NetIncmFromFundraisingEvtGrp/UnrelatedBusinessRevenueAmt 

    LssRntlExpnss_RlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (i)  Description:  Real amount  most recent xpath: /IRS990/LessRentalExpensesGrp/RealAmt 

    NtGnOrLssInvstmnts_RltdOrExmptFncIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  most recent xpath: /IRS990/NetGainOrLossInvestmentsGrp/RelatedOrExemptFuncIncomeAmt 

    FdrtdCmpgnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VIII Line 1a  Description: Federated campaigns  most recent xpath: /IRS990/FederatedCampaignsAmt 

    NtIncmFrmFndrsngEvt_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  most recent xpath: /IRS990/NetIncmFromFundraisingEvtGrp/ExclusionAmt 

    IncmFrmInvstBndPrcds_UnrltdBsnssRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  most recent xpath: /IRS990/IncmFromInvestBondProceedsGrp/UnrelatedBusinessRevenueAmt 

    LssRntlExpnss_PrsnlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (ii)  Description:  Amount  most recent xpath: /IRS990/LessRentalExpensesGrp/PersonalAmt 

    FndrsngGrssIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VIII Line 8a  Description: Gross income from fundraising events, Line 8a box  most recent xpath: /IRS990/FundraisingGrossIncomeAmt 

    CntrRptFndrsngEvntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VIII Line 8a  Description: Contributions reported from fundraising events on line 1c, Line 8a underline  most recent xpath: /IRS990/ContriRptFundraisingEventAmt 

    TtlRvn_TtlRvnClmnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  most recent xpath: /IRS990/TotalRevenueGrp/TotalRevenueColumnAmt 

    NtIncmOrLss_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  most recent xpath: /IRS990/NetIncomeOrLossGrp/ExclusionAmt 

    IncmFrmInvstBndPrcds_RltdOrExmptFncIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  most recent xpath: /IRS990/IncmFromInvestBondProceedsGrp/RelatedOrExemptFuncIncomeAmt 

    TtlRvn_UnrltdBsnssRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  most recent xpath: /IRS990/TotalRevenueGrp/UnrelatedBusinessRevenueAmt 

    TtlPrgrmSrvcRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VIII Line 2g  Description: Program service revenue total  most recent xpath: /IRS990/TotalProgramServiceRevenueAmt 

    NtIncmFrmGmng_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  most recent xpath: /IRS990/NetIncomeFromGamingGrp/ExclusionAmt 

    InvstmntIncm_TtlRvnClmnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  most recent xpath: /IRS990/InvestmentIncomeGrp/TotalRevenueColumnAmt 

    GmngGrssIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VIII Line 9a  Description: Gross income from gaming  most recent xpath: /IRS990/GamingGrossIncomeAmt 

    NtGnOrLssInvstmnts_UnrltdBsnssRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  most recent xpath: /IRS990/NetGainOrLossInvestmentsGrp/UnrelatedBusinessRevenueAmt 

    TtlRvn_RltdOrExmptFncIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  most recent xpath: /IRS990/TotalRevenueGrp/RelatedOrExemptFuncIncomeAmt 

    NtRntlIncmOrLss_RltdOrExmptFncIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  most recent xpath: /IRS990/NetRentalIncomeOrLossGrp/RelatedOrExemptFuncIncomeAmt 

    NtGnOrLssInvstmnts_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  most recent xpath: /IRS990/NetGainOrLossInvestmentsGrp/ExclusionAmt 

    TtlOthPrgrmSrvcRv_RltdOrExmptFncIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  most recent xpath: /IRS990/TotalOthProgramServiceRevGrp/RelatedOrExemptFuncIncomeAmt 

    RyltsRvn_UnrltdBsnssRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  most recent xpath: /IRS990/RoyaltiesRevenueGrp/UnrelatedBusinessRevenueAmt 

    GrssSlsOfInvntryAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VIII Line 10a  Description: Gross sales of inventory, less returns and allowances  most recent xpath: /IRS990/GrossSalesOfInventoryAmt 

    GnOrLss_ScrtsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (i)  Description:  Securities amount  most recent xpath: /IRS990/GainOrLossGrp/SecuritiesAmt 

    NtGnOrLssInvstmnts_TtlRvnClmnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  most recent xpath: /IRS990/NetGainOrLossInvestmentsGrp/TotalRevenueColumnAmt 

    TtlCntrbtnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VIII Line 1h Column (A)  Description: Total contributions  most recent xpath: /IRS990/TotalContributionsAmt 

    NtIncmOrLss_UnrltdBsnssRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  most recent xpath: /IRS990/NetIncomeOrLossGrp/UnrelatedBusinessRevenueAmt 

    NtRntlIncmOrLss_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  most recent xpath: /IRS990/NetRentalIncomeOrLossGrp/ExclusionAmt 

    NtIncmFrmFndrsngEvt_TtlRvnClmnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  most recent xpath: /IRS990/NetIncmFromFundraisingEvtGrp/TotalRevenueColumnAmt 

    GrssRnts_RlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (i)  Description:  Real amount  most recent xpath: /IRS990/GrossRentsGrp/RealAmt 

    GvrnmntGrntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VIII Line 1e  Description: Government grants (contributions)  most recent xpath: /IRS990/GovernmentGrantsAmt 

    MscRvn_UnrltdBsnssRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  most recent xpath: /IRS990/MiscellaneousRevenueGrp/UnrelatedBusinessRevenueAmt 

    MmbrshpDsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VIII Line 1b  Description: Outside fundraising or commercial co-ventures  most recent xpath: /IRS990/MembershipDuesAmt 

    NncshCntrbtnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VIII Line 1g  Description: Noncash contributions  most recent xpath: /IRS990/NoncashContributionsAmt 

    InvstmntIncm_RltdOrExmptFncIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  most recent xpath: /IRS990/InvestmentIncomeGrp/RelatedOrExemptFuncIncomeAmt 

    LssCstOthBssSlsExpnss_OthrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (ii)  Description:  Other amount  most recent xpath: /IRS990/LessCostOthBasisSalesExpnssGrp/OtherAmt 

#######
#
# IRS990 -  Part IX Functional Expense 
#
#######

class part_ix(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    OthrSlrsAndWgs_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/OtherSalariesAndWagesGrp/ProgramServicesAmt 

    DprctnDpltn_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/DepreciationDepletionGrp/FundraisingAmt 

    Rylts_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/RoyaltiesGrp/ProgramServicesAmt 

    CmpCrrntOfcrDrctrs_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/CompCurrentOfcrDirectorsGrp/ManagementAndGeneralAmt 

    InfrmtnTchnlgy_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/InformationTechnologyGrp/FundraisingAmt 

    Occpncy_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/OccupancyGrp/FundraisingAmt 

    BnftsTMmbrs_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/BenefitsToMembersGrp/TotalAmt 

    FsFrSrvcsLgl_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/FeesForServicesLegalGrp/ProgramServicesAmt 

    FsFrSrvcsMngmnt_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/FeesForServicesManagementGrp/TotalAmt 

    InfInSkdOPrtIXInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part IX  Description: Schedule O contains a response to a question in Part IX  most recent xpath: /IRS990/InfoInScheduleOPartIXInd 

    TtlJntCsts_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/TotalJointCostsGrp/FundraisingAmt 

    Occpncy_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/OccupancyGrp/TotalAmt 

    InfrmtnTchnlgy_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/InformationTechnologyGrp/TotalAmt 

    DprctnDpltn_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/DepreciationDepletionGrp/TotalAmt 

    Rylts_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/RoyaltiesGrp/FundraisingAmt 

    PymtTrvlEntrtnmntPbOfcl_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/PymtTravelEntrtnmntPubOfclGrp/ManagementAndGeneralAmt 

    Advrtsng_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/AdvertisingGrp/FundraisingAmt 

    CmpCrrntOfcrDrctrs_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/CompCurrentOfcrDirectorsGrp/FundraisingAmt 

    FsFrSrvcsPrfFndrsng_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/FeesForServicesProfFundraising/FundraisingAmt 

    FsFrSrvcsLbbyng_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/FeesForServicesLobbyingGrp/ManagementAndGeneralAmt 

    PnsnPlnCntrbtns_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/PensionPlanContributionsGrp/TotalAmt 

    FsFrSrvcsLgl_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/FeesForServicesLegalGrp/TotalAmt 

    CmpDsqlPrsns_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/CompDisqualPersonsGrp/FundraisingAmt 

    CnfrncsMtngs_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/ConferencesMeetingsGrp/ManagementAndGeneralAmt 

    PymtTrvlEntrtnmntPbOfcl_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/PymtTravelEntrtnmntPubOfclGrp/FundraisingAmt 

    FsFrSrvcInvstMgmntFs_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/FeesForSrvcInvstMgmntFeesGrp/ManagementAndGeneralAmt 

    Advrtsng_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/AdvertisingGrp/ProgramServicesAmt 

    FsFrSrvcsAccntng_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/FeesForServicesAccountingGrp/ProgramServicesAmt 

    FsFrSrvcsLbbyng_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/FeesForServicesLobbyingGrp/FundraisingAmt 

    FsFrSrvcInvstMgmntFs_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/FeesForSrvcInvstMgmntFeesGrp/TotalAmt 

    CnfrncsMtngs_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/ConferencesMeetingsGrp/FundraisingAmt 

    CnfrncsMtngs_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/ConferencesMeetingsGrp/ProgramServicesAmt 

    PymntsTAfflts_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/PaymentsToAffiliatesGrp/ManagementAndGeneralAmt 

    CmpDsqlPrsns_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/CompDisqualPersonsGrp/ProgramServicesAmt 

    Intrst_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/InterestGrp/ProgramServicesAmt 

    CmpCrrntOfcrDrctrs_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/CompCurrentOfcrDirectorsGrp/ProgramServicesAmt 

    FsFrSrvcsMngmnt_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/FeesForServicesManagementGrp/ProgramServicesAmt 

    Trvl_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/TravelGrp/ProgramServicesAmt 

    TtlJntCsts_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/TotalJointCostsGrp/TotalAmt 

    Rylts_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/RoyaltiesGrp/TotalAmt 

    FsFrSrvcsMngmnt_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/FeesForServicesManagementGrp/ManagementAndGeneralAmt 

    OffcExpnss_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/OfficeExpensesGrp/FundraisingAmt 

    FsFrSrvcsOthr_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/FeesForServicesOtherGrp/TotalAmt 

    PymtTrvlEntrtnmntPbOfcl_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/PymtTravelEntrtnmntPubOfclGrp/ProgramServicesAmt 

    OthrEmplyBnfts_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/OtherEmployeeBenefitsGrp/ManagementAndGeneralAmt 

    Intrst_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/InterestGrp/FundraisingAmt 

    JntCstsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part IX Line 26  Description: Joint costs?  most recent xpath: /IRS990/JointCostsInd 

    AllOthrExpnss_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/AllOtherExpensesGrp/ProgramServicesAmt 

    FsFrSrvcsLgl_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/FeesForServicesLegalGrp/FundraisingAmt 

    InfrmtnTchnlgy_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/InformationTechnologyGrp/ManagementAndGeneralAmt 

    DprctnDpltn_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/DepreciationDepletionGrp/ProgramServicesAmt 

    FsFrSrvcsOthr_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/FeesForServicesOtherGrp/ManagementAndGeneralAmt 

    OthrSlrsAndWgs_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/OtherSalariesAndWagesGrp/FundraisingAmt 

    InfrmtnTchnlgy_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/InformationTechnologyGrp/ProgramServicesAmt 

    PyrllTxs_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/PayrollTaxesGrp/FundraisingAmt 

    Rylts_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/RoyaltiesGrp/ManagementAndGeneralAmt 

    FsFrSrvcsLbbyng_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/FeesForServicesLobbyingGrp/TotalAmt 

    FsFrSrvcsOthr_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/FeesForServicesOtherGrp/FundraisingAmt 

    TtlJntCsts_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/TotalJointCostsGrp/ProgramServicesAmt 

    PnsnPlnCntrbtns_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/PensionPlanContributionsGrp/ProgramServicesAmt 

    OffcExpnss_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/OfficeExpensesGrp/ProgramServicesAmt 

    FsFrSrvcsLbbyng_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/FeesForServicesLobbyingGrp/ProgramServicesAmt 

    AllOthrExpnss_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/AllOtherExpensesGrp/TotalAmt 

    FsFrSrvcsMngmnt_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/FeesForServicesManagementGrp/FundraisingAmt 

    OthrEmplyBnfts_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/OtherEmployeeBenefitsGrp/ProgramServicesAmt 

    PyrllTxs_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/PayrollTaxesGrp/TotalAmt 

    BnftsTMmbrs_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/BenefitsToMembersGrp/ProgramServicesAmt 

    TtlFnctnlExpnss_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/TotalFunctionalExpensesGrp/FundraisingAmt 

    TtlFnctnlExpnss_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/TotalFunctionalExpensesGrp/ManagementAndGeneralAmt 

    GrntsTDmstcIndvdls_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/GrantsToDomesticIndividualsGrp/TotalAmt 

    OthrSlrsAndWgs_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/OtherSalariesAndWagesGrp/TotalAmt 

    CmpCrrntOfcrDrctrs_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/CompCurrentOfcrDirectorsGrp/TotalAmt 

    PymntsTAfflts_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/PaymentsToAffiliatesGrp/ProgramServicesAmt 

    FsFrSrvcsAccntng_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/FeesForServicesAccountingGrp/FundraisingAmt 

    Insrnc_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/InsuranceGrp/FundraisingAmt 

    FsFrSrvcsLgl_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/FeesForServicesLegalGrp/ManagementAndGeneralAmt 

    CnfrncsMtngs_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/ConferencesMeetingsGrp/TotalAmt 

    Trvl_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/TravelGrp/TotalAmt 

    OthrEmplyBnfts_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/OtherEmployeeBenefitsGrp/FundraisingAmt 

    CmpDsqlPrsns_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/CompDisqualPersonsGrp/ManagementAndGeneralAmt 

    Trvl_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/TravelGrp/FundraisingAmt 

    GrntsTDmstcOrgs_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/GrantsToDomesticOrgsGrp/ProgramServicesAmt 

    FsFrSrvcsOthr_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/FeesForServicesOtherGrp/ProgramServicesAmt 

    OffcExpnss_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/OfficeExpensesGrp/ManagementAndGeneralAmt 

    Advrtsng_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/AdvertisingGrp/ManagementAndGeneralAmt 

    OthrEmplyBnfts_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/OtherEmployeeBenefitsGrp/TotalAmt 

    FsFrSrvcInvstMgmntFs_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/FeesForSrvcInvstMgmntFeesGrp/ProgramServicesAmt 

    FrgnGrnts_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/ForeignGrantsGrp/ProgramServicesAmt 

    GrntsTDmstcOrgs_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/GrantsToDomesticOrgsGrp/TotalAmt 

    PnsnPlnCntrbtns_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/PensionPlanContributionsGrp/ManagementAndGeneralAmt 

    GrntsTDmstcIndvdls_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/GrantsToDomesticIndividualsGrp/ProgramServicesAmt 

    Advrtsng_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/AdvertisingGrp/TotalAmt 

    TtlFnctnlExpnss_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/TotalFunctionalExpensesGrp/ProgramServicesAmt 

    TtlFnctnlExpnss_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/TotalFunctionalExpensesGrp/TotalAmt 

    FrgnGrnts_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/ForeignGrantsGrp/TotalAmt 

    PyrllTxs_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/PayrollTaxesGrp/ProgramServicesAmt 

    OffcExpnss_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/OfficeExpensesGrp/TotalAmt 

    Insrnc_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/InsuranceGrp/TotalAmt 

    Intrst_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/InterestGrp/ManagementAndGeneralAmt 

    AllOthrExpnss_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/AllOtherExpensesGrp/ManagementAndGeneralAmt 

    FsFrSrvcsPrfFndrsng_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/FeesForServicesProfFundraising/TotalAmt 

    AllOthrExpnss_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/AllOtherExpensesGrp/FundraisingAmt 

    FsFrSrvcsAccntng_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/FeesForServicesAccountingGrp/TotalAmt 

    Insrnc_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/InsuranceGrp/ProgramServicesAmt 

    PymntsTAfflts_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/PaymentsToAffiliatesGrp/TotalAmt 

    FsFrSrvcInvstMgmntFs_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/FeesForSrvcInvstMgmntFeesGrp/FundraisingAmt 

    OthrSlrsAndWgs_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/OtherSalariesAndWagesGrp/ManagementAndGeneralAmt 

    PymtTrvlEntrtnmntPbOfcl_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/PymtTravelEntrtnmntPubOfclGrp/TotalAmt 

    FsFrSrvcsAccntng_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/FeesForServicesAccountingGrp/ManagementAndGeneralAmt 

    FsFrSrvcsPrfFndrsng = models.TextField(null=True, blank=True)
    # Line number: Part IX Line 11e  Description: Fees for services (non-employees): Professional fundraising  most recent xpath: /IRS990/FeesForServicesProfFundraising 

    Trvl_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/TravelGrp/ManagementAndGeneralAmt 

    CmpDsqlPrsns_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/CompDisqualPersonsGrp/TotalAmt 

    Occpncy_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/OccupancyGrp/ManagementAndGeneralAmt 

    Occpncy_PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/OccupancyGrp/ProgramServicesAmt 

    Insrnc_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/InsuranceGrp/ManagementAndGeneralAmt 

    TtlJntCsts_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/TotalJointCostsGrp/ManagementAndGeneralAmt 

    DprctnDpltn_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/DepreciationDepletionGrp/ManagementAndGeneralAmt 

    PymntsTAfflts_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/PaymentsToAffiliatesGrp/FundraisingAmt 

    Intrst_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/InterestGrp/TotalAmt 

    PyrllTxs_MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/PayrollTaxesGrp/ManagementAndGeneralAmt 

    PnsnPlnCntrbtns_FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/PensionPlanContributionsGrp/FundraisingAmt 

#######
#
# IRS990 -  Part X Balance Sheet 
#
#######

class part_x(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    TtlNtAsstsFndBlnc_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/TotalNetAssetsFundBalanceGrp/EOYAmt 

    CpStkTrPrnCrrntFnds_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/CapStkTrPrinCurrentFundsGrp/EOYAmt 

    TmprrlyRstrNtAssts_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/TemporarilyRstrNetAssetsGrp/BOYAmt 

    UnscrdNtsLnsPybl_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/UnsecuredNotesLoansPayableGrp/EOYAmt 

    LndBldgEqpAccmDprcAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part X Line 10b  Description: Less: accumulated depreciation  most recent xpath: /IRS990/LandBldgEquipAccumDeprecAmt 

    OthrLblts_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/OtherLiabilitiesGrp/EOYAmt 

    DnrRstrNtAssts_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/DonorRestrictionNetAssetsGrp/BOYAmt 

    RcvblsFrmOffcrsEtc_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/ReceivablesFromOfficersEtcGrp/BOYAmt 

    MrtgNtsPyblScrdInvstPrp_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/MortgNotesPyblScrdInvstPropGrp/EOYAmt 

    TtLbNtAsstsFndBlnc_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/TotLiabNetAssetsFundBalanceGrp/BOYAmt 

    AccntsPyblAccrExpnss_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/AccountsPayableAccrExpnssGrp/EOYAmt 

    AccntsRcvbl_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/AccountsReceivableGrp/EOYAmt 

    PdInCpSrplsLndBldgEqpFnd_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/PdInCapSrplsLandBldgEqpFundGrp/EOYAmt 

    PrpdExpnssDfrdChrgs_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/PrepaidExpensesDefrdChargesGrp/EOYAmt 

    InvstmntsPbTrddSc_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/InvestmentsPubTradedSecGrp/BOYAmt 

    InvntrsFrSlOrUs_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/InventoriesForSaleOrUseGrp/BOYAmt 

    SvngsAndTmpCshInvst_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/SavingsAndTempCashInvstGrp/BOYAmt 

    TxExmptBndLblts_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/TaxExemptBondLiabilitiesGrp/EOYAmt 

    InvstmntsPrgrmRltd_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/InvestmentsProgramRelatedGrp/EOYAmt 

    UnscrdNtsLnsPybl_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/UnsecuredNotesLoansPayableGrp/BOYAmt 

    TtlLblts_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/TotalLiabilitiesGrp/EOYAmt 

    InvstmntsPbTrddSc_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/InvestmentsPubTradedSecGrp/EOYAmt 

    RcvblFrmDsqlfdPrsn_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/RcvblFromDisqualifiedPrsnGrp/EOYAmt 

    InvstmntsOthrScrts_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/InvestmentsOtherSecuritiesGrp/BOYAmt 

    InvntrsFrSlOrUs_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/InventoriesForSaleOrUseGrp/EOYAmt 

    EscrwAccntLblty_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/EscrowAccountLiabilityGrp/EOYAmt 

    LnsFrmOffcrsDrctrs_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/LoansFromOfficersDirectorsGrp/EOYAmt 

    UnrstrctdNtAssts_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/NoDonorRestrictionNetAssetsGrp/BOYAmt 

    TxExmptBndLblts_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/TaxExemptBondLiabilitiesGrp/BOYAmt 

    CshNnIntrstBrng_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/CashNonInterestBearingGrp/BOYAmt 

    DnrRstrNtAssts_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/DonorRestrictionNetAssetsGrp/EOYAmt 

    TtlAssts_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/TotalAssetsGrp/BOYAmt 

    RtnErnEndwmntIncmOthFnds_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/RtnEarnEndowmentIncmOthFndsGrp/BOYAmt 

    OthrLblts_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/OtherLiabilitiesGrp/BOYAmt 

    OthNtsLnsRcvblNt_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/OthNotesLoansReceivableNetGrp/EOYAmt 

    DfrrdRvn_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/DeferredRevenueGrp/EOYAmt 

    PrpdExpnssDfrdChrgs_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/PrepaidExpensesDefrdChargesGrp/BOYAmt 

    AccntsPyblAccrExpnss_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/AccountsPayableAccrExpnssGrp/BOYAmt 

    UnrstrctdNtAssts_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/UnrestrictedNetAssetsGrp/BOYAmt 

    TtlAssts_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/TotalAssetsGrp/EOYAmt 

    AccntsRcvbl_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/AccountsReceivableGrp/BOYAmt 

    OthrAsstsTtl_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/OtherAssetsTotalGrp/EOYAmt 

    RtnErnEndwmntIncmOthFnds_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/RtnEarnEndowmentIncmOthFndsGrp/EOYAmt 

    LnsFrmOffcrsDrctrs_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/LoansFromOfficersDirectorsGrp/BOYAmt 

    EscrwAccntLblty_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/EscrowAccountLiabilityGrp/BOYAmt 

    LndBldgEqpCstOrOthrBssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part X Line 10a  Description: Land, buildings, and equipment basis  most recent xpath: /IRS990/LandBldgEquipCostOrOtherBssAmt 

    MrtgNtsPyblScrdInvstPrp_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/MortgNotesPyblScrdInvstPropGrp/BOYAmt 

    OrgnztnFllwsSFAS117Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part X  Description: Organizations that follow SFAS 117, check here  most recent xpath: /IRS990/OrganizationFollowsFASB117Ind 

    DfrrdRvn_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/DeferredRevenueGrp/BOYAmt 

    PldgsAndGrntsRcvbl_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/PledgesAndGrantsReceivableGrp/EOYAmt 

    LndBldgEqpBssNt_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/LandBldgEquipBasisNetGrp/EOYAmt 

    IntngblAssts_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/IntangibleAssetsGrp/BOYAmt 

    OrgDsNtFllwSFAS117Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part X  Description: Organizations that do not follow SFAS 117, check here  most recent xpath: /IRS990/OrgDoesNotFollowSFAS117Ind 

    RcvblsFrmOffcrsEtc_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/ReceivablesFromOfficersEtcGrp/EOYAmt 

    InvstmntsOthrScrts_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/InvestmentsOtherSecuritiesGrp/EOYAmt 

    TtlNtAsstsFndBlnc_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/TotalNetAssetsFundBalanceGrp/BOYAmt 

    GrntsPybl_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/GrantsPayableGrp/BOYAmt 

    TmprrlyRstrNtAssts_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/TemporarilyRstrNetAssetsGrp/EOYAmt 

    IntngblAssts_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/IntangibleAssetsGrp/EOYAmt 

    CpStkTrPrnCrrntFnds_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/CapStkTrPrinCurrentFundsGrp/BOYAmt 

    TtlLblts_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/TotalLiabilitiesGrp/BOYAmt 

    OrgnztnFllwsSFAS117Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part X  Description: Organizations that follow SFAS 117, check here  most recent xpath: /IRS990/OrganizationFollowsSFAS117Ind 

    SvngsAndTmpCshInvst_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/SavingsAndTempCashInvstGrp/EOYAmt 

    GrntsPybl_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/GrantsPayableGrp/EOYAmt 

    PrmnntlyRstrNtAssts_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/PermanentlyRstrNetAssetsGrp/BOYAmt 

    OrgDsNtFllwSFAS117Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part X  Description: Organizations that do not follow SFAS 117, check here  most recent xpath: /IRS990/OrgDoesNotFollowFASB117Ind 

    PldgsAndGrntsRcvbl_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/PledgesAndGrantsReceivableGrp/BOYAmt 

    OthrAsstsTtl_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/OtherAssetsTotalGrp/BOYAmt 

    InfInSkdOPrtXInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part X  Description: Schedule O contains a response to a question in Part X  most recent xpath: /IRS990/InfoInScheduleOPartXInd 

    OthNtsLnsRcvblNt_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/OthNotesLoansReceivableNetGrp/BOYAmt 

    CshNnIntrstBrng_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/CashNonInterestBearingGrp/EOYAmt 

    InvstmntsPrgrmRltd_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/InvestmentsProgramRelatedGrp/BOYAmt 

    UnrstrctdNtAssts_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/NoDonorRestrictionNetAssetsGrp/EOYAmt 

    PdInCpSrplsLndBldgEqpFnd_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/PdInCapSrplsLandBldgEqpFundGrp/BOYAmt 

    PrmnntlyRstrNtAssts_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/PermanentlyRstrNetAssetsGrp/EOYAmt 

    UnrstrctdNtAssts_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/UnrestrictedNetAssetsGrp/EOYAmt 

    LndBldgEqpBssNt_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/LandBldgEquipBasisNetGrp/BOYAmt 

    TtLbNtAsstsFndBlnc_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (B)  Description:  Ending of year  most recent xpath: /IRS990/TotLiabNetAssetsFundBalanceGrp/EOYAmt 

    RcvblFrmDsqlfdPrsn_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part X Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990/RcvblFromDisqualifiedPrsnGrp/BOYAmt 

#######
#
# IRS990 -  Part XI Reconciliation of Net Assets 
#
#######

class part_xi(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    InvstmntExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 7  Description: Investment expenses  most recent xpath: /IRS990/InvestmentExpenseAmt 

    DntdSrvcsAndUsFcltsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 6  Description: Donated services and use of facilities  most recent xpath: /IRS990/DonatedServicesAndUseFcltsAmt 

    RcncltnRvnExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 3  Description: Revenue less expenses  most recent xpath: /IRS990/ReconcilationRevenueExpnssAmt 

    InfInSkdOPrtXIInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part XI  Description: Schedule O contains a response to a question in Part XI  most recent xpath: /IRS990/InfoInScheduleOPartXIInd 

    PrrPrdAdjstmntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 8  Description: Prior period adjustments  most recent xpath: /IRS990/PriorPeriodAdjustmentsAmt 

    NtUnrlzdGnsLsssInvstAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 5  Description: Net unrealized gains (losses) on investments  most recent xpath: /IRS990/NetUnrlzdGainsLossesInvstAmt 

    OthrChngsInNtAsstsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 9  Description: Other changes in net assets or fund balances  most recent xpath: /IRS990/OtherChangesInNetAssetsAmt 

#######
#
# IRS990 -  Part XII Financial Statements and Reporting 
#
#######

class part_xii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    MthdOfAccntngAccrlInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part XII Line 1  Description: Method of accounting - Accrual  most recent xpath: /IRS990/MethodOfAccountingAccrualInd 

    MthdOfAccntngCshInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part XII Line 1  Description: Method of accounting - Cash  most recent xpath: /IRS990/MethodOfAccountingCashInd 

    InfInSkdOPrtXIIInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part XII  Description: Schedule O contains a response to a question in Part XII  most recent xpath: /IRS990/InfoInScheduleOPartXIIInd 

    MthdOfAccntngOthrInd = models.TextField(null=True, blank=True)
    # Line number: Part XII Line 1  Description: Method of accounting - Other  most recent xpath: /IRS990/MethodOfAccountingOtherInd 

    AdtCmmttInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part XII Line 2c  Description: Does the organization have an audit committee?  most recent xpath: /IRS990/AuditCommitteeInd 

    AccntntCmplOrRvwInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part XII Line 2a  Description: Accountant provide compilation or review?  most recent xpath: /IRS990/AccountantCompileOrReviewInd 

    FdrlGrntAdtPrfrmdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part XII Line 3b  Description: Federal grant audit performed?  most recent xpath: /IRS990/FederalGrantAuditPerformedInd 

    FSAdtdBss_SprtBssFnclStmtInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Part XII Lines 2a and 2b  Description:  Financial statement issued on separate basis  most recent xpath: /IRS990/FSAuditedBasisGrp/SeparateBasisFinclStmtInd 

    AcctCmplOrRvwBss_SprtBssFnclStmtInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Part XII Lines 2a and 2b  Description:  Financial statement issued on separate basis  most recent xpath: /IRS990/AcctCompileOrReviewBasisGrp/SeparateBasisFinclStmtInd 

    AcctCmplOrRvwBss_CnsldtdBssFnclStmtInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Part XII Lines 2a and 2b  Description:  Financial statement issued on consolidated basis  most recent xpath: /IRS990/AcctCompileOrReviewBasisGrp/ConsolidatedBasisFinclStmtInd 

    AcctCmplOrRvwBss_CnslAndSpBssFnclStmtInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Part XII Lines 2a and 2b  Description:  Financial statement issued on consolidated and separate basis  most recent xpath: /IRS990/AcctCompileOrReviewBasisGrp/ConsolAndSepBasisFinclStmtInd 

    FSAdtdBss_CnsldtdBssFnclStmtInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Part XII Lines 2a and 2b  Description:  Financial statement issued on consolidated basis  most recent xpath: /IRS990/FSAuditedBasisGrp/ConsolidatedBasisFinclStmtInd 

    FSAdtdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part XII Line 2b  Description: Financial sheets audited?  most recent xpath: /IRS990/FSAuditedInd 

    FdrlGrntAdtRqrdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part XII Line 3a  Description: Federal grant audit required?  most recent xpath: /IRS990/FederalGrantAuditRequiredInd 

    FSAdtdBss_CnslAndSpBssFnclStmtInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Part XII Lines 2a and 2b  Description:  Financial statement issued on consolidated and separate basis  most recent xpath: /IRS990/FSAuditedBasisGrp/ConsolAndSepBasisFinclStmtInd 

#######
#
# IRS990 - SpclCndtnDsc - Special condition description
# A repeating structure from part_0
#
#######

class SpclCndtnDsc(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    SpclCndtnDsc = models.TextField(null=True, blank=True)
    # Description: Special condition description  most recent xpath: /IRS990/SpecialConditionDesc 

#######
#
# IRS990 - PrgSrvcAccmActyOthr
# A repeating structure from part_iii
#
#######

class PrgSrvcAccmActyOthr(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    ExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part III  Description:  Expense  most recent xpath: /IRS990/ProgSrvcAccomActyOtherGrp/ExpenseAmt 

    GrntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part III  Description:  Grants  most recent xpath: /IRS990/ProgSrvcAccomActyOtherGrp/GrantAmt 

    ActvtyCd = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part III  Description:  Activity code  most recent xpath: /IRS990/ProgSrvcAccomActyOtherGrp/ActivityCd 

    RvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part III  Description:  Revenue  most recent xpath: /IRS990/ProgSrvcAccomActyOtherGrp/RevenueAmt 

    Dsc = models.TextField(null=True, blank=True)
    # Line number:  Part III  Description:  Description  most recent xpath: /IRS990/ProgSrvcAccomActyOtherGrp/Desc 

#######
#
# IRS990 - FrgnCntryCd - Name of foreign country
# A repeating structure from part_v
#
#######

class FrgnCntryCd(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FrgnCntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part V Line 4b  Description: Name of foreign country  most recent xpath: /IRS990/ForeignCountryCd 

#######
#
# IRS990 - SttsWhrCpyOfRtrnIsFldCd - States where return filed
# A repeating structure from part_vi
#
#######

class SttsWhrCpyOfRtrnIsFldCd(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    SttsWhrCpyOfRtrnIsFldCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part VI Section C Line 17  Description: States where return filed  most recent xpath: /IRS990/StatesWhereCopyOfReturnIsFldCd 

#######
#
# IRS990 - CntrctrCmpnstn
# A repeating structure from part_vii
#
#######

class CntrctrCmpnstn(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    BsnssNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part VII Section B Line 1(A)  Description:  Business name line 2  most recent xpath: /IRS990/ContractorCompensationGrp/ContractorName/BusinessName/BusinessNameLine2Txt 

    FrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number:  Part VII Section B Line 1(A)  Description:  Postal code  most recent xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/ForeignAddress/ForeignPostalCd 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VII Section B Line 1(A)  Description:  Address line 1  most recent xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/USAddress/AddressLine1Txt 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number:  Part VII Section B Line 1(A)  Description:  City  most recent xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part VII Section B Line 1(A)  Description:  State  most recent xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/USAddress/StateAbbreviationCd 

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number:  Part VII Section B Line 1(A)  Description:  ZIP code  most recent xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/USAddress/ZIPCd 

    CntrctrCmpnstn_CmpnstnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VII Section B Line 1(C)  Description:  Compensation  most recent xpath: /IRS990/ContractorCompensationGrp/CompensationAmt 

    BsnssNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part VII Section B Line 1(A)  Description:  Business name line 1  most recent xpath: /IRS990/ContractorCompensationGrp/ContractorName/BusinessName/BusinessNameLine1Txt 

    CntrctrNm_PrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VII Section B Line 1(A)  Description:  Name - Person  most recent xpath: /IRS990/ContractorCompensationGrp/ContractorName/PersonNm 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VII Section B Line 1(A)  Description:  Address line 2  most recent xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/USAddress/AddressLine2Txt 

    FrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VII Section B Line 1(A)  Description:  Address line 1  most recent xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number:  Part VII Section B Line 1(A)  Description:  City  most recent xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/ForeignAddress/CityNm 

    FrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number:  Part VII Section B Line 1(A)  Description:  Province or state  most recent xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/ForeignAddress/ProvinceOrStateNm 

    CntrctrCmpnstn_SrvcsDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part VII Section B Line 1(B)  Description:  Description of services  most recent xpath: /IRS990/ContractorCompensationGrp/ServicesDesc 

    FrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part VII Section B Line 1(A)  Description:  Country  most recent xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/ForeignAddress/CountryCd 

    FrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VII Section B Line 1(A)  Description:  Address line 2  most recent xpath: /IRS990/ContractorCompensationGrp/ContractorAddress/ForeignAddress/AddressLine2Txt 

#######
#
# IRS990 - Frm990PrtVIISctnA - Section A, at least name required
# A repeating structure from part_vii
#
#######

class Frm990PrtVIISctnA(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    OffcrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part VII Section A Line 1a C  Description:  Officer  most recent xpath: /IRS990/Form990PartVIISectionAGrp/OfficerInd 

    BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part VII Section A Line 1a A  Description:  Business name line 2  most recent xpath: /IRS990/Form990PartVIISectionAGrp/BusinessName/BusinessNameLine2Txt 

    PrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part VII Section A Line 1a A  Description:  Name - Person  most recent xpath: /IRS990/Form990PartVIISectionAGrp/PersonNm 

    FrmrOfcrDrctrTrstInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part VII Section A Line 1a C  Description:  Former  most recent xpath: /IRS990/Form990PartVIISectionAGrp/FormerOfcrDirectorTrusteeInd 

    AvrgHrsPrWkRt = models.TextField(null=True, blank=True)
    # Line number: Part VII Section A Line 1a B  Description:  Average hours per week  most recent xpath: /IRS990/Form990PartVIISectionAGrp/AverageHoursPerWeekRt 

    RprtblCmpFrmRltdOrgAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VII Section A Line 1a E  Description:  Reportable compensation from related organizations  most recent xpath: /IRS990/Form990PartVIISectionAGrp/ReportableCompFromRltdOrgAmt 

    KyEmplyInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part VII Section A Line 1a C  Description:  Key Employee  most recent xpath: /IRS990/Form990PartVIISectionAGrp/KeyEmployeeInd 

    TtlTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part VII Section A Line 1a A  Description:  Title  most recent xpath: /IRS990/Form990PartVIISectionAGrp/TitleTxt 

    OthrCmpnstnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VII Section A Line 1a F  Description:  Other compensation  most recent xpath: /IRS990/Form990PartVIISectionAGrp/OtherCompensationAmt 

    RprtblCmpFrmOrgAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VII Section A Line 1a D  Description:  Reportable compensation from organization  most recent xpath: /IRS990/Form990PartVIISectionAGrp/ReportableCompFromOrgAmt 

    IndvdlTrstOrDrctrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part VII Section A Line 1a C  Description:  Individual trustee or director  most recent xpath: /IRS990/Form990PartVIISectionAGrp/IndividualTrusteeOrDirectorInd 

    InstttnlTrstInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part VII Section A Line 1a C  Description:  Institutional Trustee  most recent xpath: /IRS990/Form990PartVIISectionAGrp/InstitutionalTrusteeInd 

    HghstCmpnstdEmplyInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part VII Section A Line 1a C  Description:  Highest compensated employee  most recent xpath: /IRS990/Form990PartVIISectionAGrp/HighestCompensatedEmployeeInd 

    BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part VII Section A Line 1a A  Description:  Business name line 1  most recent xpath: /IRS990/Form990PartVIISectionAGrp/BusinessName/BusinessNameLine1Txt 

    AvrgHrsPrWkRltdOrgRt = models.TextField(null=True, blank=True)
    # Line number: Part VII Section A Line 1a B  Description:  Average hours per week for related organizations  most recent xpath: /IRS990/Form990PartVIISectionAGrp/AverageHoursPerWeekRltdOrgRt 

#######
#
# IRS990 - OthrRvnMsc
# A repeating structure from part_viii
#
#######

class OthrRvnMsc(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    BsnssCd = models.TextField(null=True, blank=True)
    # Line number:  Part VIII  Description:  Business code  most recent xpath: /IRS990/OtherRevenueMiscGrp/BusinessCd 

    Dsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part VIII Line 11a 11b 11c  Description:  Description  most recent xpath: /IRS990/OtherRevenueMiscGrp/Desc 

    ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  most recent xpath: /IRS990/OtherRevenueMiscGrp/ExclusionAmt 

    UnrltdBsnssRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  most recent xpath: /IRS990/OtherRevenueMiscGrp/UnrelatedBusinessRevenueAmt 

    RltdOrExmptFncIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  most recent xpath: /IRS990/OtherRevenueMiscGrp/RelatedOrExemptFuncIncomeAmt 

    TtlRvnClmnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  most recent xpath: /IRS990/OtherRevenueMiscGrp/TotalRevenueColumnAmt 

#######
#
# IRS990 - PrgrmSrvcRvn
# A repeating structure from part_viii
#
#######

class PrgrmSrvcRvn(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (D)  Description:  Excluded by section 512, 513, or 514: amount  most recent xpath: /IRS990/ProgramServiceRevenueGrp/ExclusionAmt 

    Dsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part VIII Line 2a - 2e  Description:  Description  most recent xpath: /IRS990/ProgramServiceRevenueGrp/Desc 

    UnrltdBsnssRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (C)  Description:  Unrelated business revenue  most recent xpath: /IRS990/ProgramServiceRevenueGrp/UnrelatedBusinessRevenueAmt 

    BsnssCd = models.TextField(null=True, blank=True)
    # Line number:  Part VIII  Description:  Business code  most recent xpath: /IRS990/ProgramServiceRevenueGrp/BusinessCd 

    RltdOrExmptFncIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (B)  Description:  Related or exempt function revenue  most recent xpath: /IRS990/ProgramServiceRevenueGrp/RelatedOrExemptFuncIncomeAmt 

    TtlRvnClmnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Column (A)  Description:  Total revenue  most recent xpath: /IRS990/ProgramServiceRevenueGrp/TotalRevenueColumnAmt 

#######
#
# IRS990 - OthrExpnss
# A repeating structure from part_ix
#
#######

class OthrExpnss(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    PrgrmSrvcsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (B)  Description:  Program services  most recent xpath: /IRS990/OtherExpensesGrp/ProgramServicesAmt 

    TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (A)  Description:  Total  most recent xpath: /IRS990/OtherExpensesGrp/TotalAmt 

    Dsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part IX Line 24a - 24d  Description:  Description  most recent xpath: /IRS990/OtherExpensesGrp/Desc 

    FndrsngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (D)  Description:  Fundraising  most recent xpath: /IRS990/OtherExpensesGrp/FundraisingAmt 

    MngmntAndGnrlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  col (C)  Description:  Management and general  most recent xpath: /IRS990/OtherExpensesGrp/ManagementAndGeneralAmt 

#######
#
# IRS990EZ - EZ Part 0 Prefatory material 
#
#######

class ez_part_0(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    MthdOfAccntngOthrDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: G  Description: Method of accounting - Other  most recent xpath: /IRS990EZ/MethodOfAccountingOtherDesc 

    ApplctnPndngInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: B  Description: Indicates this return has an application pending  most recent xpath: /IRS990EZ/ApplicationPendingInd 

    OfOrgnztnOthrDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: K  Description: Type of organization other description  most recent xpath: /IRS990EZ/TypeOfOrganizationOtherDesc 

    IntlRtrnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: B  Description: Indicates this is an initial return  most recent xpath: /IRS990EZ/InitialReturnInd 

    OfOrgnztnOthrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: K  Description: Type of organization - other  most recent xpath: /IRS990EZ/TypeOfOrganizationOtherInd 

    AmnddRtrnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: B  Description: Amended return  most recent xpath: /IRS990EZ/AmendedReturnInd 

    MthdOfAccntngCshInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: G  Description: Method of accounting - Cash  most recent xpath: /IRS990EZ/MethodOfAccountingCashInd 

    MthdOfAccntngAccrlInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: G  Description: Method of accounting - Accrual  most recent xpath: /IRS990EZ/MethodOfAccountingAccrualInd 

    SkdBNtRqrdInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: H  Description: Indicates Schedule B is not required  most recent xpath: /IRS990EZ/ScheduleBNotRequiredInd 

    Orgnztn527Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: J  Description: Indicates a 527 organization  most recent xpath: /IRS990EZ/Organization527Ind 

    NmChngInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: B  Description: Indicates this return has an name change  most recent xpath: /IRS990EZ/NameChangeInd 

    Orgnztn501c3Ind = models.TextField(null=True, blank=True)
    # Line number: J  Description: Indicates a 501(c)(3) organization  most recent xpath: /IRS990EZ/Organization501c3Ind 

    WbstAddrssTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: I  Description: Web site  most recent xpath: /IRS990EZ/WebsiteAddressTxt 

    Orgnztn49471NtPFInd = models.TextField(null=True, blank=True)
    # Line number: J  Description: Indicates a 4947(a)(1) organization  most recent xpath: /IRS990EZ/Organization4947a1NotPFInd 

    GrpExmptnNm = models.TextField(null=True, blank=True)
    # Line number: F  Description: Group exempt number  most recent xpath: /IRS990EZ/GroupExemptionNum 

    AddrssChngInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: B  Description: Indicates this return has an address change  most recent xpath: /IRS990EZ/AddressChangeInd 

    OfOrgnztnCrpInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: K  Description: Type of organization - corporation  most recent xpath: /IRS990EZ/TypeOfOrganizationCorpInd 

    OfOrgnztnTrstInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: K  Description: Type of organization - trust  most recent xpath: /IRS990EZ/TypeOfOrganizationTrustInd 

    Orgnztn501cInd = models.TextField(null=True, blank=True)
    # Line number: J  Description: Indicates a 501(c) organization  most recent xpath: /IRS990EZ/Organization501cInd 

    Orgnztn501cType = models.BigIntegerField(null=True, blank=True)
    # Line number: J  Description: Insert 501(c) no  most recent xpath: /IRS990EZ/Organization501cInd/@organization501cTypeTxt 

    GrssRcptsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: L  Description: Gross receipts  most recent xpath: /IRS990EZ/GrossReceiptsAmt 

    FnlRtrnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: B  Description: Final return  most recent xpath: /IRS990EZ/FinalReturnInd 

    OfOrgnztnAsscInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: K  Description: Type of organization - association  most recent xpath: /IRS990EZ/TypeOfOrganizationAssocInd 

#######
#
# IRS990EZ - EZ Part I Revenue, Expenses, and Changes in Net Assets or Fund Balances 
#
#######

class ez_part_i(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    SpclEvntsNtIncmLssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 6d  Description: Special events net income (or loss)  most recent xpath: /IRS990EZ/SpecialEventsNetIncomeLossAmt 

    GrntsAndSmlrAmntsPdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 10  Description: Grants and similar amounts paid  most recent xpath: /IRS990EZ/GrantsAndSimilarAmountsPaidAmt 

    OthrExpnssTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 16  Description: Other expenses - total  most recent xpath: /IRS990EZ/OtherExpensesTotalAmt 

    BnftsPdTOrFrMmbrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 11  Description: Benefits paid to or for members  most recent xpath: /IRS990EZ/BenefitsPaidToOrForMembersAmt 

    FndrsngGrssIncmAmt = models.TextField(null=True, blank=True)
    # Line number: Part I Line 6b  Description: Fundraising gross income  most recent xpath: /IRS990EZ/FundraisingGrossIncomeAmt 

    InfInSkdOPrtIInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I  Description: Schedule O contains a response to a question in Part I  most recent xpath: /IRS990EZ/InfoInScheduleOPartIInd 

    InvstmntIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 4  Description: Investment income  most recent xpath: /IRS990EZ/InvestmentIncomeAmt 

    SlOfAsstsGrssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 5a  Description: Gross amount from sale of assets other than inventory  most recent xpath: /IRS990EZ/SaleOfAssetsGrossAmt 

    NtAsstsOrFndBlncsBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 19  Description: Net assets BOY  most recent xpath: /IRS990EZ/NetAssetsOrFundBalancesBOYAmt 

    OthrChngsInNtAsstsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 20  Description: Other changes in net assets  most recent xpath: /IRS990EZ/OtherChangesInNetAssetsAmt 

    TtlExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 17  Description: Total expenses  most recent xpath: /IRS990EZ/TotalExpensesAmt 

    FsAndOthrPymtTIndCntrctAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 13  Description: Professional fees and other payments to independent contractors  most recent xpath: /IRS990EZ/FeesAndOtherPymtToIndCntrctAmt 

    CntrbtnsGftsGrntsEtcAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 1  Description: Contributions, gifts, grants, and similar amounts received  most recent xpath: /IRS990EZ/ContributionsGiftsGrantsEtcAmt 

    NtAsstsOrFndBlncsEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 21  Description: Net assets EOY  most recent xpath: /IRS990EZ/NetAssetsOrFundBalancesEOYAmt 

    CstOrOthrBssExpnsSlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 5b  Description: Cost or other basis and sales expenses  most recent xpath: /IRS990EZ/CostOrOtherBasisExpenseSaleAmt 

    PrntngPblctnsPstgAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 15  Description: Printing, publications, postage, and shipping  most recent xpath: /IRS990EZ/PrintingPublicationsPostageAmt 

    SlrsOthrCmpEmplBnftAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 12  Description: Salaries, other compensation, and employee benefits  most recent xpath: /IRS990EZ/SalariesOtherCompEmplBnftAmt 

    TtlRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 9  Description: Total revenue  most recent xpath: /IRS990EZ/TotalRevenueAmt 

    ExcssOrDfctFrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 18  Description: Excess or deficit  most recent xpath: /IRS990EZ/ExcessOrDeficitForYearAmt 

    GrssPrftLssSlsOfInvntryAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 7c  Description: Gross profit (or loss) from sales of inventory  most recent xpath: /IRS990EZ/GrossProfitLossSlsOfInvntryAmt 

    GnOrLssFrmSlOfAsstsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 5c  Description: Gain or (loss) from sale of assets other than inventory  most recent xpath: /IRS990EZ/GainOrLossFromSaleOfAssetsAmt 

    CstOfGdsSldAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 7b  Description: Less: cost of goods sold  most recent xpath: /IRS990EZ/CostOfGoodsSoldAmt 

    SpclEvntsDrctExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 6c  Description: Special events direct expenses  most recent xpath: /IRS990EZ/SpecialEventsDirectExpensesAmt 

    GmngGrssIncmAmt = models.TextField(null=True, blank=True)
    # Line number: Part I Line 6a  Description: Special events Indicates revenue from gaming  most recent xpath: /IRS990EZ/GamingGrossIncomeAmt 

    PrgrmSrvcRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 2  Description: ProgramServiceRevenue  most recent xpath: /IRS990EZ/ProgramServiceRevenueAmt 

    OthrRvnTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 8  Description: Other revenue - total  most recent xpath: /IRS990EZ/OtherRevenueTotalAmt 

    OccpncyRntUtltsAndMntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 14  Description: Occupancy, rent, utilities, and maintenance  most recent xpath: /IRS990EZ/OccupancyRentUtltsAndMaintAmt 

    MmbrshpDsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 3  Description: Membership dues and assessments  most recent xpath: /IRS990EZ/MembershipDuesAmt 

    GrssSlsOfInvntryAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 7a  Description: Gross sales of inventory  most recent xpath: /IRS990EZ/GrossSalesOfInventoryAmt 

#######
#
# IRS990EZ - EZ Part II Balance Sheets 
#
#######

class ez_part_ii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    OthrAsstsTtlDtl_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II - Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990EZ/OtherAssetsTotalDetail/BOYAmt 

    CshSvngsAndInvstmnts_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II - Column (B)  Description:  Ending of year  most recent xpath: /IRS990EZ/CashSavingsAndInvestmentsGrp/EOYAmt 

    CshSvngsAndInvstmnts_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II - Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990EZ/CashSavingsAndInvestmentsGrp/BOYAmt 

    SmOfTtlLblts_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II - Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990EZ/SumOfTotalLiabilitiesGrp/BOYAmt 

    NtAsstsOrFndBlncs_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Line 27 Column (B)  Description:  Ending of year  most recent xpath: /IRS990EZ/NetAssetsOrFundBalancesGrp/EOYAmt 

    SmOfTtlLblts_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II - Column (B)  Description:  Ending of year  most recent xpath: /IRS990EZ/SumOfTotalLiabilitiesGrp/EOYAmt 

    Frm990TtlAssts_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II - Column (B)  Description:  Ending of year  most recent xpath: /IRS990EZ/Form990TotalAssetsGrp/EOYAmt 

    Frm990TtlAssts_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II - Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990EZ/Form990TotalAssetsGrp/BOYAmt 

    OthrAsstsTtlDtl_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II - Column (B)  Description:  Ending of year  most recent xpath: /IRS990EZ/OtherAssetsTotalDetail/EOYAmt 

    NtAsstsOrFndBlncs_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Line 27 Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990EZ/NetAssetsOrFundBalancesGrp/BOYAmt 

    LndAndBldngs_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II - Column (B)  Description:  Ending of year  most recent xpath: /IRS990EZ/LandAndBuildingsGrp/EOYAmt 

    EZ_InfInSkdOPrtIIInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part II  Description: Schedule O contains a response to a question in Part II  most recent xpath: /IRS990EZ/InfoInScheduleOPartIIInd 

    LndAndBldngs_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II - Column (A)  Description:  Beginnning of year  most recent xpath: /IRS990EZ/LandAndBuildingsGrp/BOYAmt 

#######
#
# IRS990EZ - EZ Part III Program Service Accomplishments 
#
#######

class ez_part_iii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    TtlPrgrmSrvcExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Line 32  Description: Total Program Service Expenses  most recent xpath: /IRS990EZ/TotalProgramServiceExpensesAmt 

    InfInSkdOPrtIIIInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part III  Description: Schedule O contains a response to a question in Part III  most recent xpath: /IRS990EZ/InfoInScheduleOPartIIIInd 

    PrmryExmptPrpsTxt = models.TextField(null=True, blank=True)
    # Line number: Part III  Description: Primary exempt purpose  most recent xpath: /IRS990EZ/PrimaryExemptPurposeTxt 

#######
#
# IRS990EZ - EZ Part IV Compensation 
#
#######

class ez_part_iv(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    InfInSkdOPrtIVInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part IV  Description: Schedule O contains a response to a question in Part IV  most recent xpath: /IRS990EZ/InfoInScheduleOPartIVInd 

#######
#
# IRS990EZ - EZ Part V Other Information 
#
#######

class ez_part_v(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    EZ_TrnsctnWthCntrlEntInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 45b  Description: Payment from or engage in transaction with a controlled entity?  most recent xpath: /IRS990EZ/TransactionWithControlEntInd 

    EZ_DrctIndrctPltclExpndAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part V Line 37a  Description: Direct or indirect political expenditures.  most recent xpath: /IRS990EZ/DirectIndirectPltclExpendAmt 

    BsnssNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part V Line 42a  Description:  Business name line 1  most recent xpath: /IRS990EZ/BooksInCareOfDetail/BusinessName/BusinessNameLine1Txt 

    EZ_PltclCmpgnActyInd = models.TextField(null=True, blank=True)
    # Line number: Part V Line 46  Description: Did the organization engage in direct or indirect political campaign activities on behalf of or in opposition to candidates for public office?  most recent xpath: /IRS990EZ/PoliticalCampaignActyInd 

    EZ_TxImpsdUndrIRC4911Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part V Line 40a  Description: 501(c)(3) Organizations: Amount of tax imposed on the organization furing the year under section 4911  most recent xpath: /IRS990EZ/TaxImposedUnderIRC4911Amt 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part V Line 42a  Description:  State  most recent xpath: /IRS990EZ/BooksInCareOfDetail/USAddress/StateAbbreviationCd 

    EZ_LnsTFrmOffcrsAmt = models.TextField(null=True, blank=True)
    # Line number: Part V Line 38b  Description: Loans to/from officers amount  most recent xpath: /IRS990EZ/LoansToFromOfficersAmt 

    EZ_ActvtsNtPrvslyRptInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 33  Description: Did the organization engage in any activity not previously reported to the IRS?  most recent xpath: /IRS990EZ/ActivitiesNotPreviouslyRptInd 

    FrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number: Part V Line 42a  Description:  City  most recent xpath: /IRS990EZ/BooksInCareOfDetail/ForeignAddress/CityNm 

    EZ_FrgnFnnclAccntInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 42b  Description: Did the organization have an interest in or authority over a financial account in a foreign country?  most recent xpath: /IRS990EZ/ForeignFinancialAccountInd 

    BksInCrOfDtl_PrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part V Line 42a  Description:  Name - Person  most recent xpath: /IRS990EZ/BooksInCareOfDetail/PersonNm 

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number: Part V Line 42a  Description:  ZIP code  most recent xpath: /IRS990EZ/BooksInCareOfDetail/USAddress/ZIPCd 

    FrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part V Line 42a  Description:  Address line 2  most recent xpath: /IRS990EZ/BooksInCareOfDetail/ForeignAddress/AddressLine2Txt 

    EZ_OrgnztnFld990TInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 35b  Description: If "Yes" for Line 35a, has it filed a tax return on Form 990-T for this year?  most recent xpath: /IRS990EZ/OrganizationFiled990TInd 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number: Part V Line 42a  Description:  City  most recent xpath: /IRS990EZ/BooksInCareOfDetail/USAddress/CityNm 

    EZ_TxImpsdUndrIRC4912Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part V Line 40a  Description: 501(c)(3) Organizations: Amount of tax imposed on the organization furing the year under section 4912  most recent xpath: /IRS990EZ/TaxImposedUnderIRC4912Amt 

    EZ_RltdOrgnztnCtrlEntInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 45a  Description: Is any related organization a controlled entity within the meaning of section 512(b)(13)?  most recent xpath: /IRS990EZ/RelatedOrganizationCtrlEntInd 

    EZ_GrssRcptsFrPblcUsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part V Line 39b  Description: 501(c)(7) orgs: Gross receipts, included on line 9, for public use of club facilities  most recent xpath: /IRS990EZ/GrossReceiptsForPublicUseAmt 

    EZ_TxImpsdUndrIRC4955Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part V Line 40a  Description: 501(c)(3) Organizations: Amount of tax imposed on the organization furing the year under section 4955  most recent xpath: /IRS990EZ/TaxImposedUnderIRC4955Amt 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part V Line 42a  Description:  Address line 2  most recent xpath: /IRS990EZ/BooksInCareOfDetail/USAddress/AddressLine2Txt 

    EZ_DnrAdvsdFndsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 44a  Description: Maintain any donor advised funds?  most recent xpath: /IRS990EZ/DonorAdvisedFndsInd 

    EZ_NECTFlngFrm990Ind = models.TextField(null=True, blank=True)
    # Line number: Part V Line 43  Description: Indicates section 4947(a)(1) nonexempt charitable trusts filing Form 990 in lieu of Form 1041  most recent xpath: /IRS990EZ/NECTFilingForm990Ind 

    FrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number: Part V Line 42a  Description:  Province or state  most recent xpath: /IRS990EZ/BooksInCareOfDetail/ForeignAddress/ProvinceOrStateNm 

    EZ_OrgnztnHdUBIInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 35a  Description: Did the organization have unrelated business gross income of $1,000 or more during the year covered by this return?  most recent xpath: /IRS990EZ/OrganizationHadUBIInd 

    EZ_SbjctTPrxyTxInd = models.TextField(null=True, blank=True)
    # Line number: Part V Line 35c  Description: Subject to proxy tax?  most recent xpath: /IRS990EZ/SubjectToProxyTaxInd 

    FrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number: Part V Line 42a  Description:  Postal code  most recent xpath: /IRS990EZ/BooksInCareOfDetail/ForeignAddress/ForeignPostalCd 

    EZ_ChgMdTOrgnzngDcNtRptInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 34  Description: Were any changes made in the organizing or governing documents but not reported to the IRS?  most recent xpath: /IRS990EZ/ChgMadeToOrgnzngDocNotRptInd 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part V Line 42a  Description:  Address line 1  most recent xpath: /IRS990EZ/BooksInCareOfDetail/USAddress/AddressLine1Txt 

    BsnssNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part V Line 42a  Description:  Business name line 2  most recent xpath: /IRS990EZ/BooksInCareOfDetail/BusinessName/BusinessNameLine2Txt 

    EZ_FrgnOffcInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 42c  Description: At any time during the calender year, did the organization maintain an office outside of the U.S.?  most recent xpath: /IRS990EZ/ForeignOfficeInd 

    EZ_OprtHsptlInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 44b  Description: Operate one or more hospital facilities?  most recent xpath: /IRS990EZ/OperateHospitalInd 

    BksInCrOfDtl_PhnNm = models.CharField(null=True, blank=True, max_length=10)
    # Line number: Part V Line 42a  Description:  Telephone number  most recent xpath: /IRS990EZ/BooksInCareOfDetail/PhoneNum 

    EZ_MdLnsTFrmOffcrsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 38a  Description: Did the organization borrow from, or make any loans to, any officer, director, trustee, or key employee or were any such loans made in a prior year and still unpaid at the start of the period caovered by this return?  most recent xpath: /IRS990EZ/MadeLoansToFromOfficersInd 

    EZ_InfInSkdOPrtVInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V  Description: Schedule O contains a response to a question in Part V  most recent xpath: /IRS990EZ/InfoInScheduleOPartVInd 

    FrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part V Line 42a  Description:  Country  most recent xpath: /IRS990EZ/BooksInCareOfDetail/ForeignAddress/CountryCd 

    EZ_TnnngSrvcsPrvddInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 44c  Description: Payments received for indoor tanning services?  most recent xpath: /IRS990EZ/TanningServicesProvidedInd 

    EZ_Frm720FldInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 44d  Description: Form 720 filed and taxes paid on indoor tanning services?  most recent xpath: /IRS990EZ/Form720FiledInd 

    EZ_InttnFsAndCpCntrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part V Line 39a  Description: 501(c)(7) orgs: Initiation fees and capital contributions included on line 9  most recent xpath: /IRS990EZ/InitiationFeesAndCapContriAmt 

    EZ_OrgnztnDsslvdEtcInd = models.TextField(null=True, blank=True)
    # Line number: Part V Line 36  Description: Was there a liquidation, dissolution, termination, or substantial contraction during the year?  most recent xpath: /IRS990EZ/OrganizationDissolvedEtcInd 

    EZ_TxImpsdOnOrgnztnMgrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part V Line 40c  Description: Amount of tax imposed on the organization managers etc during the year under sections 4912, 4955, and 4958  most recent xpath: /IRS990EZ/TaxImposedOnOrganizationMgrAmt 

    EZ_EnggdInExcssBnftTrnsInd = models.TextField(null=True, blank=True)
    # Line number: Part V Line 40b  Description: 501(c)(3) and 501(c)(4) orgs: Did the organization engage in any section 4958 excess benefit transaction during the year, etc?  most recent xpath: /IRS990EZ/EngagedInExcessBenefitTransInd 

    FrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part V Line 42a  Description:  Address line 1  most recent xpath: /IRS990EZ/BooksInCareOfDetail/ForeignAddress/AddressLine1Txt 

    EZ_Frm1120PlFldInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 37b  Description: Did the organization file Form 1120-POL for this year?  most recent xpath: /IRS990EZ/Form1120PolFiledInd 

    EZ_TxRmbrsdByOrgnztnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part V Line 40d  Description: Amount of tax on line 40c, above, reimbursed by the organization  most recent xpath: /IRS990EZ/TaxReimbursedByOrganizationAmt 

    EZ_PrhbtdTxShltrTrnsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 40e  Description: At any time during the tax year, was the organization a party to a prohibited tax shelter transaction?  most recent xpath: /IRS990EZ/ProhibitedTaxShelterTransInd 

#######
#
# IRS990EZ - EZ Part VI Section 501(c)(3) Organizations Only 
#
#######

class ez_part_vi(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    PrtVIOfCmpOfHghstPdEmplTxt = models.TextField(null=True, blank=True)
    # Line number: Part VI Line 50  Description: If there are none, enter "None"  most recent xpath: /IRS990EZ/PartVIOfCompOfHghstPdEmplTxt 

    TrnsfrExmptNnChrtblRltdOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Line 49a  Description: Did the organization make any transfers to an exempt non-charitable related organization?  most recent xpath: /IRS990EZ/TrnsfrExmptNonChrtblRltdOrgInd 

    FldSkdAInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Line 52  Description: Did the organization complete Schedule A?  most recent xpath: /IRS990EZ/FiledScheduleAInd 

    InfInSkdOPrtVIInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part VI  Description: Schedule O contains a response to a question in Part VI  most recent xpath: /IRS990EZ/InfoInScheduleOPartVIInd 

    RltdOrgSct527OrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Line 49b  Description: If "Yes," was the related organization(s) a section 527 organization?  most recent xpath: /IRS990EZ/RelatedOrgSect527OrgInd 

    CntrctRcvdGrtrThn100KCnt = models.TextField(null=True, blank=True)
    # Line number: Part VI Line 51d  Description: Total number of other independent contractors receiving over $100,000  most recent xpath: /IRS990EZ/CntrctRcvdGreaterThan100KCnt 

    PrtVIHghstPdCntrctPrfSrvcTxt = models.TextField(null=True, blank=True)
    # Line number: Part VI Line 51  Description: If there are none, enter "None"  most recent xpath: /IRS990EZ/PartVIHghstPdCntrctProfSrvcTxt 

    LbbyngActvtsInd = models.TextField(null=True, blank=True)
    # Line number: Part VI Line 47  Description: Did the organization engage in lobbying activities?  most recent xpath: /IRS990EZ/LobbyingActivitiesInd 

    SchlOprtngInd = models.TextField(null=True, blank=True)
    # Line number: Part VI Line 48  Description: Is the organization operating a school as described in section 170(b)(1)(A)(ii)?  most recent xpath: /IRS990EZ/SchoolOperatingInd 

    OthrEmplyPdOvr100kCnt = models.TextField(null=True, blank=True)
    # Line number: Part VI Line 50f  Description: Total number of other employees paid over $100,000  most recent xpath: /IRS990EZ/OtherEmployeePaidOver100kCnt 

#######
#
# IRS990EZ - EZSpclCndtnDsc - Special condition description
# A repeating structure from ez_part_0
#
#######

class EZSpclCndtnDsc(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    SpclCndtnDsc = models.TextField(null=True, blank=True)
    # Description: Special condition description  most recent xpath: /IRS990EZ/SpecialConditionDesc 

#######
#
# IRS990EZ - EZPrgrmSrvcAccmplshmnt
# A repeating structure from ez_part_iii
#
#######

class EZPrgrmSrvcAccmplshmnt(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    DscrptnPrgrmSrvcAccmTxt = models.TextField(null=True, blank=True)
    # Line number:  Part III  Description:  Description of program service accomplishments  most recent xpath: /IRS990EZ/ProgramSrvcAccomplishmentGrp/DescriptionProgramSrvcAccomTxt 

    GrntsAndAllctnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part III  Description:  Grants and allocations  most recent xpath: /IRS990EZ/ProgramSrvcAccomplishmentGrp/GrantsAndAllocationsAmt 

    FrgnGrntsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Part III  Description:  Includes foreign grants?  most recent xpath: /IRS990EZ/ProgramSrvcAccomplishmentGrp/ForeignGrantsInd 

    PrgrmSrvcExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part III  Description:  Program service expenses  most recent xpath: /IRS990EZ/ProgramSrvcAccomplishmentGrp/ProgramServiceExpensesAmt 

#######
#
# IRS990EZ - EZOffcrDrctrTrstEmpl
# A repeating structure from ez_part_iv
#
#######

class EZOffcrDrctrTrstEmpl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    TtlTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part IV - Column (a)  Description:  Title  most recent xpath: /IRS990EZ/OfficerDirectorTrusteeEmplGrp/TitleTxt 

    AvrgHrsPrWkDvtdTPsRt = models.TextField(null=True, blank=True)
    # Line number:  Part IV - Column (b)  Description:  Average Hours per week devoted to position  most recent xpath: /IRS990EZ/OfficerDirectorTrusteeEmplGrp/AverageHrsPerWkDevotedToPosRt 

    BsnssNmLn1 = models.TextField(null=True, blank=True)
    # Line number:  Part IV - Column (a)  Description:  Business Name Line 1  most recent xpath: /IRS990EZ/OfficerDirectorTrusteeEmplGrp/BusinessName/BusinessNameLine1 

    BsnssNmLn1 = models.TextField(null=True, blank=True)
    # Line number:  Part IV - Column (a)  Description:  Business Name Line 1  most recent xpath: /IRS990EZ/OfficerDirectorTrusteeEmplGrp/BusinessName/BusinessNameLine1Txt 

    BsnssNmLn2 = models.TextField(null=True, blank=True)
    # Line number:  Part IV - Column (a)  Description:  Business Name Line 2  most recent xpath: /IRS990EZ/OfficerDirectorTrusteeEmplGrp/BusinessName/BusinessNameLine2 

    BsnssNmLn2 = models.TextField(null=True, blank=True)
    # Line number:  Part IV - Column (a)  Description:  Business Name Line 2  most recent xpath: /IRS990EZ/OfficerDirectorTrusteeEmplGrp/BusinessName/BusinessNameLine2Txt 

    PrsnNm = models.TextField(null=True, blank=True)
    # Line number:  Part IV - Column (a)  Description:  Person Name  most recent xpath: /IRS990EZ/OfficerDirectorTrusteeEmplGrp/PersonNm 

    EmplyBnftPrgrmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part IV - Column (d)  Description:  Contributions to employee benefit plans and deferred compensation  most recent xpath: /IRS990EZ/OfficerDirectorTrusteeEmplGrp/EmployeeBenefitProgramAmt 

    ExpnsAccntOthrAllwncAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part IV - Column (e)  Description:  Expense account and other allowances  most recent xpath: /IRS990EZ/OfficerDirectorTrusteeEmplGrp/ExpenseAccountOtherAllwncAmt 

    BsnssNm = models.TextField(null=True, blank=True)
    # Line number:  Part IV - Column (a)  Description:  Business Name  most recent xpath: /IRS990EZ/OfficerDirectorTrusteeEmplGrp/BusinessName 

    CmpnstnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part IV - Column (c)  Description:  Compensation  most recent xpath: /IRS990EZ/OfficerDirectorTrusteeEmplGrp/CompensationAmt 

#######
#
# IRS990EZ - EZFrgnFnnclAccntCntryCd - Name of foreign country
# A repeating structure from ez_part_v
#
#######

class EZFrgnFnnclAccntCntryCd(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FrgnFnnclAccntCntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part V Line 42b  Description: Name of foreign country  most recent xpath: /IRS990EZ/ForeignFinancialAccountCntryCd 

#######
#
# IRS990EZ - EZFrgnOffcCntryCd - Name of foreign country
# A repeating structure from ez_part_v
#
#######

class EZFrgnOffcCntryCd(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FrgnOffcCntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part V Line 42c  Description: Name of foreign country  most recent xpath: /IRS990EZ/ForeignOfficeCountryCd 

#######
#
# IRS990EZ - EZSttsWhrCpyOfRtrnIsFldCd - States With Which a Copy of This Return is Filed
# A repeating structure from ez_part_v
#
#######

class EZSttsWhrCpyOfRtrnIsFldCd(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    SttsWhrCpyOfRtrnIsFldCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part V Line 41  Description: States With Which a Copy of This Return is Filed  most recent xpath: /IRS990EZ/StatesWhereCopyOfReturnIsFldCd 

#######
#
# IRS990EZ - EZCmpnstnHghstPdEmpl
# A repeating structure from ez_part_vi
#
#######

class EZCmpnstnHghstPdEmpl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    ExpnsAccntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Line 50 Column (e)  Description:  Expense Account  most recent xpath: /IRS990EZ/CompensationHighestPaidEmplGrp/ExpenseAccountAmt 

    CmpnstnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Line 50 Column (c)  Description:  Compensation  most recent xpath: /IRS990EZ/CompensationHighestPaidEmplGrp/CompensationAmt 

    EmplyBnftsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Line 50 Column (d)  Description:  Employee benefits  most recent xpath: /IRS990EZ/CompensationHighestPaidEmplGrp/EmployeeBenefitsAmt 

    PrsnNm = models.TextField(null=True, blank=True)
    # Line number:  Part VI Line 50 Column (a)  Description:  Highest paid employee's name  most recent xpath: /IRS990EZ/CompensationHighestPaidEmplGrp/PersonNm 

    AvrgHrsPrWkRt = models.TextField(null=True, blank=True)
    # Line number:  Part VI Line 50 Column (b)  Description:  Average hours per week  most recent xpath: /IRS990EZ/CompensationHighestPaidEmplGrp/AverageHoursPerWeekRt 

    TtlTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part VI Line 50 Column (a)  Description:  Title  most recent xpath: /IRS990EZ/CompensationHighestPaidEmplGrp/TitleTxt 

#######
#
# IRS990EZ - EZCmpnstnOfHghstPdCntrct
# A repeating structure from ez_part_vi
#
#######

class EZCmpnstnOfHghstPdCntrct(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    CmpnstnOfHghstPdCntrct_PrsnNm = models.TextField(null=True, blank=True)
    # Line number:  Part VI Line 51 Column (a)  Description:  Highest paid contractor's name - Person  most recent xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/PersonNm 

    FrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part VI Line 51 Column (a)  Description:  Country  most recent xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/ForeignAddress/CountryCd 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VI Line 51 Column (a)  Description:  Address line 1  most recent xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/USAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VI Line 51 Column (a)  Description:  Address line 2  most recent xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number:  Part VI Line 51 Column (a)  Description:  Province or state  most recent xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/ForeignAddress/ProvinceOrStateNm 

    CmpnstnOfHghstPdCntrct_BsnssNm = models.TextField(null=True, blank=True)
    # Line number:  Part VI Line 51 Column (a)  Description:  Highest paid contractor's name - Business  most recent xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/BusinessName 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VI Line 51 Column (a)  Description:  Address line 2  most recent xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/USAddress/AddressLine2Txt 

    FrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number:  Part VI Line 51 Column (a)  Description:  Postal code  most recent xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/ForeignAddress/ForeignPostalCd 

    FrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VI Line 51 Column (a)  Description:  Address line 1  most recent xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/ForeignAddress/AddressLine1Txt 

    CmpnstnOfHghstPdCntrct_CmpnstnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Line 51 Column (c)  Description:  Compensation  most recent xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/CompensationAmt 

    FrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number:  Part VI Line 51 Column (a)  Description:  City  most recent xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/ForeignAddress/CityNm 

    CmpnstnOfHghstPdCntrct_SrvcTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part VI Line 51 Column (b)  Description:  Type of service  most recent xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/ServiceTypeTxt 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number:  Part VI Line 51 Column (a)  Description:  City  most recent xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/USAddress/CityNm 

    CmpnstnOfHghstPdCntrct_BsnssNmLn1 = models.TextField(null=True, blank=True)
    # Line number:  Part VI Line 51 Column (a)  Description:  Highest paid contractor's name - Business Name Line 1  most recent xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/BusinessName/BusinessNameLine1 

    CmpnstnOfHghstPdCntrct_BsnssNmLn1 = models.TextField(null=True, blank=True)
    # Line number:  Part VI Line 51 Column (a)  Description:  Highest paid contractor's name - Business Name Line 1  most recent xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/BusinessName/BusinessNameLine1Txt 

    CmpnstnOfHghstPdCntrct_BsnssNmLn2 = models.TextField(null=True, blank=True)
    # Line number:  Part VI Line 51 Column (a)  Description:  Highest paid contractor's name - Business Name Line 2  most recent xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/BusinessName/BusinessNameLine2 

    CmpnstnOfHghstPdCntrct_BsnssNmLn2 = models.TextField(null=True, blank=True)
    # Line number:  Part VI Line 51 Column (a)  Description:  Highest paid contractor's name - Business Name Line 2  most recent xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/BusinessName/BusinessNameLine2Txt 

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number:  Part VI Line 51 Column (a)  Description:  ZIP code  most recent xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/USAddress/ZIPCd 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part VI Line 51 Column (a)  Description:  State  most recent xpath: /IRS990EZ/CompensationOfHghstPdCntrctGrp/USAddress/StateAbbreviationCd 

#######
#
# IRS990PF - PF Part 0 Prefatory material 
#
#######

class pf_part_0(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    MthdOfAccntngOthrInd = models.TextField(null=True, blank=True)
    # Line number: J  Description: Method of accounting - Other  most recent xpath: /IRS990PF/MethodOfAccountingOtherInd 

    AddrssChngInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: G  Description: Indicates this return has an address change  most recent xpath: /IRS990PF/AddressChangeInd 

    IntlRtrnFrmrPbChrtyInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: G  Description: Indicates this is an initial return of a former public charity  most recent xpath: /IRS990PF/InitialReturnFormerPubChrtyInd 

    MthdOfAccntngAccrlInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: J  Description: Method of accounting - Accrual  most recent xpath: /IRS990PF/MethodOfAccountingAccrualInd 

    PF60MnthTrmSct507b1BInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: F  Description: Indicates private foundation is in a 60-month termination under section 507(b)(1)(B)  most recent xpath: /IRS990PF/PF60MonthTermSect507b1BInd 

    IntlRtrnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: G  Description: Indicates this is an initial return  most recent xpath: /IRS990PF/InitialReturnInd 

    PFSttsTrmSct507b1AInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: E  Description: Indicates private foundation status terminated under section 507(b)(1)(A)  most recent xpath: /IRS990PF/PFStatusTermSect507b1AInd 

    FrgnOrgMtng85PctTstInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: D2  Description: Indicates this return is for a foreign organization meeting 85% test  most recent xpath: /IRS990PF/ForeignOrgMeeting85PctTestInd 

    FrgnOrgnztnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: D1  Description: Indicates this return is for a foreign organization  most recent xpath: /IRS990PF/ForeignOrganizationInd 

    Orgnztn501c3TxblPFInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: H  Description: Other taxable private foundation  most recent xpath: /IRS990PF/Organization501c3TaxablePFInd 

    Orgnztn501c3ExmptPFInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: H  Description: Section 501(c)(3) exempt private foundation  most recent xpath: /IRS990PF/Organization501c3ExemptPFInd 

    FMVAsstsEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: I  Description: Fair market value of all assets at end of year  most recent xpath: /IRS990PF/FMVAssetsEOYAmt 

    Orgnztn49471TrtdPFInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: H  Description: Section 4947(a)(1) nonexempt charitable trust  most recent xpath: /IRS990PF/Organization4947a1TrtdPFInd 

    MthdOfAccntngCshInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: J  Description: Method of accounting - Cash  most recent xpath: /IRS990PF/MethodOfAccountingCashInd 

    ApplctnPndngInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: C  Description: Indicates this return has an application pending  most recent xpath: /IRS990PF/ApplicationPendingInd 

    AmnddRtrnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: G  Description: Amended return  most recent xpath: /IRS990PF/AmendedReturnInd 

    FnlRtrnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: G  Description: Final return  most recent xpath: /IRS990PF/FinalReturnInd 

    NmChngInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: G  Description: Indicates this return has an name change  most recent xpath: /IRS990PF/NameChangeInd 

#######
#
# IRS990PF - PF Part I Analysis of Revenue and Expenses 
#
#######

class pf_part_i(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    ExcssRvnOvrExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 27a(a)  Description: Excess of Revenue Over Expenses and Disbursements - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/ExcessRevenueOverExpensesAmt 

    OthrPrfFsDsbrsChrtblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 16c(d)  Description: Other Professional Fees - Disbursements for Charitable Purposes  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherProfFeesDsbrsChrtblAmt 

    IntrstNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 17(b)  Description: Interest - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/InterestNetInvstIncmAmt 

    OthrIncmAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 11(c)  Description: Other Income - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherIncomeAdjNetIncmAmt 

    TrvCnfMtngAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 21(c)  Description: Travel, Conferences, and Meetings - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TravConfMeetingAdjNetIncmAmt 

    TtOprExpnssRvAndExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 24(a)  Description: Total Operating and Administrative Expenses - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotOprExpensesRevAndExpnssAmt 

    AccntngFsRvAndExpnssAmt = models.TextField(null=True, blank=True)
    # Line number: Part I Line 16b(a)  Description: Accounting Fees - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/AccountingFeesRevAndExpnssAmt 

    TxsNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 18(b)  Description: Taxes - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TaxesNetInvstIncmAmt 

    TtlAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 12(c)  Description: Total - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotalAdjNetIncmAmt 

    LglFsAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 16a(c)  Description: Legal Fees - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/LegalFeesAdjNetIncmAmt 

    OccpncyAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 20(c)  Description: Occupancy - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OccupancyAdjNetIncmAmt 

    TtlExpnssAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 26(c)  Description: Total Expenses and Disbursements - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotalExpensesAdjNetIncmAmt 

    PrntngAndPbRvAndExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 22(a)  Description: Printing and Publications - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/PrintingAndPubRevAndExpnssAmt 

    PrntngAndPbDsbrsChrtblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 22(d)  Description: Printing and Publications - Disbursements for Charitable Purposes  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/PrintingAndPubDsbrsChrtblAmt 

    PnsnEmplBnftRvAndExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 15(a)  Description: Pension Plans, Employee Benefits - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/PensionEmplBnftRevAndExpnssAmt 

    TrvCnfMtngNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 21(b)  Description: Travel, Conferences, and Meetings - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TravConfMeetingNetInvstIncmAmt 

    IntrstOnSvRvAndExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 3(a)  Description: Interest on Savings and Temporary Cash Investments - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/InterestOnSavRevAndExpnssAmt 

    TxsAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 18(c)  Description: Taxes - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TaxesAdjNetIncmAmt 

    OthEmplSlrsWgsAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 14(c)  Description: Other Employee Salaries and Wages - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OthEmplSlrsWgsAdjNetIncmAmt 

    PnsnEmplBnftNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 15(b)  Description: Pension Plans, Employee Benefits - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/PensionEmplBnftNetInvstIncmAmt 

    CstOfGdsSldAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 10b  Description: Cost of Goods Sold  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/CostOfGoodsSoldAmt 

    LglFsNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 16a(b)  Description: Legal Fees - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/LegalFeesNetInvstIncmAmt 

    IntrstAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 17(c)  Description: Interest - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/InterestAdjNetIncmAmt 

    DvdndsAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 4(c)  Description: Dividends and Interest from Securities - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/DividendsAdjNetIncmAmt 

    TtlExpnssDsbrsChrtblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 26(d)  Description: Total Expenses and Disbursements - Disbursements for Charitable Purposes  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotalExpensesDsbrsChrtblAmt 

    CmpOfcrDrTrstDsbrsChrtblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 13(d)  Description: Compensation of Officers, Directors, Trustees, etc. - Disbursements for Charitable Purposes  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/CompOfcrDirTrstDsbrsChrtblAmt 

    TrvCnfMtngRvAndExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 21(a)  Description: Travel, Conferences, and Meetings - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TravConfMeetingRevAndExpnssAmt 

    PnsnEmplBnftDsbrsChrtblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 15(d)  Description: Pension Plans, Employee Benefits - Disbursements for Charitable Purposes  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/PensionEmplBnftDsbrsChrtblAmt 

    DvdndsNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 4(b)  Description: Dividends and Interest from Securities - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/DividendsNetInvstIncmAmt 

    OthEmplSlrsWgsNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 14(b)  Description: Other Employee Salaries and Wages - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OthEmplSlrsWgsNetInvstIncmAmt 

    CmpOfcrDrTrstNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 13(b)  Description: Compensation of Officers, Directors, Trustees, etc. - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/CompOfcrDirTrstNetInvstIncmAmt 

    OthEmplSlrsWgsRvAndExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 14(a)  Description: Other Employee Salaries and Wages - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OthEmplSlrsWgsRevAndExpnssAmt 

    OccpncyNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 20(b)  Description: Occupancy - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OccupancyNetInvstIncmAmt 

    TtOprExpnssAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 24(c)  Description: Total Operating and Administrative Expenses - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotOprExpensesAdjNetIncmAmt 

    OthrExpnssAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 23(c)  Description: Other Expenses - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherExpensesAdjNetIncmAmt 

    TtOprExpnssNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 24(b)  Description: Total Operating and Administrative Expenses - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotOprExpensesNetInvstIncmAmt 

    OthrIncmNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 11(b)  Description: Other Income - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherIncomeNetInvstIncmAmt 

    TtlRvAndExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 12(a)  Description: Total - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotalRevAndExpnssAmt 

    GrssRntsNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 5a(b)  Description: Gross Rents - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/GrossRentsNetInvstIncmAmt 

    NtRntlIncmOrLssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 5b  Description: Net Rental Income or Los  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/NetRentalIncomeOrLossAmt 

    OthrExpnssNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 23(b)  Description: Other Expenses - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherExpensesNetInvstIncmAmt 

    GrssSlsLssRtAndAllwncAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 10a  Description: Gross Sales Less Returns and Allowances  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/GrossSalesLessRetAndAllwncAmt 

    NtInvstmntIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 27b(b)  Description: Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/NetInvestmentIncomeAmt 

    TtlExpnssNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 26(b)  Description: Total Expenses and Disbursements - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotalExpensesNetInvstIncmAmt 

    CntrRcvdRvAndExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 1(a)  Description: Contributions Received - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/ContriRcvdRevAndExpnssAmt 

    TrvCnfMtngDsbrsChrtblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 21(d)  Description: Travel, Conferences, and Meetings - Disbursements for Charitable Purposes  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TravConfMeetingDsbrsChrtblAmt 

    OccpncyRvAndExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 20(a)  Description: Occupancy - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OccupancyRevAndExpnssAmt 

    NtSTCptlGnAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 8(c)  Description: Net Short-Term Capital Gain - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/NetSTCapitalGainAdjNetIncmAmt 

    LglFsDsbrsChrtblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 16a(d)  Description: Legal Fees - Disbursements for Charitable Purposes  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/LegalFeesDsbrsChrtblAmt 

    DvdndsRvAndExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 4(a)  Description: Dividends and Interest from Securities - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/DividendsRevAndExpnssAmt 

    PrntngAndPbNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 22(b)  Description: Printing and Publications - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/PrintingAndPubNetInvstIncmAmt 

    CmpOfcrDrTrstRvAndExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 13(a)  Description: Compensation of Officers, Directors, Trustees, etc. - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/CompOfcrDirTrstRevAndExpnssAmt 

    AccntngFsNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 16b(b)  Description: Accounting Fees - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/AccountingFeesNetInvstIncmAmt 

    IntrstDsbrsChrtblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 17(d)  Description: Interest - Disbursements for Charitable Purposes  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/InterestDsbrsChrtblAmt 

    GrssRntsRvAndExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 5a(a)  Description: Gross Rents - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/GrossRentsRevAndExpnssAmt 

    AccntngFsChrtblPrpsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 16b(d)  Description: Accounting Fees - Disbursements for Charitable Purposes  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/AccountingFeesChrtblPrpsAmt 

    IntrstOnSvngsAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 3(c)  Description: Interest on Savings and Temporary Cash Investments - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/InterestOnSavingsAdjNetIncmAmt 

    PnsnEmplBnftAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 15(c)  Description: Pension Plans, Employee Benefits - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/PensionEmplBnftAdjNetIncmAmt 

    CpGnNtIncmNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 7(b)  Description: Capital Gain Net Income - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/CapGainNetIncmNetInvstIncmAmt 

    CntrPdRvAndExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 25(a)  Description: Contributions, Gifts, Grants Paid - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/ContriPaidRevAndExpnssAmt 

    PrntngAndPbAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 22(c)  Description: Printing and Publications - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/PrintingAndPubAdjNetIncmAmt 

    TtOprExpnssDsbrsChrtblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 24(d)  Description: Total Operating and Administrative Expenses - Disbursements for Charitable Purposes  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotOprExpensesDsbrsChrtblAmt 

    OthrExpnssRvAndExpnssAmt = models.TextField(null=True, blank=True)
    # Line number: Part I Line 23(a)  Description: Other Expenses - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherExpensesRevAndExpnssAmt 

    DprcAndDpltnRvAndExpnssAmt = models.TextField(null=True, blank=True)
    # Line number: Part I Line 19(a)  Description: Depreciation and Depletion - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/DeprecAndDpltnRevAndExpnssAmt 

    DprcAndDpltnAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 19(c)  Description: Depreciation and Depletion - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/DeprecAndDpltnAdjNetIncmAmt 

    OthrPrfFsAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 16c(c)  Description: Other Professional Fees - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherProfFeesAdjNetIncmAmt 

    AccntngFsAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 16b(c)  Description: Accounting Fees - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/AccountingFeesAdjNetIncmAmt 

    LglFsRvAndExpnssAmt = models.TextField(null=True, blank=True)
    # Line number: Part I Line 16a(a)  Description: Legal Fees - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/LegalFeesRevAndExpnssAmt 

    OthrPrfFsNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 16c(b)  Description: Other Professional Fees - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherProfFeesNetInvstIncmAmt 

    OthrIncmRvAndExpnssAmt = models.TextField(null=True, blank=True)
    # Line number: Part I Line 11(a)  Description: Other Income - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherIncomeRevAndExpnssAmt 

    GrssPrftRvAndExpnssAmt = models.TextField(null=True, blank=True)
    # Line number: Part I Line 10c(a)  Description: Gross Profit - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/GrossProfitRevAndExpnssAmt 

    IntrstOnSvNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 3(b)  Description: Interest on Savings and Temporary Cash Investments - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/InterestOnSavNetInvstIncmAmt 

    OthrExpnssDsbrsChrtblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 23(d)  Description: Other Expenses - Disbursements for Charitable Purposes  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherExpensesDsbrsChrtblAmt 

    OthEmplSlrsWgsDsbrsChrtblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 14(d)  Description: Other Employee Salaries and Wages - Disbursements for Charitable Purposes  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OthEmplSlrsWgsDsbrsChrtblAmt 

    TtlExpnssRvAndExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 26(a)  Description: Total Expenses and Disbursements - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotalExpensesRevAndExpnssAmt 

    GrssRntsAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 5a(c)  Description: Gross Rents - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/GrossRentsAdjNetIncmAmt 

    IntrstRvAndExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 17(a)  Description: Interest - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/InterestRevAndExpnssAmt 

    TxsRvAndExpnssAmt = models.TextField(null=True, blank=True)
    # Line number: Part I Line 18(a)  Description: Taxes - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TaxesRevAndExpnssAmt 

    CntrPdDsbrsChrtblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 25(d)  Description: Contributions, Gifts, Grants Paid - Disbursements for Charitable Purposes  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/ContriPaidDsbrsChrtblAmt 

    TxsDsbrsChrtblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 18(d)  Description: Taxes - Disbursements for Charitable Purposes  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TaxesDsbrsChrtblAmt 

    TtlNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 12(b)  Description: Total - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/TotalNetInvstIncmAmt 

    AdjstdNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 27c(c)  Description: Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/AdjustedNetIncomeAmt 

    OthrPrfFsRvAndExpnssAmt = models.TextField(null=True, blank=True)
    # Line number: Part I Line 16c(a)  Description: Other Professional Fees - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OtherProfFeesRevAndExpnssAmt 

    DprcAndDpltnNtInvstIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 19(b)  Description: Depreciation and Depletion - Net Investment Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/DeprecAndDpltnNetInvstIncmAmt 

    IncmMdfctnsAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 9(c)  Description: Income Modifications - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/IncmModificationsAdjNetIncmAmt 

    CmpOfcrDrTrstAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 13(c)  Description: Compensation of Officers, Directors, Trustees, etc. - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/CompOfcrDirTrstAdjNetIncmAmt 

    GrssSlsPrcAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 6b  Description: Gross Sales Price  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/GrossSalesPriceAmt 

    OccpncyDsbrsChrtblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 20(d)  Description: Occupancy - Disbursements for Charitable Purposes  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/OccupancyDsbrsChrtblAmt 

    NtGnSlAstRvAndExpnssAmt = models.TextField(null=True, blank=True)
    # Line number: Part I Line 6a(a)  Description: Net Gain from Sale of Assets - Revenue and Expenses per Books  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/NetGainSaleAstRevAndExpnssAmt 

    SkdBNtRqrdInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 2  Description: Not required to attach Schedule B  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/ScheduleBNotRequiredInd 

    GrssPrftAdjNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 10c(c)  Description: Gross Profit - Adjusted Net Income  most recent xpath: /IRS990PF/AnalysisOfRevenueAndExpenses/GrossProfitAdjNetIncmAmt 

#######
#
# IRS990PF - PF Part II Balance Sheets 
#
#######

class pf_part_ii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    GrntsPyblEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 18(b)  Description: Grants Payable - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/GrantsPayableEOYAmt 

    PrpdExpnssBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 9(a)  Description: Prepaid Expenses - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PrepaidExpensesBOYAmt 

    TtlAsstsEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 16(b)  Description: Total Assets - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TotalAssetsEOYAmt 

    OthrAsstsEOYAmt = models.TextField(null=True, blank=True)
    # Line number: Part II Line 15(b)  Description: Other Assets - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherAssetsEOYAmt 

    LndBldgEqpAccmDprcAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 14  Description: Accumulated Depreciation (for Land, Buildings, and Equipment)  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LandBldgEquipAccumDeprecAmt 

    DnrRstrNtAssts_BOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 25(a)  Description: Net assets with donor restrictions - BOY - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/DonorRstrNetAssetsBOYAmt 

    OrgDsNtFllwSFAS117Ind = models.CharField(null=True, blank=True, max_length=1)
    # Description: Organizations That Do Not Follow SFAS 117  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OrgDoesNotFollowSFAS117Ind 

    TtlLbltsBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 23(a)  Description: Total Liabilities - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TotalLiabilitiesBOYAmt 

    PrmnntlyRstrctdEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 26(b)  Description: Permanently Restricted - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PermanentlyRestrictedEOYAmt 

    PldgsRcvblBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 4(a)  Description: Pledges Receivable - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PledgesRcvblBOYAmt 

    OthrInvstmntsEOYFMVAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 13(c)  Description: Investments, Other - End of Year - Fair Market Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherInvestmentsEOYFMVAmt 

    PldgsRcvblEOYFMVAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 4(c)  Description: Pledges Receivable - End of Year - Fair Market Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PledgesRcvblEOYFMVAmt 

    InvstLndCstOrOthrBssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 11  Description: Investments, Land, Etc. Basis  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/InvstLandCostOrOtherBasisAmt 

    CptlStckBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 27(a)  Description: Capital Stock - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CapitalStockBOYAmt 

    OthrLbltsBOYAmt = models.TextField(null=True, blank=True)
    # Line number: Part II Line 22(a)  Description: Other Liabilities - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherLiabilitiesBOYAmt 

    CshEOYFMVAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 1(c)  Description: Cash - End of Year - Fair Market Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CashEOYFMVAmt 

    UnrstrctdBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 24(a)  Description: Unrestricted - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/UnrestrictedBOYAmt 

    USGvrnmntOblgtnsEOYAmt = models.TextField(null=True, blank=True)
    # Line number: Part II Line 10a(b)  Description: Investments, Government Obligations - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/USGovernmentObligationsEOYAmt 

    AddtnlPdInCptlEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 28(b)  Description: Paid-in or Capital Surplus - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/AdditionalPaidInCapitalEOYAmt 

    TtNtAstOrFndBlncsEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 30(b)  Description: Total Net Assets or Fund Balances - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TotNetAstOrFundBalancesEOYAmt 

    USGvrnmntOblgtnsBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 10a(a)  Description: Investments, Government Obligations - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/USGovernmentObligationsBOYAmt 

    AcctRcvblAllwncDbtflAcctAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 3  Description: Allowance for Doubtful Accounts (for Accounts Receivable)  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/AcctRcvblAllwncDbtflAcctAmt 

    TtlLbltsEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 23(b)  Description: Total Liabilities - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TotalLiabilitiesEOYAmt 

    GrntsRcvblEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 5(b)  Description: Grants Receivable - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/GrantsReceivableEOYAmt 

    AcctRcvblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 3  Description: Accounts Receivable  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/AcctRcvblAmt 

    OrgnztnFllwsSFAS117Ind = models.CharField(null=True, blank=True, max_length=1)
    # Description: Organizations That Follow SFAS 117  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OrganizationFollowsFASB117Ind 

    CrprtBndsEOYAmt = models.TextField(null=True, blank=True)
    # Line number: Part II Line 10c(b)  Description: Investments, Corporate Bonds - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CorporateBondsEOYAmt 

    SvAndTmpCshInvstEOYFMVAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 2(c)  Description: Savings and Temporary Cash Investments - End of Year - Fair Market Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/SavAndTempCashInvstEOYFMVAmt 

    LndBldgInvstmntsEOYFMVAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 11(c)  Description: Investments, Land, Etc. - End of Year - Fair Market Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LandBldgInvestmentsEOYFMVAmt 

    DfrrdRvnBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 19(a)  Description: Deferred Revenue - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/DeferredRevenueBOYAmt 

    LndBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 14(a)  Description: Land, Buildings, and Equipment - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LandBOYAmt 

    PrpdExpnssEOYFMVAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 9(c)  Description: Prepaid Expenses - End of Year - Fair Market Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PrepaidExpensesEOYFMVAmt 

    TmprrlyRstrctdBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 25(a)  Description: Temporarily Restricted - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TemporarilyRestrictedBOYAmt 

    OrgnztnFllwsSFAS117Ind = models.CharField(null=True, blank=True, max_length=1)
    # Description: Organizations That Follow SFAS 117  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OrganizationFollowsSFAS117Ind 

    LndBldgEqpCstOrOthrBssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 14  Description: Land, Buildings, and Equipment - Basis  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LandBldgEquipCostOrOtherBssAmt 

    LndBldgInvstmntsEOYAmt = models.TextField(null=True, blank=True)
    # Line number: Part II Line 11(b)  Description: Investments, Land, Etc. - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LandBldgInvestmentsEOYAmt 

    OthrInvstmntsBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 13(a)  Description: Investments, Other - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherInvestmentsBOYAmt 

    RtndErnngBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 29(a)  Description: Retained Earnings - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/RetainedEarningBOYAmt 

    RcvblFrmOffcrsEOYFMVAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 6(c)  Description: Receivables from Officers - End of Year - Fair Market Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/RcvblFromOfficersEOYFMVAmt 

    AcctRcvblEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 3(b)  Description: Accounts Receivable - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/AcctRcvblEOYAmt 

    CshEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 1(b)  Description: Cash - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CashEOYAmt 

    SvAndTmpCshInvstEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 2(b)  Description: Savings and Temporary Cash Investments - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/SavAndTempCashInvstEOYAmt 

    DnrRstrNtAssts_EOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 25(b)  Description: Net assets with donor restrictions - EOY - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/DonorRstrNetAssetsEOYAmt 

    UnrstrctdBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 24(a)  Description: Unrestricted - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/NoDonorRstrNetAssestsBOYAmt 

    CrprtBndsEOYFMVAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 10c(c)  Description: Investments, Corporate Bonds - End of Year - Fair Market Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CorporateBondsEOYFMVAmt 

    AddtnlPdInCptlBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 28(a)  Description: Paid-in or Capital Surplus - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/AdditionalPaidInCapitalBOYAmt 

    CrprtStckEOYFMVAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 10b(c)  Description: Investments, Corporate Stock - End of Year - Fair Market Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CorporateStockEOYFMVAmt 

    UnrstrctdEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 24(b)  Description: Unrestricted - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/NoDonorRstrNetAssestsEOYAmt 

    USGvtOblgtnsEOYFMVAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 10a(c)  Description: Investments, Government Obligations - End of Year - Fair Market Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/USGovtObligationsEOYFMVAmt 

    PldgsRcvblEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 4(b)  Description: Pledges Receivable - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PledgesRcvblEOYAmt 

    LnsFrmOffcrsEOYAmt = models.TextField(null=True, blank=True)
    # Line number: Part II Line 20(b)  Description: Loans from Officers - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LoansFromOfficersEOYAmt 

    AcctRcvblEOYFMVAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 3(c)  Description: Accounts Receivable - End of Year - Fair Market Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/AcctRcvblEOYFMVAmt 

    TtlAsstsBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 16(a)  Description: Total Assets - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TotalAssetsBOYAmt 

    SvAndTmpCshInvstBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 2(a)  Description: Savings and Temporary Cash Investments - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/SavAndTempCashInvstBOYAmt 

    RcvblFrmOffcrsEOYAmt = models.TextField(null=True, blank=True)
    # Line number: Part II Line 6(b)  Description: Receivables from Officers - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/RcvblFromOfficersEOYAmt 

    AccntsPyblBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 17(a)  Description: Accounts Payable - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/AccountsPayableBOYAmt 

    PldgsRcvblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 4  Description: Pledges Receivable  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PledgesRcvblAmt 

    InvntrsEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 8(b)  Description: Inventories for Sale or Use - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/InventoriesEOYAmt 

    AcctRcvblBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 3(a)  Description: Accounts Receivable - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/AcctRcvblBOYAmt 

    OthrNtsAndLnsRcvblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 7  Description: Other Notes and Loans Receivable  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherNtsAndLoansRcvblAmt 

    GrntsRcvblEOYFMVAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 5(c)  Description: Grants Receivable - End of Year - Fair Market Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/GrantsReceivableEOYFMVAmt 

    PldgsRcvblAllwncDbtflAcctAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 4  Description: Allowance for Doubtful Accounts (for Pledges Receivable)  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PledgesRcvblAllwncDbtflAcctAmt 

    PrpdExpnssEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 9(b)  Description: Prepaid Expenses - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PrepaidExpensesEOYAmt 

    CptlStckEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 27(b)  Description: Capital Stock - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CapitalStockEOYAmt 

    MrtggsAndNtsPyblEOYAmt = models.TextField(null=True, blank=True)
    # Line number: Part II Line 21(b)  Description: Mortgages and Notes Payable - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/MortgagesAndNotesPayableEOYAmt 

    OthrNtsAndLnsRcvblEOYAmt = models.TextField(null=True, blank=True)
    # Line number: Part II Line 7(b)  Description: Other Notes and Loans Receivable - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherNtsAndLoansRcvblEOYAmt 

    LndBldgInvstmntsBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 11(a)  Description: Investments, Land, Etc. - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LandBldgInvestmentsBOYAmt 

    RcvblFrmOffcrsBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 6(a)  Description: Receivables from Officers - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/RcvblFromOfficersBOYAmt 

    LnsFrmOffcrsBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 20(a)  Description: Loans from Officers - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LoansFromOfficersBOYAmt 

    TtlLbltsNtAstBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 31(a)  Description: Total Liabilities and Net Assets - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TotalLiabilitiesNetAstBOYAmt 

    OthrRcvblAllwncDbtflAcctAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 7  Description: Allowance for Doubtful Accounts (for Other Notes and Loans Receivable)  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherRcvblAllwncDbtflAcctAmt 

    MrtggLnsBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 12(a)  Description: Investments, Mortgage Loans - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/MortgageLoansBOYAmt 

    InvstLndAccmDprctnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 11  Description: Accumulated Depreciation (for Investments, Land, Etc.)  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/InvstLandAccumDepreciationAmt 

    TtNtAstOrFndBlncsBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 30(a)  Description: Total Net Assets or Fund Balances - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TotNetAstOrFundBalancesBOYAmt 

    CrprtBndsBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 10c(a)  Description: Investments, Corporate Bonds - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CorporateBondsBOYAmt 

    OthrLbltsEOYAmt = models.TextField(null=True, blank=True)
    # Line number: Part II Line 22(b)  Description: Other Liabilities - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherLiabilitiesEOYAmt 

    CshBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 1(a)  Description: Cash - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CashBOYAmt 

    AccntsPyblEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 17(b)  Description: Accounts Payable - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/AccountsPayableEOYAmt 

    InvntrsBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 8(a)  Description: Inventories for Sale or Use - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/InventoriesBOYAmt 

    GrntsPyblBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 18(a)  Description: Grants Payable - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/GrantsPayableBOYAmt 

    RtndErnngEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 29(b)  Description: Retained Earnings - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/RetainedEarningEOYAmt 

    UnrstrctdEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 24(b)  Description: Unrestricted - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/UnrestrictedEOYAmt 

    TmprrlyRstrctdEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 25(b)  Description: Temporarily Restricted - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TemporarilyRestrictedEOYAmt 

    InvntrsEOYFMVAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 8(c)  Description: Inventories for Sale or Use - End of Year - Fair Market Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/InventoriesEOYFMVAmt 

    DfrrdRvnEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 19(b)  Description: Deferred Revenue - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/DeferredRevenueEOYAmt 

    OthrNtsAndLnsRcvblEOYFMVAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 7(c)  Description: Other Notes and Loans Receivable - End of Year - Fair Market Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherNtsAndLoansRcvblEOYFMVAmt 

    TtlAsstsEOYFMVAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 16(c)  Description: Total Assets - End of Year - Fair Market Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TotalAssetsEOYFMVAmt 

    MrtggLnsEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 12(b)  Description: Investments, Mortgage Loans - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/MortgageLoansEOYAmt 

    MrtggsAndNtsPyblBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 21(a)  Description: Mortgages and Notes Payable - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/MortgagesAndNotesPayableBOYAmt 

    TtlLbltsNtAstEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 31(b)  Description: Total Liabilities and Net Assets - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/TotalLiabilitiesNetAstEOYAmt 

    OthrNtsAndLnsRcvblBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 7(a)  Description: Other Notes and Loans Receivable - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherNtsAndLoansRcvblBOYAmt 

    LndEOYFMVAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 14(c)  Description: Land, Buildings, and Equipment - End of Year - Fair Market Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LandEOYFMVAmt 

    PrmnntlyRstrctdBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 26(a)  Description: Permanently Restricted - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/PermanentlyRestrictedBOYAmt 

    CrprtStckBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 10b(a)  Description: Investments, Corporate Stock - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CorporateStockBOYAmt 

    MrtggLnsEOYFMVAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 12(c)  Description: Investments, Mortgage Loans - End of Year - Fair Market Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/MortgageLoansEOYFMVAmt 

    LndEOYAmt = models.TextField(null=True, blank=True)
    # Line number: Part II Line 14(b)  Description: Land, Buildings, and Equipment - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/LandEOYAmt 

    OthrAsstsBOYAmt = models.TextField(null=True, blank=True)
    # Line number: Part II Line 15(a)  Description: Other Assets - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherAssetsBOYAmt 

    OthrInvstmntsEOYAmt = models.TextField(null=True, blank=True)
    # Line number: Part II Line 13(b)  Description: Investments, Other - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherInvestmentsEOYAmt 

    OthrAsstsEOYFMVAmt = models.TextField(null=True, blank=True)
    # Line number: Part II Line 15(c)  Description: Other Assets - End of Year - Fair Market Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OtherAssetsEOYFMVAmt 

    CrprtStckEOYAmt = models.TextField(null=True, blank=True)
    # Line number: Part II Line 10b(b)  Description: Investments, Corporate Stock - End of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/CorporateStockEOYAmt 

    OrgDsNtFllwSFAS117Ind = models.CharField(null=True, blank=True, max_length=1)
    # Description: Organizations That Do Not Follow SFAS 117  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/OrgDoesNotFollowFASB117Ind 

    GrntsRcvblBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 5(a)  Description: Grants Receivable - Beginning of Year - Book Value  most recent xpath: /IRS990PF/Form990PFBalanceSheetsGrp/GrantsReceivableBOYAmt 

#######
#
# IRS990PF - PF Part III Changes in Net Assets or Fund Balances 
#
#######

class pf_part_iii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    TtNtAstOrFndBlncsEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Line 6  Description: Total Net Assets or Fund Balances at End of Year  most recent xpath: /IRS990PF/ChgInNetAssetsFundBalancesGrp/TotNetAstOrFundBalancesEOYAmt 

    ExcssRvnOvrExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Line 2  Description: Excess of Revenue Over Expenses and Disbursements - Revenue and Expenses per Books  most recent xpath: /IRS990PF/ChgInNetAssetsFundBalancesGrp/ExcessRevenueOverExpensesAmt 

    TtNtAstOrFndBlncsBOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Line 1  Description: Total Net Assets or Fund Balances at Beginning of Year  most recent xpath: /IRS990PF/ChgInNetAssetsFundBalancesGrp/TotNetAstOrFundBalancesBOYAmt 

    OthrIncrssAmt = models.TextField(null=True, blank=True)
    # Line number: Part III Line 3  Description: Other Increases  most recent xpath: /IRS990PF/ChgInNetAssetsFundBalancesGrp/OtherIncreasesAmt 

    OthrDcrssAmt = models.TextField(null=True, blank=True)
    # Line number: Part III Line 5  Description: Other Decreases  most recent xpath: /IRS990PF/ChgInNetAssetsFundBalancesGrp/OtherDecreasesAmt 

    SbttlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Line 4  Description: Subtotal  most recent xpath: /IRS990PF/ChgInNetAssetsFundBalancesGrp/SubtotalAmt 

#######
#
# IRS990PF - PF Part IV Capital Gains and Losses for Tax on Investment Income 
#
#######

class pf_part_iv(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    NtShrtTrmCptlGnLssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IV Line 3  Description: Net Short-Term Capital Gain or Loss  most recent xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/NetShortTermCapitalGainLossAmt 

    CptlGnNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IV Line 2  Description: Capital Gain Net Income  most recent xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapitalGainNetIncomeAmt 

#######
#
# IRS990PF - PF Part VI Excise Tax Based on Investment Income 
#
#######

class pf_part_vi(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    OrgnlRtrnTxPdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Line 7 Tax Paid with Orig Return  Description: Tax Paid with the Original Return  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/OriginalReturnTaxPaidAmt 

    TxUndrSctn511Amt = models.TextField(null=True, blank=True)
    # Line number: Part VI Line 2  Description: Tax Under Section 511  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/TaxUnderSection511Amt 

    TxBsdOnInvstmntIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Line 5  Description: Tax Based on Investment Income  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/TaxBasedOnInvestmentIncomeAmt 

    ExmptFrgnOrgTxWthldAtSrcAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Line 6b  Description: Exempt foreign organizations - tax withheld at source  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/ExemptFrgnOrgTaxWthldAtSrceAmt 

    SbttlATxAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Line 4  Description: Subtitle A Tax  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/SubtitleATaxAmt 

    ExmptOprtngFndtnsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part VI Line 1a  Description: Exempt Operating Foundations  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/ExemptOperatingFoundationsInd 

    OrgnlRtrnOvrpymntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Line 7 Orig Return Overpayment  Description: Original Return Overpayment  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/OriginalReturnOverpaymentAmt 

    EsPnltyAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Line 8  Description: Penalty for Underpayment  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/EsPenaltyAmt 

    TxDAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Line 9  Description: Tax Due  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/TaxDueAmt 

    SbttlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Line 3  Description: Subtotal (add lines 1 and 2)  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/SubtotalAmt 

    AppldTEsTxAmtB = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Line 6c  Description: Tax Paid with Extension  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/AppliedToEsTaxAmt 

    BckpWthhldngWthhldAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Line 6d  Description: Backup Withholding Erroneously Withheld  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/BackupWithholdingWithheldAmt 

    InvstmntIncmExcsTxAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Line 1  Description: Investment Income Excise Tax - amount  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/InvestmentIncomeExciseTaxAmt 

    TtlPymntsAndCrdtsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Line 7  Description: Total Credits and Payments  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/TotalPaymentsAndCreditsAmt 

    RlngLttrDt = models.CharField(null=True, blank=True, max_length=31)
    # Line number: Part VI Line 1a  Description: Date of Ruling Letter  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/RulingLetterDt 

    NtApplcblCd = models.TextField(null=True, blank=True)
    # Line number: Part VI Line 1  Description: Investment Income Excise Tax - "N/A"  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/NotApplicableCd 

    OvrpymntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Line 10  Description: Overpayment  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/OverpaymentAmt 

    AppldTEsTxAmtC = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Line 6c  Description: Tax Paid with Extension  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/ExtsnRequestIncomeTaxPaidAmt 

    RfndAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Line 11  Description: Amount to be refunded  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/RefundAmt 

    EstmtdPlsOvpmtIncmTxAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Line 6a  Description: Estimated Tax Payments and Overpayment Credited  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/EstimatedPlusOvpmtIncmTxAmt 

    Frm2220AttchdInd = models.TextField(null=True, blank=True)
    # Line number: Part VI Line 8  Description: Indicates Form 2220 is attached  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/Form2220AttachedInd 

    AppldTESTxAmtA = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Line 11  Description: Amount Credited to Next Year  most recent xpath: /IRS990PF/ExciseTaxBasedOnInvstIncmGrp/AppliedToESTaxAmt 

#######
#
# IRS990PF - PF Part VII-A Statements Regarding Activities 
#
#######

class pf_part_viia(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    SttmntsRgrdngActy_PhnNm = models.CharField(null=True, blank=True, max_length=10)
    # Line number: Part VII-A Line 14  Description: Books In Care Of - Phone Number  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/PhoneNum 

    SttmntsRgrdngActy_NwSbstntlCntrbtrsInd = models.TextField(null=True, blank=True)
    # Line number: Part VII-A Line 10  Description: New Substantial Contributors?  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/NewSubstantialContributorsInd 

    SttmntsRgrdngActy_WbstAddrssTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part VII-A Line 13  Description: Website Address  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/WebsiteAddressTxt 

    SttmntsRgrdngActy_NECTFlngInLOFFrm1041Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part VII-A Line 15  Description: Section 4947(a)(1) Nonexempt Charitable Trusts Filing in lieu of Form 1041  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/NECTFilingInLieuOFForm1041Ind 

    SttmntsRgrdngActy_Frm990TFldInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-A Line 4b  Description: Form 990-T Filed?  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/Form990TFiledInd 

    SttmntsRgrdngActy_IndvdlWthBksNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part VII-A Line 14  Description: Books In Care Of - Person Name  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/IndividualWithBooksNm 

    SttmntsRgrdngActy_MrThn100SpntInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-A Line 1b  Description: More Than $100 Spent?  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/MoreThan100SpentInd 

    LctnOfBksUSAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number: Part VII-A Line 14  Description:  City  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksUSAddress/CityNm 

    LctnOfBksFrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part VII-A Line 14  Description:  Address line 2  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksForeignAddress/AddressLine2Txt 

    SttmntsRgrdngActy_Sctn4955OrgnztnTxAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VII-A Line 1d(1)  Description: Section 4955 Tax on Organization  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/Section4955OrganizationTaxAmt 

    SttmntsRgrdngActy_PrvtOprtngFndtnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-A Line 9  Description: Private Operating Foundation?  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/PrivateOperatingFoundationInd 

    LctnOfBksUSAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number: Part VII-A Line 14  Description:  ZIP code  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksUSAddress/ZIPCd 

    SttmntsRgrdngActy_ChngsTArtclsOrBylwsInd = models.TextField(null=True, blank=True)
    # Line number: Part VII-A Line 3  Description: Changes to Articles or Bylaws?  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/ChangesToArticlesOrBylawsInd 

    LctnOfBksFrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number: Part VII-A Line 14  Description:  City  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksForeignAddress/CityNm 

    SttmntsRgrdngActy_DnrAdvsdFndInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-A Line 12  Description: Did Ihe organization acquire a direct or indirect interest in any applicable insurance contract?  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/DonorAdvisedFundInd 

    LctnOfBksFrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number: Part VII-A Line 14  Description:  Province or state  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksForeignAddress/ProvinceOrStateNm 

    SttmntsRgrdngActy_AtLst5000InAsstsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-A Line 7  Description: At least $5000 in Assets?  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/AtLeast5000InAssetsInd 

    PrsnsWthBksNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part VII-A Line 14  Description:  Business name line 2  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/PersonsWithBooksName/BusinessNameLine2Txt 

    SttmntsRgrdngActy_Sctn4955MngrsTxAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VII-A Line 1d(2)  Description: Section 4955 Tax on Managers  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/Section4955ManagersTaxAmt 

    SttmntsRgrdngActy_OwnCntrlldEnttyInd = models.TextField(null=True, blank=True)
    # Line number: Part VII-A Line 11  Description: At any time during the year, did the foundation, directly or indirectly, own a controlled entity within the meaning of section 51 2(b)(l3)?  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/OwnControlledEntityInd 

    SttmntsRgrdngActy_CmplyWthPblcInspRqrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-A Line 13  Description: Comply with Public Inspection Requirements?  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/ComplyWithPublicInspRqrInd 

    LctnOfBksFrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part VII-A Line 14  Description:  Address line 1  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksForeignAddress/AddressLine1Txt 

    SttmntsRgrdngActy_TxExmptIntrstAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VII-A Line 15  Description: Tax Exempt Interest Received  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/TaxExemptInterestAmt 

    SttmntsRgrdngActy_UnrltdBsIncmOvrLmtInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-A Line 4a  Description: Unrelated Business Income Over $1000?  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/UnrelatedBusIncmOverLimitInd 

    SttmntsRgrdngActy_Sctn508RqrStsfdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-A Line 6  Description: Requirements of Section 508(e)?  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/Section508eRqrSatisfiedInd 

    SttmntsRgrdngActy_TxRmbrsdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VII-A Line 1e  Description: Reimbursement of Tax  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/TaxReimbursedAmt 

    LctnOfBksFrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part VII-A Line 14  Description:  Country  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksForeignAddress/CountryCd 

    SttmntsRgrdngActy_ActvtsNtPrvslyRptInd = models.TextField(null=True, blank=True)
    # Line number: Part VII-A Line 2  Description: Activities Not Previously Reported?  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/ActivitiesNotPreviouslyRptInd 

    LctnOfBksUSAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part VII-A Line 14  Description:  Address line 1  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksUSAddress/AddressLine1Txt 

    SttmntsRgrdngActy_Frm990PFFldWthAttyGnInd = models.TextField(null=True, blank=True)
    # Line number: Part VII-A Line 8b  Description: Form 990-PF Filed with Attorney General?  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/Form990PFFiledWithAttyGenInd 

    SttmntsRgrdngActy_LgsltvPltclActyInd = models.TextField(null=True, blank=True)
    # Line number: Part VII-A Line 1a  Description: Legislative and Political Activities?  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/LegislativePoliticalActyInd 

    LctnOfBksUSAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part VII-A Line 14  Description:  Address line 2  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksUSAddress/AddressLine2Txt 

    LctnOfBksFrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number: Part VII-A Line 14  Description:  Postal code  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksForeignAddress/ForeignPostalCd 

    PrsnsWthBksNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part VII-A Line 14  Description:  Business name line 1  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/PersonsWithBooksName/BusinessNameLine1Txt 

    SttmntsRgrdngActy_OrgnztnDsslvdEtcInd = models.TextField(null=True, blank=True)
    # Line number: Part VII-A Line 5  Description: Termination, etc.?  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/OrganizationDissolvedEtcInd 

    LctnOfBksUSAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part VII-A Line 14  Description:  State  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/LocationOfBooksUSAddress/StateAbbreviationCd 

    SttmntsRgrdngActy_Frm1120POLFldInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-A Line 1c  Description: Form 1120-POL Filed?  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/Form1120POLFiledInd 

    SttmntsRgrdngActy_FrgnAccntsQstnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-A Line 16  Description: Interest or a signature or other authority over a bank, securities, or other financial account in a foreign country?  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/ForeignAccountsQuestionInd 

#######
#
# IRS990PF - PF Part VII-B Statements Regarding Activities for Which Form 4720 May Be Required 
#
#######

class pf_part_viib(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    UndstrbtdIncmPY4Yr = models.IntegerField(null=True, blank=True)
    # Line number: Part VII-B Line 2a  Description: Undistributed Income Prior Year 4  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistributedIncomePY4Yr 

    UndstrIncmSct49422AppYr4Yr = models.IntegerField(null=True, blank=True)
    # Line number: Part VII-B Line 2c  Description: Undistributed Income 4942(a)(2) Applied Year 4  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistrIncmSect4942a2AppYr4Yr 

    UndstrbtdIncmPYInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 2a  Description: Undistributed Income Prior Years?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistributedIncomePYInd 

    GrntsTOrgnztnsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 5a(4)  Description: Grants to Organizations?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/GrantsToOrganizationsInd 

    SbjTTxRmnrtnExPrchtPymtInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 8  Description: Subject to the section 4960 tax on remuneration or excess parachute payments?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/SubjToTaxRmnrtnExPrchtPymtInd 

    RlyngCrrntNtcDsstrAsstInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part VII-B Line 1b  Description: Relying on Current Notice of Disaster Assistance  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/RelyingCurrentNtcDsstrAsstInd 

    InflncElctnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 5a(2)  Description: Influence Election?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/InfluenceElectionInd 

    PrhbtdTxShltrTrnsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 7a  Description: Prohibited Tax Shelter Transaction?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/ProhibitedTaxShelterTransInd 

    PrcdsOrNtIncmInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 7b  Description: Proceeds Or Net Income?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/ProceedsOrNetIncomeInd 

    TrnsctnsFlTQlfyAsExcInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 5b  Description: Any Transactions Fail to Qualify as Exceptions?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/TransactionsFailToQlfyAsExcInd 

    BsnssHldngsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 3a  Description: Business Holdings?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/BusinessHoldingsInd 

    ExcssBsnssHldngsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 3b  Description: Excess Business Holdings?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/ExcessBusinessHoldingsInd 

    UncrrctdPYJprdyInvstInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 4b  Description: Uncorrected Jeopardy Investments?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/UncorrectedPYJeopardyInvstInd 

    PyPrmmsPrsnlBnftCntrctInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 6b  Description: Pay Premiums on a Personal Benefit Contract?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/PayPremiumsPrsnlBnftCntrctInd 

    MntndExpndtrRspnsInd = models.TextField(null=True, blank=True)
    # Line number: Part VII-B Line 5c  Description: Maintained Expenditure Responsibility?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/MaintainedExpenditureRspnsInd 

    UndstrIncmSct49422AppYr2Yr = models.IntegerField(null=True, blank=True)
    # Line number: Part VII-B Line 2c  Description: Undistributed Income 4942(a)(2) Applied Year 2  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistrIncmSect4942a2AppYr2Yr 

    UndstrIncmSct49422AppYr1Yr = models.IntegerField(null=True, blank=True)
    # Line number: Part VII-B Line 2c  Description: Undistributed Income 4942(a)(2) Applied Year 1  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistrIncmSect4942a2AppYr1Yr 

    UndstrIncmSct49422NtAppInd = models.TextField(null=True, blank=True)
    # Line number: Part VII-B Line 2b  Description: Undistributed Income 4942(a)(2) Not Applied?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistrIncmSect4942a2NotAppInd 

    BrrwOrLndDsqlfdPrsnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 1a(2)  Description: Borrow or Lend with a Disqualified Person?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/BrrwOrLendDisqualifiedPrsnInd 

    UncrrctdPrrActsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 1c  Description: Uncorrected Prior Acts?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/UncorrectedPriorActsInd 

    SlOrExchDsqlfdPrsnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 1a(1)  Description: Sale or Exchange with a Disqualified Person?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/SaleOrExchDisqualifiedPrsnInd 

    RlyngCrrntNtcDsstrAsst1Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part VII-B Line 5b  Description: Relying on Current Notice of Disaster Assistance  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/RelyingCurrentNtcDsstrAsst1Ind 

    UndstrbtdIncmPY3Yr = models.IntegerField(null=True, blank=True)
    # Line number: Part VII-B Line 2a  Description: Undistributed Income Prior Year 3  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistributedIncomePY3Yr 

    GrntsTIndvdlsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 5a(3)  Description: Grants to Individuals?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/GrantsToIndividualsInd 

    TrnsfrAstDsqlfdPrsnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 1a(5)  Description: Transfer Assets to a Disqualified Person?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/TransferAstDisqualifiedPrsnInd 

    InflncLgsltnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 5a(1)  Description: Influence Legislation?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/InfluenceLegislationInd 

    JprdyInvstmntsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 4a  Description: Jeopardy Investments?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/JeopardyInvestmentsInd 

    NnchrtblPrpsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 5a(5)  Description: Noncharitable Purpose?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/NoncharitablePurposeInd 

    PymntTGvrnmntOffclInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 1a(6)  Description: Payment to a Government Official?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/PaymentToGovernmentOfficialInd 

    FrnGdsDsqlfdPrsnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 1a(3)  Description: Furnished Goods, etc. with a Disqualified Person?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/FurnGoodsDisqualifiedPrsnInd 

    RcvFndsTPyPrsnlBnftCntrctInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 6a  Description: Receive Funds to Pay Premiums on a Personal Benefit Contract?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/RcvFndsToPayPrsnlBnftCntrctInd 

    PyCmpDsqlfdPrsnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 1a(4)  Description: Pay Compensation to a Disqualified Person?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/PayCompDisqualifiedPrsnInd 

    ActsFlTQlfyAsExcptnsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VII-B Line 1b  Description: Any Acts Fail to Qualify as Exceptions?  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/ActsFailToQlfyAsExceptionsInd 

    UndstrbtdIncmPY2Yr = models.IntegerField(null=True, blank=True)
    # Line number: Part VII-B Line 2a  Description: Undistributed Income Prior Year 2  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistributedIncomePY2Yr 

    UndstrbtdIncmPY1Yr = models.IntegerField(null=True, blank=True)
    # Line number: Part VII-B Line 2a  Description: Undistributed Income Prior Year 1  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistributedIncomePY1Yr 

    UndstrIncmSct49422AppYr3Yr = models.IntegerField(null=True, blank=True)
    # Line number: Part VII-B Line 2c  Description: Undistributed Income 4942(a)(2) Applied Year 3  most recent xpath: /IRS990PF/StatementsRegardingActy4720Grp/UndistrIncmSect4942a2AppYr3Yr 

#######
#
# IRS990PF - PF Part VIII Compensation 
#
#######

class pf_part_viii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    CmpOfHghstPdCntrctOrNONETxt = models.TextField(null=True, blank=True)
    # Line number: Part VIII Line 3  Description: If there are none, enter "None"  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompOfHghstPdCntrctOrNONETxt 

    CntrctrPdOvr50kCnt = models.TextField(null=True, blank=True)
    # Line number: Part VIII Line 3  Description: Total number of other contractors paid over $50,000  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/ContractorPaidOver50kCnt 

    CmpOfHghstPdEmplOrNONETxt = models.TextField(null=True, blank=True)
    # Line number: Part VIII Line 2  Description: If there are none, enter "None"  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompOfHghstPdEmplOrNONETxt 

    OthrEmplyPdOvr50kCnt = models.TextField(null=True, blank=True)
    # Line number: Part VIII Line 2  Description: Total number of other employees paid over $50,000  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OtherEmployeePaidOver50kCnt 

#######
#
# IRS990PF - PF Part IX-A Summary of Charitable Activities 
#
#######

class pf_part_ixa(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    Expnss4Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IX-A Line 4  Description: Expenses 4  most recent xpath: /IRS990PF/SummaryOfDirectChrtblActyGrp/Expenses4Amt 

    Dscrptn3Txt = models.TextField(null=True, blank=True)
    # Line number: Part IX-A Line 3  Description: Description 3  most recent xpath: /IRS990PF/SummaryOfDirectChrtblActyGrp/Description3Txt 

    Expnss3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IX-A Line 3  Description: Expenses 3  most recent xpath: /IRS990PF/SummaryOfDirectChrtblActyGrp/Expenses3Amt 

    Expnss1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IX-A Line 1  Description: Expenses 1  most recent xpath: /IRS990PF/SummaryOfDirectChrtblActyGrp/Expenses1Amt 

    Dscrptn1Txt = models.TextField(null=True, blank=True)
    # Line number: Part IX-A Line 1  Description: Description 1  most recent xpath: /IRS990PF/SummaryOfDirectChrtblActyGrp/Description1Txt 

    Dscrptn4Txt = models.TextField(null=True, blank=True)
    # Line number: Part IX-A Line 4  Description: Description 4  most recent xpath: /IRS990PF/SummaryOfDirectChrtblActyGrp/Description4Txt 

    Expnss2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IX-A Line 2  Description: Expenses 2  most recent xpath: /IRS990PF/SummaryOfDirectChrtblActyGrp/Expenses2Amt 

    Dscrptn2Txt = models.TextField(null=True, blank=True)
    # Line number: Part IX-A Line 2  Description: Description 2  most recent xpath: /IRS990PF/SummaryOfDirectChrtblActyGrp/Description2Txt 

#######
#
# IRS990PF - PF Part IX-B Summary of Program-Related Investments 
#
#######

class pf_part_ixb(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    Dscrptn2Txt = models.TextField(null=True, blank=True)
    # Line number: Part IX-B Line 2  Description: Description 2  most recent xpath: /IRS990PF/SumOfProgramRelatedInvstGrp/Description2Txt 

    AllOthrPrgrmRltdInvstTtAmt = models.TextField(null=True, blank=True)
    # Line number: Part IX-B Line 3  Description: All Other Program-Related Investments Total  most recent xpath: /IRS990PF/SumOfProgramRelatedInvstGrp/AllOtherProgramRltdInvstTotAmt 

    Expnss2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IX-B Line 2  Description: Amount 2  most recent xpath: /IRS990PF/SumOfProgramRelatedInvstGrp/Expenses2Amt 

    TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IX-B Total  Description: Total  most recent xpath: /IRS990PF/SumOfProgramRelatedInvstGrp/TotalAmt 

    Dscrptn1Txt = models.TextField(null=True, blank=True)
    # Line number: Part IX-B Line 1  Description: Description 1  most recent xpath: /IRS990PF/SumOfProgramRelatedInvstGrp/Description1Txt 

    Expnss1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IX-B Line 1  Description: Amount 1  most recent xpath: /IRS990PF/SumOfProgramRelatedInvstGrp/Expenses1Amt 

#######
#
# IRS990PF - PF Part X Minimum Investment Return 
#
#######

class pf_part_x(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    AvrgMnthlyCshBlncsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part X Line 1b  Description: Average Monthly Cash Balances  most recent xpath: /IRS990PF/MinimumInvestmentReturnGrp/AverageMonthlyCashBalancesAmt 

    RdctnClmdAmt = models.TextField(null=True, blank=True)
    # Line number: Part X Line 1e  Description: Reduction Claimed  most recent xpath: /IRS990PF/MinimumInvestmentReturnGrp/ReductionClaimedAmt 

    AdjstdTtlFMVOfUnsdAstAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part X Line 3  Description: Adjusted Total FMV of Unused Assets (subtract line 2 from line 1d)  most recent xpath: /IRS990PF/MinimumInvestmentReturnGrp/AdjustedTotalFMVOfUnusedAstAmt 

    AcqstnIndbtdnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part X Line 2  Description: Acquisition Indebtedness  most recent xpath: /IRS990PF/MinimumInvestmentReturnGrp/AcquisitionIndebtednessAmt 

    AvrgMnthlyFMVOfScAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part X Line 1a  Description: Average Monthly FMV of Securities  most recent xpath: /IRS990PF/MinimumInvestmentReturnGrp/AverageMonthlyFMVOfSecAmt 

    CshDmdChrtblAmt = models.TextField(null=True, blank=True)
    # Line number: Part X Line 4  Description: Cash Deemed Charitable  most recent xpath: /IRS990PF/MinimumInvestmentReturnGrp/CashDeemedCharitableAmt 

    FMVAllOthrNnchrtblAstAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part X Line 1c  Description: FMV of All Other Noncharitable Assets  most recent xpath: /IRS990PF/MinimumInvestmentReturnGrp/FMVAllOtherNoncharitableAstAmt 

    MnmmInvstmntRtrnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part X Line 6  Description: Minimum Investment Return  most recent xpath: /IRS990PF/MinimumInvestmentReturnGrp/MinimumInvestmentReturnAmt 

    TtlFMVOfUnsdAsstsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part X Line 1d  Description: Total FMV of Unused Assets  most recent xpath: /IRS990PF/MinimumInvestmentReturnGrp/TotalFMVOfUnusedAssetsAmt 

    NtVlNnchrtblAsstsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part X Line 5  Description: Net Noncharitable Assets  most recent xpath: /IRS990PF/MinimumInvestmentReturnGrp/NetVlNoncharitableAssetsAmt 

#######
#
# IRS990PF - PF Part XI Distributable Amount 
#
#######

class pf_part_xi(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    DstrbtblAsAdjstdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 7  Description: Distributable Amount as Adjusted  most recent xpath: /IRS990PF/DistributableAmountGrp/DistributableAsAdjustedAmt 

    MnmmInvstmntRtrnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 1  Description: Minimum Investment Return  most recent xpath: /IRS990PF/DistributableAmountGrp/MinimumInvestmentReturnAmt 

    TtlTxAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 2c  Description: Total Tax (add lines 2a and 2b)  most recent xpath: /IRS990PF/DistributableAmountGrp/TotalTaxAmt 

    DdctnFrmDstrbtblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 6  Description: Deduction from Distributable Amount  most recent xpath: /IRS990PF/DistributableAmountGrp/DeductionFromDistributableAmt 

    DstrbtblBfrAdjAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 3  Description: Distributable Amount Before Adjustments  most recent xpath: /IRS990PF/DistributableAmountGrp/DistributableBeforeAdjAmt 

    DstrbtblBfrDdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 5  Description: Distributable Amount Before Deduction (add lines 3 and 4)  most recent xpath: /IRS990PF/DistributableAmountGrp/DistributableBeforeDedAmt 

    TxBsdOnInvstmntIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 2a  Description: Tax Based on Investment Income  most recent xpath: /IRS990PF/DistributableAmountGrp/TaxBasedOnInvestmentIncomeAmt 

    Sct4942j3j5FndtnAndFrgnOrgInd = models.CharField(null=True, blank=True, max_length=1)
    # Description: Section 4942(j)(3)&(j)(5) Private Operating Foundations and Certain Foreign Organizations  most recent xpath: /IRS990PF/DistributableAmountGrp/Sect4942j3j5FndtnAndFrgnOrgInd 

    RcvrsQlfdDstrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 4  Description: Recoveries of Qualified Distributions  most recent xpath: /IRS990PF/DistributableAmountGrp/RecoveriesQualfiedDistriAmt 

    IncmTxAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 2b  Description: Income Tax for This Year  most recent xpath: /IRS990PF/DistributableAmountGrp/IncomeTaxAmt 

#######
#
# IRS990PF - PF Part XII Qualifying Distributions 
#
#######

class pf_part_xii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    PrgrmRltdInvstTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XII Line 1b  Description: Program Related Investments Total  most recent xpath: /IRS990PF/PFQualifyingDistributionsGrp/ProgramRelatedInvstTotalAmt 

    QlfyngDstrbtnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XII Line 4  Description: Qualifying Distributions  most recent xpath: /IRS990PF/PFQualifyingDistributionsGrp/QualifyingDistributionsAmt 

    ExpnssAndCntrbtnsAmt = models.TextField(null=True, blank=True)
    # Line number: Part XII Line 1a  Description: Expenses and Contributions  most recent xpath: /IRS990PF/PFQualifyingDistributionsGrp/ExpensesAndContributionsAmt 

    ChrtblAsstsAcqsPdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XII Line 2  Description: Amounts Paid to Acquire Charitable Assets  most recent xpath: /IRS990PF/PFQualifyingDistributionsGrp/CharitableAssetsAcquisPaidAmt 

    StAsdCshDstrTstAmt = models.TextField(null=True, blank=True)
    # Line number: Part XII Line 3b  Description: Amounts Set Aside - Cash Distribution Test  most recent xpath: /IRS990PF/PFQualifyingDistributionsGrp/SetAsideCashDistriTestAmt 

    StAsdStbltyTstAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XII Line 3a  Description: Amounts Set Aside - Suitability Test  most recent xpath: /IRS990PF/PFQualifyingDistributionsGrp/SetAsideSuitabilityTestAmt 

#######
#
# IRS990PF - PF Part XIII Undistributed Income 
#
#######

class pf_part_xiii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    UndstrbtdIncmPYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 2a(c)  Description: Undistributed Income Prior Year  most recent xpath: /IRS990PF/UndistributedIncomeGrp/UndistributedIncomePYAmt 

    ExcssDstrbtnCyvYr1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 3e  Description: Excess Distributions Carryover - Year 1  most recent xpath: /IRS990PF/UndistributedIncomeGrp/ExcessDistributionCyovYr1Amt 

    RmnngDstrFrmCrpsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 4e(a)  Description: Remaining Amount Distributed from Corpus  most recent xpath: /IRS990PF/UndistributedIncomeGrp/RemainingDistriFromCorpusAmt 

    ExcssDstrCyvTNxtYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 9(a)  Description: Excess Distribution Carryover to Next Year  most recent xpath: /IRS990PF/UndistributedIncomeGrp/ExcessDistriCyovToNextYrAmt 

    ExcssDstrbtnCyvYr3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 3c  Description: Excess Distributions Carryover - Year 3  most recent xpath: /IRS990PF/UndistributedIncomeGrp/ExcessDistributionCyovYr3Amt 

    UndstrbtdIncmCYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 6f(d)  Description: Undistributed Income for Current Year  most recent xpath: /IRS990PF/UndistributedIncomeGrp/UndistributedIncomeCYAmt 

    ExcssFrmYr1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 10d  Description: Excess from Year 1  most recent xpath: /IRS990PF/UndistributedIncomeGrp/ExcessFromYear1Amt 

    ExcssDstrbtnCyvAppCYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 5(d)  Description: Excess Distributions Carryover Applied to Current Year  most recent xpath: /IRS990PF/UndistributedIncomeGrp/ExcessDistributionCyovAppCYAmt 

    ExcssDstrbtnCyvYr5Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 3a  Description: Excess Distributions Carryover - Year 5  most recent xpath: /IRS990PF/UndistributedIncomeGrp/ExcessDistributionCyovYr5Amt 

    ExcssDstrbtnCyvYr2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 3d  Description: Excess Distributions Carryover - Year 2  most recent xpath: /IRS990PF/UndistributedIncomeGrp/ExcessDistributionCyovYr2Amt 

    Txbl2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 6e(c)  Description: Taxable Amount 2  most recent xpath: /IRS990PF/UndistributedIncomeGrp/Taxable2Amt 

    Txbl1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 6d(b)  Description: Taxable Amount 1  most recent xpath: /IRS990PF/UndistributedIncomeGrp/Taxable1Amt 

    ExcssFrmYr2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 10c  Description: Excess from Year 2  most recent xpath: /IRS990PF/UndistributedIncomeGrp/ExcessFromYear2Amt 

    ExcssDstrCyvFrmYr5Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 8(a)  Description: Excess Distribution Carryover from Year 5  most recent xpath: /IRS990PF/UndistributedIncomeGrp/ExcessDistriCyovFromYr5Amt 

    ExcssFrmYr4Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 10a  Description: Excess from Year 4  most recent xpath: /IRS990PF/UndistributedIncomeGrp/ExcessFromYear4Amt 

    PrrYr2Yr = models.IntegerField(null=True, blank=True)
    # Line number: Part XIII Line 2b  Description: Prior Year 2  most recent xpath: /IRS990PF/UndistributedIncomeGrp/PriorYear2Yr 

    DstrbtblAsAdjstdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 1(d)  Description: Distributable Amount as Adjusted  most recent xpath: /IRS990PF/UndistributedIncomeGrp/DistributableAsAdjustedAmt 

    CrpsDstr170b1EOr4942g3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 7(a)  Description: Treated as Distribution from Corpus to Satisfy Requirements Imposed by Section 170(b)(1)(E) or 4942(g)(3)  most recent xpath: /IRS990PF/UndistributedIncomeGrp/CorpusDistri170b1EOr4942g3Amt 

    ExcssDstrCyvAppCYCrpsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 5(a)  Description: Excess Distributions Carryover Applied to Current Year - Corpus  most recent xpath: /IRS990PF/UndistributedIncomeGrp/ExcessDistriCyovAppCYCorpusAmt 

    AppldTCrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 4d(d)  Description: Applied to Current Year  most recent xpath: /IRS990PF/UndistributedIncomeGrp/AppliedToCurrentYearAmt 

    AppldTYr1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 4a(c)  Description: Applied to Year 1  most recent xpath: /IRS990PF/UndistributedIncomeGrp/AppliedToYear1Amt 

    ExcssDstrbtnCyvYr4Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 3b  Description: Excess Distributions Carryover - Year 4  most recent xpath: /IRS990PF/UndistributedIncomeGrp/ExcessDistributionCyovYr4Amt 

    TtlCrpsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 6a(a)  Description: Total Corpus  most recent xpath: /IRS990PF/UndistributedIncomeGrp/TotalCorpusAmt 

    PrrYr3Yr = models.IntegerField(null=True, blank=True)
    # Line number: Part XIII Line 2b  Description: Prior Year 3  most recent xpath: /IRS990PF/UndistributedIncomeGrp/PriorYear3Yr 

    PrrYr1Yr = models.IntegerField(null=True, blank=True)
    # Line number: Part XIII Line 2b  Description: Prior Year 1  most recent xpath: /IRS990PF/UndistributedIncomeGrp/PriorYear1Yr 

    PrrYrUndstrbtdIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 6b(b)  Description: Prior Year's Undistributed Income  most recent xpath: /IRS990PF/UndistributedIncomeGrp/PriorYearUndistributedIncmAmt 

    TtlFrPrrYrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 2b(b)  Description: Total for Prior Years  most recent xpath: /IRS990PF/UndistributedIncomeGrp/TotalForPriorYearsAmt 

    AppldTPrrYrsAmt = models.TextField(null=True, blank=True)
    # Line number: Part XIII Line 4b(b)  Description: Applied to Prior Years  most recent xpath: /IRS990PF/UndistributedIncomeGrp/AppliedToPriorYearsAmt 

    QlfyngDstrbtnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 4  Description: Qualifying Distributions  most recent xpath: /IRS990PF/UndistributedIncomeGrp/QualifyingDistributionsAmt 

    TtlExcssDstrbtnCyvAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 3f(a)  most recent xpath: /IRS990PF/UndistributedIncomeGrp/TotalExcessDistributionCyovAmt 

    ExcssFrmYr3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 10b  Description: Excess from Year 3  most recent xpath: /IRS990PF/UndistributedIncomeGrp/ExcessFromYear3Amt 

    ExcssFrmCrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 10e  Description: Excess from Current Year  most recent xpath: /IRS990PF/UndistributedIncomeGrp/ExcessFromCurrentYearAmt 

    PrrYrDfcncyOrTxAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XIII Line 6c(b)  Description: Prior Year's Deficiency or Tax  most recent xpath: /IRS990PF/UndistributedIncomeGrp/PriorYearDeficiencyOrTaxAmt 

    TrtdAsDstrFrmCrpsAmt = models.TextField(null=True, blank=True)
    # Line number: Part XIII Line 4c(a)  Description: Treated as Distribution from Corpus  most recent xpath: /IRS990PF/UndistributedIncomeGrp/TreatedAsDistriFromCorpusAmt 

#######
#
# IRS990PF - PF Part XIV Private Operating Foundations 
#
#######

class pf_part_xiv(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    TtlAssts_Yr2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (c)  Description:  Year 2  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsGrp/Year2Amt 

    TtlAssts_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (e)  Description:  Total  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsGrp/TotalAmt 

    TtlAsstsSct4942j3B_Yr1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (b)  Description:  Year 1  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsSect4942j3BiGrp/Year1Amt 

    PblcSpprt_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (e)  Description:  Total  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/PublicSupportType/TotalAmt 

    QlfyngDstrMdDrt_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (e)  Description:  Total  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriMadeDrtGrp/TotalAmt 

    PrvtOprtngFndtns_Sctn4942j3Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part XIV Line 1b  Description: Section 4942(j)(3)  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/Section4942j3Ind 

    QlfyngDstrbtns_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (e)  Description:  Total  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistributionsGrp/TotalAmt 

    TtlSpprt_Yr2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (c)  Description:  Year 2  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalSupportGrp/Year2Amt 

    GrssInvstmntIncm_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (a)  Description:  Current Year  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/GrossInvestmentIncomeGrp/CurrentYearAmt 

    LssrAdjNtIncmMnInvstRt_Yr2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (c)  Description:  Year 2  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LessorAdjNetIncmMinInvstRetGrp/Year2Amt 

    TtlAssts_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (a)  Description:  Current Year  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsGrp/CurrentYearAmt 

    PblcSpprt_Yr3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (d)  Description:  Year 3  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/PublicSupportType/Year3Amt 

    TwThrdsMnmmInvstRt_Yr3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (d)  Description:  Year 3  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TwoThirdsMinimumInvstRetGrp/Year3Amt 

    QlfyngDstrbtns_Yr3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (d)  Description:  Year 3  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistributionsGrp/Year3Amt 

    TwThrdsMnmmInvstRt_Yr1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (b)  Description:  Year 1  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TwoThirdsMinimumInvstRetGrp/Year1Amt 

    QlfyngDstrNtUsdDrt_Yr2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (c)  Description:  Year 2  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriNotUsedDrtGrp/Year2Amt 

    TtlAsstsSct4942j3B_Yr2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (c)  Description:  Year 2  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsSect4942j3BiGrp/Year2Amt 

    GrssInvstmntIncm_Yr3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (d)  Description:  Year 3  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/GrossInvestmentIncomeGrp/Year3Amt 

    LssrAdjNtIncmMnInvstRt_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (e)  Description:  Total  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LessorAdjNetIncmMinInvstRetGrp/TotalAmt 

    GrssInvstmntIncm_Yr1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (b)  Description:  Year 1  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/GrossInvestmentIncomeGrp/Year1Amt 

    TtlAssts_Yr1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (b)  Description:  Year 1  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsGrp/Year1Amt 

    Pct85LssrAdjIncmOrMnRt_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (e)  Description:  Total  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/Pct85LessorAdjIncmOrMinRetGrp/TotalAmt 

    LrgstSpprtFrmEO_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (e)  Description:  Total  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LargestSupportFromEOGrp/TotalAmt 

    PblcSpprt_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (a)  Description:  Current Year  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/PublicSupportType/CurrentYearAmt 

    PrvtOprtngFndtns_PrvtOprtngFndtnRlngDt = models.CharField(null=True, blank=True, max_length=31)
    # Line number: Part XIV Line 1a  Description: Date of Ruling  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/PrivateOperatingFndtnRulingDt 

    PrvtOprtngFndtns_Sctn4942j5Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part XIV Line 1b  Description: Section 4942(j)(5)  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/Section4942j5Ind 

    QlfyngDstrMdDrt_Yr1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (b)  Description:  Year 1  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriMadeDrtGrp/Year1Amt 

    QlfyngDstrNtUsdDrt_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (a)  Description:  Current Year  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriNotUsedDrtGrp/CurrentYearAmt 

    TwThrdsMnmmInvstRt_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (e)  Description:  Total  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TwoThirdsMinimumInvstRetGrp/TotalAmt 

    LrgstSpprtFrmEO_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (a)  Description:  Current Year  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LargestSupportFromEOGrp/CurrentYearAmt 

    GrssInvstmntIncm_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (e)  Description:  Total  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/GrossInvestmentIncomeGrp/TotalAmt 

    Pct85LssrAdjIncmOrMnRt_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (a)  Description:  Current Year  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/Pct85LessorAdjIncmOrMinRetGrp/CurrentYearAmt 

    LssrAdjNtIncmMnInvstRt_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (a)  Description:  Current Year  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LessorAdjNetIncmMinInvstRetGrp/CurrentYearAmt 

    Pct85LssrAdjIncmOrMnRt_Yr3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (d)  Description:  Year 3  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/Pct85LessorAdjIncmOrMinRetGrp/Year3Amt 

    TtlSpprt_Yr3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (d)  Description:  Year 3  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalSupportGrp/Year3Amt 

    TtlSpprt_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (e)  Description:  Total  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalSupportGrp/TotalAmt 

    LrgstSpprtFrmEO_Yr3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (d)  Description:  Year 3  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LargestSupportFromEOGrp/Year3Amt 

    PblcSpprt_Yr2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (c)  Description:  Year 2  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/PublicSupportType/Year2Amt 

    QlfyngDstrbtns_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (a)  Description:  Current Year  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistributionsGrp/CurrentYearAmt 

    LssrAdjNtIncmMnInvstRt_Yr1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (b)  Description:  Year 1  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LessorAdjNetIncmMinInvstRetGrp/Year1Amt 

    QlfyngDstrNtUsdDrt_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (e)  Description:  Total  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriNotUsedDrtGrp/TotalAmt 

    QlfyngDstrNtUsdDrt_Yr1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (b)  Description:  Year 1  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriNotUsedDrtGrp/Year1Amt 

    Pct85LssrAdjIncmOrMnRt_Yr1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (b)  Description:  Year 1  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/Pct85LessorAdjIncmOrMinRetGrp/Year1Amt 

    LrgstSpprtFrmEO_Yr1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (b)  Description:  Year 1  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LargestSupportFromEOGrp/Year1Amt 

    QlfyngDstrMdDrt_Yr3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (d)  Description:  Year 3  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriMadeDrtGrp/Year3Amt 

    LrgstSpprtFrmEO_Yr2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (c)  Description:  Year 2  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LargestSupportFromEOGrp/Year2Amt 

    TtlSpprt_Yr1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (b)  Description:  Year 1  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalSupportGrp/Year1Amt 

    PblcSpprt_Yr1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (b)  Description:  Year 1  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/PublicSupportType/Year1Amt 

    LssrAdjNtIncmMnInvstRt_Yr3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (d)  Description:  Year 3  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/LessorAdjNetIncmMinInvstRetGrp/Year3Amt 

    QlfyngDstrMdDrt_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (a)  Description:  Current Year  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriMadeDrtGrp/CurrentYearAmt 

    Pct85LssrAdjIncmOrMnRt_Yr2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (c)  Description:  Year 2  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/Pct85LessorAdjIncmOrMinRetGrp/Year2Amt 

    QlfyngDstrNtUsdDrt_Yr3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (d)  Description:  Year 3  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriNotUsedDrtGrp/Year3Amt 

    QlfyngDstrMdDrt_Yr2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (c)  Description:  Year 2  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistriMadeDrtGrp/Year2Amt 

    QlfyngDstrbtns_Yr1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (b)  Description:  Year 1  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistributionsGrp/Year1Amt 

    TtlAsstsSct4942j3B_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (e)  Description:  Total  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsSect4942j3BiGrp/TotalAmt 

    GrssInvstmntIncm_Yr2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (c)  Description:  Year 2  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/GrossInvestmentIncomeGrp/Year2Amt 

    TtlAsstsSct4942j3B_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (a)  Description:  Current Year  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsSect4942j3BiGrp/CurrentYearAmt 

    TtlAssts_Yr3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (d)  Description:  Year 3  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsGrp/Year3Amt 

    TtlAsstsSct4942j3B_Yr3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (d)  Description:  Year 3  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalAssetsSect4942j3BiGrp/Year3Amt 

    TtlSpprt_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (a)  Description:  Current Year  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TotalSupportGrp/CurrentYearAmt 

    TwThrdsMnmmInvstRt_Yr2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (c)  Description:  Year 2  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TwoThirdsMinimumInvstRetGrp/Year2Amt 

    TwThrdsMnmmInvstRt_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (a)  Description:  Current Year  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/TwoThirdsMinimumInvstRetGrp/CurrentYearAmt 

    QlfyngDstrbtns_Yr2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  column (c)  Description:  Year 2  most recent xpath: /IRS990PF/PrivateOperatingFoundationsGrp/QualifyingDistributionsGrp/Year2Amt 

#######
#
# IRS990PF - PF Part XV Supplementary Information 
#
#######

class pf_part_xv(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    TtlGrntOrCntrApprvFtAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XV Line 3b Total  Description: Total Grant or Contribution Approved for Future Payment  most recent xpath: /IRS990PF/SupplementaryInformationGrp/TotalGrantOrContriApprvFutAmt 

    TtlGrntOrCntrPdDrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XV Line 3a Total  Description: Total Grant or Contribution Paid During Year  most recent xpath: /IRS990PF/SupplementaryInformationGrp/TotalGrantOrContriPdDurYrAmt 

    OnlyCntrTPrslctdInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part XV Line 2  Description: Only Contributes to Preselected Charitable Organizations  most recent xpath: /IRS990PF/SupplementaryInformationGrp/OnlyContriToPreselectedInd 

#######
#
# IRS990PF - PF Part XVI-A Analysis of Income-Producing Activities 
#
#######

class pf_part_xvia(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    OthrInvstmntIncmPrtVII_RltdOrExmptFnctnIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherInvestmentIncomeGrp/RelatedOrExemptFunctionIncmAmt 

    SbttlsIncmPrdcngActy_RltdOrExmptFnctnIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/SubtotalsIncmProducingActyGrp/RelatedOrExemptFunctionIncmAmt 

    NtIncmLssFrmSpclEvt_RltdOrExmptFnctnIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetIncomeLossFromSpecialEvtGrp/RelatedOrExemptFunctionIncmAmt 

    DvAndIntFrmScPrtVII_BsnssCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/DividendsAndInterestFromSecDtl/BusinessCd 

    DvAndIntFrmScPrtVII_UnrltdBsnssTxblIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/DividendsAndInterestFromSecDtl/UnrelatedBusinessTaxblIncmAmt 

    DvAndIntFrmScPrtVII_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/DividendsAndInterestFromSecDtl/ExclusionAmt 

    NtRntlIncmRNtDbtFncdPrp_UnrltdBsnssTxblIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReNotDebtFincdProp/UnrelatedBusinessTaxblIncmAmt 

    NtRntlIncmRNtDbtFncdPrp_RltdOrExmptFnctnIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReNotDebtFincdProp/RelatedOrExemptFunctionIncmAmt 

    NtRntlIncmRDbtFncdPrp_ExclsnCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReDebtFincdPropGrp/ExclusionCd 

    IntOnSvAndTmpCshInvst_ExclsnCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/IntOnSavAndTempCashInvstGrp/ExclusionCd 

    OthrInvstmntIncmPrtVII_UnrltdBsnssTxblIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherInvestmentIncomeGrp/UnrelatedBusinessTaxblIncmAmt 

    DvAndIntFrmScPrtVII_RltdOrExmptFnctnIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/DividendsAndInterestFromSecDtl/RelatedOrExemptFunctionIncmAmt 

    NtRntlIncmRDbtFncdPrp_BsnssCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReDebtFincdPropGrp/BusinessCd 

    OthrInvstmntIncmPrtVII_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherInvestmentIncomeGrp/ExclusionAmt 

    NtIncmLssFrmSpclEvt_ExclsnCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetIncomeLossFromSpecialEvtGrp/ExclusionCd 

    IntOnSvAndTmpCshInvst_RltdOrExmptFnctnIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/IntOnSavAndTempCashInvstGrp/RelatedOrExemptFunctionIncmAmt 

    SbttlsIncmPrdcngActy_UnrltdBsnssTxblIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/SubtotalsIncmProducingActyGrp/UnrelatedBusinessTaxblIncmAmt 

    FsCntrctsFrmGvtAg_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/FeesContractsFromGovtAgGrp/ExclusionAmt 

    MmbrshpDsAndAssmnt_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/MembershipDuesAndAssmntGrp/ExclusionAmt 

    MmbrshpDsAndAssmnt_BsnssCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/MembershipDuesAndAssmntGrp/BusinessCd 

    GnSlsAstOthThnInvntry_ExclsnCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GainSalesAstOthThanInvntryGrp/ExclusionCd 

    GnSlsAstOthThnInvntry_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GainSalesAstOthThanInvntryGrp/ExclusionAmt 

    NtRntlIncmRNtDbtFncdPrp_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReNotDebtFincdProp/ExclusionAmt 

    IntOnSvAndTmpCshInvst_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/IntOnSavAndTempCashInvstGrp/ExclusionAmt 

    DvAndIntFrmScPrtVII_ExclsnCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/DividendsAndInterestFromSecDtl/ExclusionCd 

    NtRntlIncmRNtDbtFncdPrp_BsnssCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReNotDebtFincdProp/BusinessCd 

    GrssPrftLssSlsOfInvntry_UnrltdBsnssTxblIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GrossProfitLossSlsOfInvntryGrp/UnrelatedBusinessTaxblIncmAmt 

    OthrInvstmntIncmPrtVII_BsnssCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherInvestmentIncomeGrp/BusinessCd 

    NtRntlIncmRNtDbtFncdPrp_ExclsnCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReNotDebtFincdProp/ExclusionCd 

    MmbrshpDsAndAssmnt_UnrltdBsnssTxblIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/MembershipDuesAndAssmntGrp/UnrelatedBusinessTaxblIncmAmt 

    MmbrshpDsAndAssmnt_RltdOrExmptFnctnIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/MembershipDuesAndAssmntGrp/RelatedOrExemptFunctionIncmAmt 

    GrssPrftLssSlsOfInvntry_RltdOrExmptFnctnIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GrossProfitLossSlsOfInvntryGrp/RelatedOrExemptFunctionIncmAmt 

    NtRntlIncmRDbtFncdPrp_UnrltdBsnssTxblIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReDebtFincdPropGrp/UnrelatedBusinessTaxblIncmAmt 

    SbttlsIncmPrdcngActy_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/SubtotalsIncmProducingActyGrp/ExclusionAmt 

    FsCntrctsFrmGvtAg_ExclsnCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/FeesContractsFromGovtAgGrp/ExclusionCd 

    NtRntlIncmPrsnlPrp_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRentalIncomePersonalPropGrp/ExclusionAmt 

    FsCntrctsFrmGvtAg_RltdOrExmptFnctnIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/FeesContractsFromGovtAgGrp/RelatedOrExemptFunctionIncmAmt 

    NtIncmLssFrmSpclEvt_UnrltdBsnssTxblIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetIncomeLossFromSpecialEvtGrp/UnrelatedBusinessTaxblIncmAmt 

    NtIncmLssFrmSpclEvt_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetIncomeLossFromSpecialEvtGrp/ExclusionAmt 

    NtRntlIncmPrsnlPrp_UnrltdBsnssTxblIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRentalIncomePersonalPropGrp/UnrelatedBusinessTaxblIncmAmt 

    NtRntlIncmRDbtFncdPrp_RltdOrExmptFnctnIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReDebtFincdPropGrp/RelatedOrExemptFunctionIncmAmt 

    GnSlsAstOthThnInvntry_UnrltdBsnssTxblIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GainSalesAstOthThanInvntryGrp/UnrelatedBusinessTaxblIncmAmt 

    GnSlsAstOthThnInvntry_RltdOrExmptFnctnIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GainSalesAstOthThanInvntryGrp/RelatedOrExemptFunctionIncmAmt 

    FsCntrctsFrmGvtAg_UnrltdBsnssTxblIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/FeesContractsFromGovtAgGrp/UnrelatedBusinessTaxblIncmAmt 

    AnlyssIncmPrdcngActy_TtlIncmPrdcngActyAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XVI-A Line 13  Description: Total (add line 104, columns (B), (D), and (E))  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/TotalIncomeProducingActyAmt 

    GrssPrftLssSlsOfInvntry_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GrossProfitLossSlsOfInvntryGrp/ExclusionAmt 

    NtIncmLssFrmSpclEvt_BsnssCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetIncomeLossFromSpecialEvtGrp/BusinessCd 

    NtRntlIncmPrsnlPrp_ExclsnCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRentalIncomePersonalPropGrp/ExclusionCd 

    FsCntrctsFrmGvtAg_BsnssCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/FeesContractsFromGovtAgGrp/BusinessCd 

    IntOnSvAndTmpCshInvst_BsnssCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/IntOnSavAndTempCashInvstGrp/BusinessCd 

    NtRntlIncmPrsnlPrp_RltdOrExmptFnctnIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRentalIncomePersonalPropGrp/RelatedOrExemptFunctionIncmAmt 

    GnSlsAstOthThnInvntry_BsnssCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GainSalesAstOthThanInvntryGrp/BusinessCd 

    GrssPrftLssSlsOfInvntry_BsnssCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GrossProfitLossSlsOfInvntryGrp/BusinessCd 

    MmbrshpDsAndAssmnt_ExclsnCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/MembershipDuesAndAssmntGrp/ExclusionCd 

    GrssPrftLssSlsOfInvntry_ExclsnCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/GrossProfitLossSlsOfInvntryGrp/ExclusionCd 

    NtRntlIncmPrsnlPrp_BsnssCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRentalIncomePersonalPropGrp/BusinessCd 

    NtRntlIncmRDbtFncdPrp_ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/NetRntlIncmReDebtFincdPropGrp/ExclusionAmt 

    OthrInvstmntIncmPrtVII_ExclsnCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherInvestmentIncomeGrp/ExclusionCd 

    IntOnSvAndTmpCshInvst_UnrltdBsnssTxblIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/IntOnSavAndTempCashInvstGrp/UnrelatedBusinessTaxblIncmAmt 

#######
#
# IRS990PF - PF Part XVII Transfers, Transactions Relationships With Noncharitable Exempt Organizations 
#
#######

class pf_part_xvii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    ShrngOfFcltsEtcInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part XVII Line 1c  Description: Other transactions : Sharing of facilities, equipment, mailing lists, other assets, or paid employees  most recent xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/SharingOfFacilitiesEtcInd 

    RntlOfFcltsOthAsstsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part XVII Line 1b(3)  Description: Other transactions : Rental of facilities, equipment, or other assets  most recent xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/RentalOfFacilitiesOthAssetsInd 

    TrnsfrOthrAsstNnchrtblEOInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part XVII Line 1a(2)  Description: Transfers of other assets to noncharitable EO  most recent xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/TrnsfrOtherAssetNonchrtblEOInd 

    SlsOrExchngsOfAsstsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part XVII Line 1b(1)  Description: Other transactions : Sales or exchanges of assets with a noncharitable exempt organization  most recent xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/SalesOrExchangesOfAssetsInd 

    PrchsOfAsstsNnchrtblEOInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part XVII Line 1b(2)  Description: Other transactions : Purchases of assets from a noncharitable exempt organization  most recent xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/PurchaseOfAssetsNonchrtblEOInd 

    TrnsfrOfCshTNnchrtblEOInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part XVII Line 1a(1)  Description: Transfers of cash to noncharitable EO  most recent xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/TrnsfrOfCashToNonchrtblEOInd 

    RmbrsmntArrngmntsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part XVII Line 1b(4)  Description: Other transactions : Reimbursement arrangements  most recent xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/ReimbursementArrangementsInd 

    PrfrmncOfSrvcsEtcInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part XVII Line 1b(6)  Description: Other transactions : Performance of Services or membership or fundraising solicitations  most recent xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/PerformanceOfServicesEtcInd 

    LnsOrLnGrntsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part XVII Line 1b(5)  Description: Other transactions : Loans or loan guarantees  most recent xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/LoansOrLoanGuaranteesInd 

    RltnshpsNnchrtblEOInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part XVII Line 2a  Description: Relationships with noncharitable EOs  most recent xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/RelationshipsNonchrtblEOInd 

#######
#
# IRS990PF - PFSpclCndtnDsc - Special condition description
# A repeating structure from pf_part_0
#
#######

class PFSpclCndtnDsc(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    SpclCndtnDsc = models.TextField(null=True, blank=True)
    # Description: Special condition description  most recent xpath: /IRS990PF/SpecialConditionDesc 

#######
#
# IRS990PF - PFCpGnsLssTxInvstIncm
# A repeating structure from pf_part_iv
#
#######

class PFCpGnsLssTxInvstIncm(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    HwAcqrdCd = models.TextField(null=True, blank=True)
    # Line number: Part IV Line 1(b)  Description: How Acquired  most recent xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/HowAcquiredCd 

    GnOrLssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IV Line 1(h)  Description: Gain or Loss  most recent xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/GainOrLossAmt 

    CstOrOthrBssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IV Line 1(g)  Description: Cost or Other Basis  most recent xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/CostOrOtherBasisAmt 

    PrprtyDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part IV Line 1(a)  Description: Description of Asset  most recent xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/PropertyDesc 

    ExcssFMVOvrAdjstdBssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IV Line 1(k)  Description: Excess of FMV Over Adjusted Basis  most recent xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/ExcessFMVOverAdjustedBssAmt 

    FMVAsOf123169Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IV Line 1(i)  Description: FMV as of 12/31/69  most recent xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/FMVAsOf123169Amt 

    AcqrdDt = models.CharField(null=True, blank=True, max_length=31)
    # Line number: Part IV Line 1(c)  Description: Date Acquired  most recent xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/AcquiredDt 

    SldDt = models.CharField(null=True, blank=True, max_length=31)
    # Line number: Part IV Line 1(d)  Description: Date Sold  most recent xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/SoldDt 

    GnsMnsExcssOrLsssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IV Line 1(l)  Description: Gains Minus Excess or Losses  most recent xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/GainsMinusExcessOrLossesAmt 

    GrssSlsPrcAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IV Line 1(e)  Description: Gross Sales Price  most recent xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/GrossSalesPriceAmt 

    DprctnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IV Line 1(f)  Description: Depreciation  most recent xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/DepreciationAmt 

    AdjstdBssAsOf123169Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IV Line 1(j)  Description: Adjusted Basis as of 12/31/69  most recent xpath: /IRS990PF/CapGainsLossTxInvstIncmDetail/CapGainsLossTxInvstIncmGrp/AdjustedBasisAsOf123169Amt 

#######
#
# IRS990PF - PFFrgnCntryCd - Name of foreign country
# A repeating structure from pf_part_viia
#
#######

class PFFrgnCntryCd(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FrgnCntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part VII-A Line 16  Description: Name of foreign country  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/ForeignCountryCd 

#######
#
# IRS990PF - PFOrgRprtOrRgstrSttCd - States Filed With
# A repeating structure from pf_part_viia
#
#######

class PFOrgRprtOrRgstrSttCd(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    OrgRprtOrRgstrSttCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part VII-A Line 8a  Description: States Filed With  most recent xpath: /IRS990PF/StatementsRegardingActyGrp/OrgReportOrRegisterStateCd 

#######
#
# IRS990PF - PFCmpnstnHghstPdEmpl - Compensation of the five highest paid employees other than officers, directors, and trustees
# A repeating structure from pf_part_viii
#
#######

class PFCmpnstnHghstPdEmpl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    CmpnstnHghstPdEmpl_TtlTxt = models.CharField(null=True, blank=True, max_length=20)
    # Line number:  Part VIII Line 2(b)  Description:  Title  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/TitleTxt 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VIII Line 2(a)  Description:  Address line 2  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/USAddress/AddressLine2Txt 

    CmpnstnHghstPdEmpl_AvrgHrsPrWkDvtdTPsRt = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 2(b)  Description:  Average hours per week  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/AverageHrsPerWkDevotedToPosRt 

    CmpnstnHghstPdEmpl_CmpnstnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Line 2(c)  Description:  Compensation  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/CompensationAmt 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VIII Line 2(a)  Description:  Address line 1  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/USAddress/AddressLine1Txt 

    FrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 2(a)  Description:  City  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/ForeignAddress/CityNm 

    CmpnstnHghstPdEmpl_EmplyBnftsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Line 2(d)  Description:  Employee benefits  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/EmployeeBenefitsAmt 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number:  Part VIII Line 2(a)  Description:  City  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/USAddress/CityNm 

    FrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VIII Line 2(a)  Description:  Address line 2  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part VIII Line 2(a)  Description:  Country  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/ForeignAddress/CountryCd 

    FrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VIII Line 2(a)  Description:  Address line 1  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 2(a)  Description:  Postal code  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/ForeignAddress/ForeignPostalCd 

    CmpnstnHghstPdEmpl_ExpnsAccntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Line 2(e)  Description:  Expense Account  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/ExpenseAccountAmt 

    FrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 2(a)  Description:  Province or state  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/ForeignAddress/ProvinceOrStateNm 

    CmpnstnHghstPdEmpl_PrsnNm = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 2(a)  Description:  Highest paid employee's name  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/PersonNm 

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number:  Part VIII Line 2(a)  Description:  ZIP code  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/USAddress/ZIPCd 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part VIII Line 2(a)  Description:  State  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationHighestPaidEmplGrp/USAddress/StateAbbreviationCd 

#######
#
# IRS990PF - PFCmpnstnOfHghstPdCntrct - Compensation of the five highest paid independent contractors for professional services
# A repeating structure from pf_part_viii
#
#######

class PFCmpnstnOfHghstPdCntrct(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 3(a)  Description:  Province or state  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/ForeignAddress/ProvinceOrStateNm 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part VIII Line 3(a)  Description:  State  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/USAddress/StateAbbreviationCd 

    FrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 3(a)  Description:  City  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/ForeignAddress/CityNm 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VIII Line 3(a)  Description:  Address line 1  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/USAddress/AddressLine1Txt 

    CmpnstnOfHghstPdCntrct_PrsnNm = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 3(a)  Description:  Highest paid contractor's name - Person  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/PersonNm 

    CmpnstnOfHghstPdCntrct_SrvcTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part VIII Line 3(b)  Description:  Type of service  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/ServiceTypeTxt 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VIII Line 3(a)  Description:  Address line 2  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/USAddress/AddressLine2Txt 

    CmpnstnOfHghstPdCntrct_BsnssNm = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 3(a)  Description:  Highest paid contractor's name - Business  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/BusinessName 

    CmpnstnOfHghstPdCntrct_BsnssNmLn1 = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 3(a)  Description:  Highest paid contractor's name - Business Name ine 1  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/BusinessName/BusinessNameLine1 

    CmpnstnOfHghstPdCntrct_BsnssNmLn1 = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 3(a)  Description:  Highest paid contractor's name - Business Name ine 1  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/BusinessName/BusinessNameLine1Txt 

    CmpnstnOfHghstPdCntrct_BsnssNmLn2 = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 3(a)  Description:  Highest paid contractor's name - Business Name line 2  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/BusinessName/BusinessNameLine2 

    CmpnstnOfHghstPdCntrct_BsnssNmLn2 = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 3(a)  Description:  Highest paid contractor's name - Business Name line 2  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/BusinessName/BusinessNameLine2Txt 

    CmpnstnOfHghstPdCntrct_CmpnstnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Line 3(c)  Description:  Compensation  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/CompensationAmt 

    FrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part VIII Line 3(a)  Description:  Country  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/ForeignAddress/CountryCd 

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number:  Part VIII Line 3(a)  Description:  ZIP code  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/USAddress/ZIPCd 

    FrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 3(a)  Description:  Postal code  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/ForeignAddress/ForeignPostalCd 

    FrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VIII Line 3(a)  Description:  Address line 2  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/ForeignAddress/AddressLine2Txt 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number:  Part VIII Line 3(a)  Description:  City  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/USAddress/CityNm 

    FrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VIII Line 3(a)  Description:  Address line 1  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/CompensationOfHghstPdCntrctGrp/ForeignAddress/AddressLine1Txt 

#######
#
# IRS990PF - PFOffcrDrTrstKyEmpl - Officer, Director, Trustee, or Key Employee
# A repeating structure from pf_part_viii
#
#######

class PFOffcrDrTrstKyEmpl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    OffcrDrTrstKyEmpl_CmpnstnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Line 1(c)  Description:  Compensation  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/CompensationAmt 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part VIII Line 1(a)  Description:  State  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/USAddress/StateAbbreviationCd 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number:  Part VIII Line 1(a)  Description:  City  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/USAddress/CityNm 

    OffcrDrTrstKyEmpl_ExpnsAccntOthrAllwncAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Line 1(e)  Description:  Expense account and other allowances  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/ExpenseAccountOtherAllwncAmt 

    OffcrDrTrstKyEmpl_PrsnNm = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 1(a)  Description:  Person Name  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/PersonNm 

    FrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 1(a)  Description:  Province or state  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/ForeignAddress/ProvinceOrStateNm 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VIII Line 1(a)  Description:  Address line 1  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/USAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VIII Line 1(a)  Description:  Address line 2  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/ForeignAddress/AddressLine2Txt 

    OffcrDrTrstKyEmpl_BsnssNmLn1 = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 1(a)  Description:  Business Name line 1  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/BusinessName/BusinessNameLine1 

    OffcrDrTrstKyEmpl_BsnssNmLn1 = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 1(a)  Description:  Business Name line 1  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/BusinessName/BusinessNameLine1Txt 

    OffcrDrTrstKyEmpl_BsnssNmLn2 = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 1(a)  Description:  Business Name line 2  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/BusinessName/BusinessNameLine2 

    OffcrDrTrstKyEmpl_BsnssNmLn2 = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 1(a)  Description:  Business Name line 2  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/BusinessName/BusinessNameLine2Txt 

    FrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VIII Line 1(a)  Description:  Address line 1  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 1(a)  Description:  Postal code  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/ForeignAddress/ForeignPostalCd 

    OffcrDrTrstKyEmpl_AvrgHrsPrWkDvtdTPsRt = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 1(b)  Description:  Average Hours per week devoted to position  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/AverageHrsPerWkDevotedToPosRt 

    OffcrDrTrstKyEmpl_BsnssNm = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 1(a)  Description:  Business Name  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/BusinessName 

    OffcrDrTrstKyEmpl_EmplyBnftPrgrmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VIII Line 1(d)  Description:  Contributions to employee benefit plans and deferred compensation  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/EmployeeBenefitProgramAmt 

    FrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part VIII Line 1(a)  Description:  Country  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/ForeignAddress/CountryCd 

    OffcrDrTrstKyEmpl_TtlTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part VIII Line 1(b)  Description:  Title  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/TitleTxt 

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number:  Part VIII Line 1(a)  Description:  ZIP code  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/USAddress/ZIPCd 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part VIII Line 1(a)  Description:  Address line 2  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/USAddress/AddressLine2Txt 

    FrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number:  Part VIII Line 1(a)  Description:  City  most recent xpath: /IRS990PF/OfficerDirTrstKeyEmplInfoGrp/OfficerDirTrstKeyEmplGrp/ForeignAddress/CityNm 

#######
#
# IRS990PF - PFApplctnSbmssnInf
# A repeating structure from pf_part_xv
#
#######

class PFApplctnSbmssnInf(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    RcpntFrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number: Part XV Line 2a  Description:  Province or state  most recent xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientForeignAddress/ProvinceOrStateNm 

    RcpntUSAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part XV Line 2a  Description:  Address line 1  most recent xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientUSAddress/AddressLine1Txt 

    ApplctnSbmssnInf_FrmAndInfAndMtrlsTxt = models.TextField(null=True, blank=True)
    # Line number: Part XV Line 2b  Description: Form and Information and Materials To Include  most recent xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/FormAndInfoAndMaterialsTxt 

    ApplctnSbmssnInf_RstrctnsOnAwrdsTxt = models.TextField(null=True, blank=True)
    # Line number: Part XV Line 2d  Description: Restrictions on Awards  most recent xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RestrictionsOnAwardsTxt 

    RcpntUSAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part XV Line 2a  Description:  State  most recent xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientUSAddress/StateAbbreviationCd 

    RcpntUSAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part XV Line 2a  Description:  Address line 2  most recent xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientUSAddress/AddressLine2Txt 

    ApplctnSbmssnInf_RcpntPrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part XV Line 2a  Description: Name of Person to Receive Applications  most recent xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientPersonNm 

    RcpntUSAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number: Part XV Line 2a  Description:  ZIP code  most recent xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientUSAddress/ZIPCd 

    ApplctnSbmssnInf_RcpntEmlAddrssTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part XV Line 2a  Description: Recipient Email Address  most recent xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientEmailAddressTxt 

    RcpntFrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number: Part XV Line 2a  Description:  City  most recent xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientForeignAddress/CityNm 

    ApplctnSbmssnInf_SbmssnDdlnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part XV Line 2c  Description: Subsmission Deadlines  most recent xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/SubmissionDeadlinesTxt 

    RcpntFrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part XV Line 2a  Description:  Address line 2  most recent xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientForeignAddress/AddressLine2Txt 

    RcpntFrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number: Part XV Line 2a  Description:  Postal code  most recent xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientForeignAddress/ForeignPostalCd 

    RcpntFrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part XV Line 2a  Description:  Address line 1  most recent xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientForeignAddress/AddressLine1Txt 

    RcpntFrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part XV Line 2a  Description:  Country  most recent xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientForeignAddress/CountryCd 

    RcpntUSAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number: Part XV Line 2a  Description:  City  most recent xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientUSAddress/CityNm 

    ApplctnSbmssnInf_RcpntPhnNm = models.CharField(null=True, blank=True, max_length=10)
    # Line number: Part XV Line 2a  Description: Phone Number of Person to Receive Applications  most recent xpath: /IRS990PF/SupplementaryInformationGrp/ApplicationSubmissionInfoGrp/RecipientPhoneNum 

#######
#
# IRS990PF - PFCntrbtngMngrNm - Contributing Manager
# A repeating structure from pf_part_xv
#
#######

class PFCntrbtngMngrNm(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    CntrbtngMngrNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part XV Line 1a  Description: Contributing Manager  most recent xpath: /IRS990PF/SupplementaryInformationGrp/ContributingManagerNm 

#######
#
# IRS990PF - PFGrntOrCntrApprvFrFt
# A repeating structure from pf_part_xv
#
#######

class PFGrntOrCntrApprvFrFt(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    RcpntUSAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part XV Line 3b  Description:  Address line 1  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientUSAddress/AddressLine1Txt 

    GrntOrCntrApprvFrFt_RcpntPrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part XV Line 3b  Description:  Recipient Person Name  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientPersonNm 

    GrntOrCntrApprvFrFt_RcpntRltnshpTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part XV Line 3b  Description:  Recipient Relationship to Foundation Manager or Substantial Contributor  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientRelationshipTxt 

    RcpntUSAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part XV Line 3b  Description:  State  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientUSAddress/StateAbbreviationCd 

    RcpntFrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part XV Line 3b  Description:  Address line 2  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientForeignAddress/AddressLine2Txt 

    RcpntBsnssNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part XV Line 3b  Description:  Business name line 2  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientBusinessName/BusinessNameLine2Txt 

    RcpntFrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number: Part XV Line 3b  Description:  Postal code  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientForeignAddress/ForeignPostalCd 

    RcpntUSAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number: Part XV Line 3b  Description:  City  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientUSAddress/CityNm 

    RcpntFrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part XV Line 3b  Description:  Country  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientForeignAddress/CountryCd 

    RcpntFrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number: Part XV Line 3b  Description:  Province or state  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientForeignAddress/ProvinceOrStateNm 

    GrntOrCntrApprvFrFt_Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XV Line 3b  Description:  Amount  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/Amt 

    RcpntFrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part XV Line 3b  Description:  Address line 1  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientForeignAddress/AddressLine1Txt 

    RcpntUSAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number: Part XV Line 3b  Description:  ZIP code  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientUSAddress/ZIPCd 

    RcpntUSAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part XV Line 3b  Description:  Address line 2  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientUSAddress/AddressLine2Txt 

    GrntOrCntrApprvFrFt_GrntOrCntrbtnPrpsTxt = models.TextField(null=True, blank=True)
    # Line number: Part XV Line 3b  Description:  Purpose of Grant or Contribution  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/GrantOrContributionPurposeTxt 

    RcpntFrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number: Part XV Line 3b  Description:  City  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientForeignAddress/CityNm 

    RcpntBsnssNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part XV Line 3b  Description:  Business name line 1  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientBusinessName/BusinessNameLine1Txt 

    GrntOrCntrApprvFrFt_RcpntFndtnSttsTxt = models.CharField(null=True, blank=True, max_length=20)
    # Line number: Part XV Line 3b  Description:  Recipient's Foundation Status  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContriApprvForFutGrp/RecipientFoundationStatusTxt 

#######
#
# IRS990PF - PFGrntOrCntrbtnPdDrYr
# A repeating structure from pf_part_xv
#
#######

class PFGrntOrCntrbtnPdDrYr(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    RcpntFrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part XV Line 3a  Description:  Address line 1  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientForeignAddress/AddressLine1Txt 

    RcpntFrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number: Part XV Line 3a  Description:  City  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientForeignAddress/CityNm 

    RcpntBsnssNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part XV Line 3a  Description:  Business name line 1  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientBusinessName/BusinessNameLine1Txt 

    RcpntFrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part XV Line 3a  Description:  Country  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientForeignAddress/CountryCd 

    RcpntUSAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part XV Line 3a  Description:  State  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientUSAddress/StateAbbreviationCd 

    GrntOrCntrbtnPdDrYr_RcpntPrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part XV Line 3a  Description:  Recipient Person Name  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientPersonNm 

    RcpntUSAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part XV Line 3a  Description:  Address line 1  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientUSAddress/AddressLine1Txt 

    GrntOrCntrbtnPdDrYr_Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XV Line 3a  Description:  Amount  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/Amt 

    RcpntBsnssNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part XV Line 3a  Description:  Business name line 2  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientBusinessName/BusinessNameLine2Txt 

    RcpntFrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part XV Line 3a  Description:  Address line 2  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientForeignAddress/AddressLine2Txt 

    RcpntUSAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part XV Line 3a  Description:  Address line 2  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientUSAddress/AddressLine2Txt 

    RcpntUSAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number: Part XV Line 3a  Description:  ZIP code  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientUSAddress/ZIPCd 

    GrntOrCntrbtnPdDrYr_GrntOrCntrbtnPrpsTxt = models.TextField(null=True, blank=True)
    # Line number: Part XV Line 3a  Description:  Purpose of Grant or Contribution  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/GrantOrContributionPurposeTxt 

    RcpntUSAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number: Part XV Line 3a  Description:  City  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientUSAddress/CityNm 

    RcpntFrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number: Part XV Line 3a  Description:  Province or state  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientForeignAddress/ProvinceOrStateNm 

    RcpntFrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number: Part XV Line 3a  Description:  Postal code  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientForeignAddress/ForeignPostalCd 

    GrntOrCntrbtnPdDrYr_RcpntFndtnSttsTxt = models.CharField(null=True, blank=True, max_length=20)
    # Line number: Part XV Line 3a  Description:  Recipient's Foundation Status  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientFoundationStatusTxt 

    GrntOrCntrbtnPdDrYr_RcpntRltnshpTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part XV Line 3a  Description:  Recipient Relationship to Foundation Manager or Substantial Contributor  most recent xpath: /IRS990PF/SupplementaryInformationGrp/GrantOrContributionPdDurYrGrp/RecipientRelationshipTxt 

#######
#
# IRS990PF - PFShrhldrMngrNm - Shareholder Manager
# A repeating structure from pf_part_xv
#
#######

class PFShrhldrMngrNm(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    ShrhldrMngrNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part XV Line 1b  Description: Shareholder Manager  most recent xpath: /IRS990PF/SupplementaryInformationGrp/ShareholderManagerNm 

#######
#
# IRS990PF - PFOthrRvnDscrbd
# A repeating structure from pf_part_xvia
#
#######

class PFOthrRvnDscrbd(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    UnrltdBsnssTxblIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherRevenueDescribedGrp/UnrelatedBusinessTaxblIncmAmt 

    RltdOrExmptFnctnIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherRevenueDescribedGrp/RelatedOrExemptFunctionIncmAmt 

    ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherRevenueDescribedGrp/ExclusionAmt 

    BsnssCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherRevenueDescribedGrp/BusinessCd 

    ExclsnCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherRevenueDescribedGrp/ExclusionCd 

    Dsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part XVI-A Line 11  Description:  Description  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/OtherRevenueDescribedGrp/Desc 

#######
#
# IRS990PF - PFPrgrmSrvcRvPrtVII
# A repeating structure from pf_part_xvia
#
#######

class PFPrgrmSrvcRvPrtVII(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    BsnssCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (A)  Description:  Business code  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/ProgramServiceRevenueDtl/BusinessCd 

    ExclsnCd = models.TextField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (C)  Description:  Exclusion code (01 through 43)  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/ProgramServiceRevenueDtl/ExclusionCd 

    ExclsnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (D)  Description:  Excluded by section 512, 513, or 514: Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/ProgramServiceRevenueDtl/ExclusionAmt 

    Dsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part XVI-A Line 1  Description:  Description  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/ProgramServiceRevenueDtl/Desc 

    RltdOrExmptFnctnIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (E)  Description:  Related or exempt function income  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/ProgramServiceRevenueDtl/RelatedOrExemptFunctionIncmAmt 

    UnrltdBsnssTxblIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVI-A - Column (B)  Description:  Amount  most recent xpath: /IRS990PF/AnalysisIncomeProducingActyGrp/ProgramServiceRevenueDtl/UnrelatedBusinessTaxblIncmAmt 

#######
#
# IRS990PF - PFRlnOfActyTAccmOfExmptPrps - Relationship of activities to the accomplishment of exempt purposes
# A repeating structure from pf_part_xvib
#
#######

class PFRlnOfActyTAccmOfExmptPrps(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    LnNmbrTxt = models.TextField(null=True, blank=True)
    # Line number: Part XVI-B  Description:  Line number  most recent xpath: /IRS990PF/RlnOfActyToAccomOfExmptPrpsGrp/RlnOfActyToAccomOfExmptPrpsGrp/LineNumberTxt 

    RltnshpSttmntTxt = models.TextField(null=True, blank=True)
    # Line number: Part XVI-B  Description:  Relationship statement  most recent xpath: /IRS990PF/RlnOfActyToAccomOfExmptPrpsGrp/RlnOfActyToAccomOfExmptPrpsGrp/RelationshipStatementTxt 

#######
#
# IRS990PF - PFRltnshpSkdDtl
# A repeating structure from pf_part_xvii
#
#######

class PFRltnshpSkdDtl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    OrgnztnDsc = models.CharField(null=True, blank=True, max_length=20)
    # Line number:  Part XVII Line 2b Column (b)  Description:  Type of organization  most recent xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/RelationshipScheduleDetail/OrganizationTypeDesc 

    BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part XVII Line 2b Column (a)  Description:  Business name line 2  most recent xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/RelationshipScheduleDetail/OrganizationBusinessName/BusinessNameLine2Txt 

    BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part XVII Line 2b Column (a)  Description:  Business name line 1  most recent xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/RelationshipScheduleDetail/OrganizationBusinessName/BusinessNameLine1Txt 

    RltnshpDscrptnTxt = models.TextField(null=True, blank=True)
    # Line number:  Part XVII Line 2b Column (c)  Description:  Description of relationship  most recent xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/RelationshipScheduleDetail/RelationshipDescriptionTxt 

#######
#
# IRS990PF - PFTrnsfrSkdDtl
# A repeating structure from pf_part_xvii
#
#######

class PFTrnsfrSkdDtl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part XVII Line 1d Column (c)  Description:  Business name line 2  most recent xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/TransferScheduleDetail/NoncharitableExemptOrgName/BusinessNameLine2Txt 

    LnNmbrTxt = models.TextField(null=True, blank=True)
    # Line number:  Part XVII Line 1d Column (a)  Description:  Line number  most recent xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/TransferScheduleDetail/LineNumberTxt 

    InvlvdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part XVII Line 1d Column (b)  Description:  Amount involved  most recent xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/TransferScheduleDetail/InvolvedAmt 

    BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part XVII Line 1d Column (c)  Description:  Business name line 1  most recent xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/TransferScheduleDetail/NoncharitableExemptOrgName/BusinessNameLine1Txt 

    TrnsfrsTrnsAndShrArrngmDsc = models.TextField(null=True, blank=True)
    # Line number:  Part XVII Line 1d Column (d)  Description:  Description of transfers, transactions, and sharing arrangements  most recent xpath: /IRS990PF/TrnsfrTransRlnNonchrtblEOGrp/TransferScheduleDetail/TransfersTransAndShrArrngmDesc 

#######
#
# IRS990ScheduleA - ScheduleA Part I Reason for Non-Private Foundation Status 
#
#######

class skeda_part_i(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    SchlInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 2  Description: A school. Section 170(b)(1)(A)(ii)  most recent xpath: /IRS990ScheduleA/SchoolInd 

    SpprtngOrgnztn5093Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 12  Description: Supporting organization 509(a)(3)  most recent xpath: /IRS990ScheduleA/SupportingOrganization509a3Ind 

    GvrnmntlUntInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 6  Description: A Federal, state, or local government or governmental unit. Section 170(b)(1)(A)(v)  most recent xpath: /IRS990ScheduleA/GovernmentalUnitInd 

    PblclySpprtdOrg5092Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 10  Description: Publicly supported organization 509(a)(2)  most recent xpath: /IRS990ScheduleA/PubliclySupportedOrg509a2Ind 

    SpprtdOrgnztnsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 12f  Description: Number of supported organizations  most recent xpath: /IRS990ScheduleA/SupportedOrganizationsCnt 

    CllgOrgnztnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 5  Description: An organization operated for the benefit of a college or university owned or operated by a governmental unit. Section 170(b)(1)(A)(iv).  most recent xpath: /IRS990ScheduleA/CollegeOrganizationInd 

    CmmntyTrstInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 8  Description: A community trust. Section 170(b)(1)(A)(vi)  most recent xpath: /IRS990ScheduleA/CommunityTrustInd 

    MdclRsrchOrgnztnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 4  Description: A medical research organization operated in conjunction with a hospital. Section 170(b)(1)(A)(iii)  most recent xpath: /IRS990ScheduleA/MedicalResearchOrganizationInd 

    AgrcltrlRsrchOrgInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 9  Description: An agricultural research organization operated in conjunction with college or university. Section 170(b)(1)(A)(ix)  most recent xpath: /IRS990ScheduleA/AgriculturalResearchOrgInd 

    TstPblcSftyInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 11  Description: An organization organized and operated to test for public safety. Section 509(a)(4)  most recent xpath: /IRS990ScheduleA/TestPublicSafetyInd 

    OthrSpprtSmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 12g(vi) Total  Description: Sum of amounts of other support  most recent xpath: /IRS990ScheduleA/OtherSupportSumAmt 

    SpprtngOrg2Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 12b  Description: Supporting organization 509(a)(3) - Type 2  most recent xpath: /IRS990ScheduleA/SupportingOrgType2Ind 

    SpprtSmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 12g(v), Total  Description: Sum of amounts of support  most recent xpath: /IRS990ScheduleA/SupportSumAmt 

    SpprtdOrgnztnsTtlCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 12g(i), Total  Description: Total number of supported organizations  most recent xpath: /IRS990ScheduleA/SupportedOrganizationsTotalCnt 

    SpprtngOrg3FncIntInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 12c  Description: Supporting organization 509(a)(3) - Type 3 functionally integrated  most recent xpath: /IRS990ScheduleA/SupportingOrgType3FuncIntInd 

    SpprtngOrg3NnFncInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 12d  Description: Supporting organization 509(a)(3) - Type 3 Non-functionally integrated  most recent xpath: /IRS990ScheduleA/SupportingOrgType3NonFuncInd 

    PblcOrgnztn170Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 7  Description: An organization that normally receives a substantial part of its support from a governmental unit or from the general public. 			Section 170(b)(1)(A)(vi)  most recent xpath: /IRS990ScheduleA/PublicOrganization170Ind 

    ChrchInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 1  Description: A church, convention of churches, or association of churches. Section 170(b)(1)(A)(i)  most recent xpath: /IRS990ScheduleA/ChurchInd 

    SpprtngOrg1Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 12a  Description: Supporting organization 509(a)(3) - Type 1  most recent xpath: /IRS990ScheduleA/SupportingOrgType1Ind 

    IRSWrttnDtrmntnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 12e  Description: Does the organization have a written determination from the IRS that it is a Type I, Type II or Type III supporting organization?  most recent xpath: /IRS990ScheduleA/IRSWrittenDeterminationInd 

    HsptlInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 3  Description: A hospital or a cooperative hospital service organization. Section 170(b)(1)(A)(iii)  most recent xpath: /IRS990ScheduleA/HospitalInd 

#######
#
# IRS990ScheduleA - ScheduleA Part II Support Schedule for Organizations described in IRC 170(b)(1)(A)(iv) and 170(b)(1)(A)(vi) 
#
#######

class skeda_part_ii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    UnrltdBsnssNtIncm170_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/UnrelatedBusinessNetIncm170Grp/TotalAmt 

    GvtFrnSrvcFcltsVl170_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl170Grp/CurrentTaxYearMinus2YearsAmt 

    GvtFrnSrvcFcltsVl170_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl170Grp/CurrentTaxYearMinus1YearAmt 

    UnrltdBsnssNtIncm170_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/UnrelatedBusinessNetIncm170Grp/CurrentTaxYearMinus4YearsAmt 

    SkdA_ThrtyThrPctSprtTstsCY170Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part II Line 16a  Description: Thirty three and one third test for the current year  most recent xpath: /IRS990ScheduleA/ThirtyThrPctSuprtTestsCY170Ind 

    OthrIncm170_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/OtherIncome170Grp/CurrentTaxYearMinus1YearAmt 

    GvtFrnSrvcFcltsVl170_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl170Grp/CurrentTaxYearMinus3YearsAmt 

    GvtFrnSrvcFcltsVl170_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl170Grp/CurrentTaxYearAmt 

    TxRvLvdOrgnztnlBnft170_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft170Grp/CurrentTaxYearMinus2YearsAmt 

    SkdA_TnPctFctsCrcmstncsTstPYInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part II Line 17b  Description: Ten percent facts and circumstances test for the prior year  most recent xpath: /IRS990ScheduleA/TenPctFactsCrcmstncsTestPYInd 

    SkdA_PblcSpprtTtl170Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 6(f)  Description: Public Support Total  most recent xpath: /IRS990ScheduleA/PublicSupportTotal170Amt 

    TxRvLvdOrgnztnlBnft170_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft170Grp/CurrentTaxYearMinus4YearsAmt 

    SkdA_ThrtyThrPctSprtTstsPY170Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part II Line 16b  Description: Thirty three and one third test for the prior year  most recent xpath: /IRS990ScheduleA/ThirtyThrPctSuprtTestsPY170Ind 

    GftsGrntsCntrRcvd170_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/GiftsGrantsContriRcvd170Grp/TotalAmt 

    UnrltdBsnssNtIncm170_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/UnrelatedBusinessNetIncm170Grp/CurrentTaxYearMinus1YearAmt 

    GftsGrntsCntrRcvd170_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/GiftsGrantsContriRcvd170Grp/CurrentTaxYearAmt 

    SkdA_SbstntlCntrbtrsTtAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 5(f)  Description: Amounts from substantial contributors total  most recent xpath: /IRS990ScheduleA/SubstantialContributorsTotAmt 

    GftsGrntsCntrRcvd170_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/GiftsGrantsContriRcvd170Grp/CurrentTaxYearMinus4YearsAmt 

    TtlClndrYr170_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/TotalCalendarYear170Grp/CurrentTaxYearMinus1YearAmt 

    GrssInvstmntIncm170_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/GrossInvestmentIncome170Grp/CurrentTaxYearMinus1YearAmt 

    UnrltdBsnssNtIncm170_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/UnrelatedBusinessNetIncm170Grp/CurrentTaxYearMinus2YearsAmt 

    TtlClndrYr170_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/TotalCalendarYear170Grp/TotalAmt 

    SkdA_TnPctFctsCrcmstncsTstCYInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part II Line 17a  Description: Ten percent facts and circumstances test for the current year  most recent xpath: /IRS990ScheduleA/TenPctFactsCrcmstncsTestCYInd 

    TtlClndrYr170_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/TotalCalendarYear170Grp/CurrentTaxYearMinus2YearsAmt 

    GftsGrntsCntrRcvd170_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/GiftsGrantsContriRcvd170Grp/CurrentTaxYearMinus3YearsAmt 

    GrssInvstmntIncm170_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/GrossInvestmentIncome170Grp/CurrentTaxYearMinus3YearsAmt 

    TxRvLvdOrgnztnlBnft170_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft170Grp/CurrentTaxYearMinus1YearAmt 

    TtlClndrYr170_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/TotalCalendarYear170Grp/CurrentTaxYearMinus3YearsAmt 

    SkdA_PblcSpprtCY170Pct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number: Part II Line 14  Description: Public support percentage (line 6 column (f) divided by line 12 column (f)  most recent xpath: /IRS990ScheduleA/PublicSupportCY170Pct 

    TxRvLvdOrgnztnlBnft170_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft170Grp/CurrentTaxYearMinus3YearsAmt 

    UnrltdBsnssNtIncm170_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/UnrelatedBusinessNetIncm170Grp/CurrentTaxYearMinus3YearsAmt 

    GvtFrnSrvcFcltsVl170_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl170Grp/CurrentTaxYearMinus4YearsAmt 

    UnrltdBsnssNtIncm170_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/UnrelatedBusinessNetIncm170Grp/CurrentTaxYearAmt 

    TxRvLvdOrgnztnlBnft170_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft170Grp/TotalAmt 

    OthrIncm170_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/OtherIncome170Grp/TotalAmt 

    TtlClndrYr170_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/TotalCalendarYear170Grp/CurrentTaxYearAmt 

    OthrIncm170_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/OtherIncome170Grp/CurrentTaxYearMinus2YearsAmt 

    GrssInvstmntIncm170_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/GrossInvestmentIncome170Grp/CurrentTaxYearMinus2YearsAmt 

    SkdA_Frst5Yrs170Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part II Line 13  Description: First five years  most recent xpath: /IRS990ScheduleA/First5Years170Ind 

    OthrIncm170_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/OtherIncome170Grp/CurrentTaxYearMinus4YearsAmt 

    GrssInvstmntIncm170_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/GrossInvestmentIncome170Grp/CurrentTaxYearMinus4YearsAmt 

    SkdA_TtlSpprtAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 11(f)  Description: Total support  most recent xpath: /IRS990ScheduleA/TotalSupportAmt 

    GftsGrntsCntrRcvd170_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/GiftsGrantsContriRcvd170Grp/CurrentTaxYearMinus1YearAmt 

    GvtFrnSrvcFcltsVl170_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl170Grp/TotalAmt 

    OthrIncm170_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/OtherIncome170Grp/CurrentTaxYearMinus3YearsAmt 

    TtlClndrYr170_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/TotalCalendarYear170Grp/CurrentTaxYearMinus4YearsAmt 

    TxRvLvdOrgnztnlBnft170_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft170Grp/CurrentTaxYearAmt 

    SkdA_GrssRcptsRltdActvtsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 12  Description: Gross receipts from admissions, merchandise sold or services performed, or furnishing of facilities in any activity that is related to the organization's tax-exempt purpose  most recent xpath: /IRS990ScheduleA/GrossReceiptsRltdActivitiesAmt 

    GrssInvstmntIncm170_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/GrossInvestmentIncome170Grp/CurrentTaxYearAmt 

    SkdA_PrvtFndtn170Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part II Line 18  Description: If the organization did not check a box on line 13, 16a, 16b, 17a or 17b, check this box and see instructions  most recent xpath: /IRS990ScheduleA/PrivateFoundation170Ind 

    OthrIncm170_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/OtherIncome170Grp/CurrentTaxYearAmt 

    SkdA_PblcSpprtPY170Pct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number: Part II Line 15  Description: Public support percentage from prior year's Schedule A, Part II, line 14  most recent xpath: /IRS990ScheduleA/PublicSupportPY170Pct 

    GftsGrntsCntrRcvd170_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/GiftsGrantsContriRcvd170Grp/CurrentTaxYearMinus2YearsAmt 

    GrssInvstmntIncm170_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/GrossInvestmentIncome170Grp/TotalAmt 

#######
#
# IRS990ScheduleA - ScheduleA Part III Support Schedule for Organizations described in IRC 509(a)(2) 
#
#######

class skeda_part_iii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    NtIncmFrmOthrUBI_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/NetIncomeFromOtherUBIGrp/CurrentTaxYearMinus2YearsAmt 

    AmntsRcvdDsqlfyPrsn_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/AmountsRcvdDsqlfyPersonGrp/CurrentTaxYearMinus3YearsAmt 

    SbstAndDsqlfyPrsnsTt_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/SubstAndDsqlfyPrsnsTotGrp/CurrentTaxYearMinus1YearAmt 

    GrssRcptsAdmssns_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/GrossReceiptsAdmissionsGrp/CurrentTaxYearMinus4YearsAmt 

    GrssRcptsAdmssns_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/GrossReceiptsAdmissionsGrp/CurrentTaxYearAmt 

    SbstntlCntrbtrsAmt_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/SubstantialContributorsAmtGrp/CurrentTaxYearAmt 

    GrssInvstmntIncm509_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/GrossInvestmentIncome509Grp/CurrentTaxYearMinus4YearsAmt 

    NtIncmFrmOthrUBI_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/NetIncomeFromOtherUBIGrp/CurrentTaxYearMinus1YearAmt 

    GftsGrntsCntrsRcvd509_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/GiftsGrantsContrisRcvd509Grp/CurrentTaxYearMinus2YearsAmt 

    SkdA_PblcSpprtTtl509Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Line 8(f)  Description: Public support total  most recent xpath: /IRS990ScheduleA/PublicSupportTotal509Amt 

    SbstntlCntrbtrsAmt_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/SubstantialContributorsAmtGrp/CurrentTaxYearMinus1YearAmt 

    OthrIncm509_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/OtherIncome509Grp/CurrentTaxYearAmt 

    SkdA_PrvtFndtn509Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part III Line 20  Description: Private Foundation. If the organization did not check the box on either line 14, 19a or 19b, check this box and see instructions  most recent xpath: /IRS990ScheduleA/PrivateFoundation509Ind 

    InvstmntIncmAndUBTI_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/InvestmentIncomeAndUBTIGrp/CurrentTaxYearMinus4YearsAmt 

    GrssInvstmntIncm509_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/GrossInvestmentIncome509Grp/CurrentTaxYearMinus2YearsAmt 

    SkdA_PblcSpprtPY509Pct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number: Part III Line 16  Description: Public support percentage from prior year's Schedule A, Part III, line 14a  most recent xpath: /IRS990ScheduleA/PublicSupportPY509Pct 

    TtlSpprtClndrYr_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/TotalSupportCalendarYearGrp/CurrentTaxYearMinus1YearAmt 

    SbstAndDsqlfyPrsnsTt_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/SubstAndDsqlfyPrsnsTotGrp/CurrentTaxYearMinus2YearsAmt 

    OthrIncm509_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/OtherIncome509Grp/TotalAmt 

    Pst1975UBTI_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/Post1975UBTIGrp/TotalAmt 

    AmntsRcvdDsqlfyPrsn_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/AmountsRcvdDsqlfyPersonGrp/TotalAmt 

    TtlSpprtClndrYr_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/TotalSupportCalendarYearGrp/CurrentTaxYearMinus2YearsAmt 

    SbstAndDsqlfyPrsnsTt_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/SubstAndDsqlfyPrsnsTotGrp/CurrentTaxYearMinus4YearsAmt 

    TtlSpprtClndrYr_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/TotalSupportCalendarYearGrp/CurrentTaxYearAmt 

    GrssRcptsAdmssns_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/GrossReceiptsAdmissionsGrp/CurrentTaxYearMinus2YearsAmt 

    GrssRcptsAdmssns_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/GrossReceiptsAdmissionsGrp/CurrentTaxYearMinus3YearsAmt 

    NtIncmFrmOthrUBI_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/NetIncomeFromOtherUBIGrp/CurrentTaxYearMinus3YearsAmt 

    GvtFrnSrvcFcltsVl509_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl509Grp/CurrentTaxYearMinus2YearsAmt 

    TxRvLvdOrgnztnlBnft509_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft509Grp/TotalAmt 

    GvtFrnSrvcFcltsVl509_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl509Grp/TotalAmt 

    GftsGrntsCntrsRcvd509_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/GiftsGrantsContrisRcvd509Grp/CurrentTaxYearAmt 

    GrssInvstmntIncm509_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/GrossInvestmentIncome509Grp/TotalAmt 

    Ttl509_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/Total509Grp/CurrentTaxYearMinus4YearsAmt 

    GvtFrnSrvcFcltsVl509_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl509Grp/CurrentTaxYearMinus3YearsAmt 

    TtlSpprtClndrYr_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/TotalSupportCalendarYearGrp/CurrentTaxYearMinus4YearsAmt 

    OthrIncm509_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/OtherIncome509Grp/CurrentTaxYearMinus3YearsAmt 

    InvstmntIncmAndUBTI_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/InvestmentIncomeAndUBTIGrp/CurrentTaxYearMinus3YearsAmt 

    AmntsRcvdDsqlfyPrsn_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/AmountsRcvdDsqlfyPersonGrp/CurrentTaxYearMinus1YearAmt 

    Ttl509_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/Total509Grp/TotalAmt 

    SkdA_ThrtyThrPctSprtTstsCY509Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part III Line 19a  Description: 33.33 % Tests - Current Year. If the organization did not check the box on line17, and line 14a is more than 33.33% and line 15a is less than 33.33%, check this box and stop here  most recent xpath: /IRS990ScheduleA/ThirtyThrPctSuprtTestsCY509Ind 

    Pst1975UBTI_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/Post1975UBTIGrp/CurrentTaxYearMinus4YearsAmt 

    InvstmntIncmAndUBTI_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/InvestmentIncomeAndUBTIGrp/TotalAmt 

    SbstAndDsqlfyPrsnsTt_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/SubstAndDsqlfyPrsnsTotGrp/CurrentTaxYearAmt 

    Pst1975UBTI_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/Post1975UBTIGrp/CurrentTaxYearMinus2YearsAmt 

    TtlSpprtClndrYr_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/TotalSupportCalendarYearGrp/TotalAmt 

    TxRvLvdOrgnztnlBnft509_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft509Grp/CurrentTaxYearMinus2YearsAmt 

    GftsGrntsCntrsRcvd509_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/GiftsGrantsContrisRcvd509Grp/CurrentTaxYearMinus4YearsAmt 

    GrssRcptsNnUnrltBs_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/GrossReceiptsNonUnrltBusGrp/TotalAmt 

    Pst1975UBTI_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/Post1975UBTIGrp/CurrentTaxYearMinus3YearsAmt 

    SbstntlCntrbtrsAmt_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/SubstantialContributorsAmtGrp/CurrentTaxYearMinus4YearsAmt 

    SkdA_ThrtyThrPctSprtTstsPY509Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part III Line 19b  Description: 33.33 % Tests - Prior Year. If the organization did not check the boxes on line 17 and line 18, and line 14b is more than 33.33% and line 15a is less than 33.33%, check this box and stop here  most recent xpath: /IRS990ScheduleA/ThirtyThrPctSuprtTestsPY509Ind 

    GrssRcptsAdmssns_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/GrossReceiptsAdmissionsGrp/CurrentTaxYearMinus1YearAmt 

    GrssRcptsNnUnrltBs_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/GrossReceiptsNonUnrltBusGrp/CurrentTaxYearMinus3YearsAmt 

    SbstAndDsqlfyPrsnsTt_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/SubstAndDsqlfyPrsnsTotGrp/TotalAmt 

    TxRvLvdOrgnztnlBnft509_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft509Grp/CurrentTaxYearMinus1YearAmt 

    GvtFrnSrvcFcltsVl509_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl509Grp/CurrentTaxYearMinus1YearAmt 

    GrssRcptsNnUnrltBs_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/GrossReceiptsNonUnrltBusGrp/CurrentTaxYearMinus1YearAmt 

    Pst1975UBTI_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/Post1975UBTIGrp/CurrentTaxYearAmt 

    GftsGrntsCntrsRcvd509_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/GiftsGrantsContrisRcvd509Grp/CurrentTaxYearMinus3YearsAmt 

    Ttl509_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/Total509Grp/CurrentTaxYearMinus1YearAmt 

    OthrIncm509_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/OtherIncome509Grp/CurrentTaxYearMinus1YearAmt 

    GrssInvstmntIncm509_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/GrossInvestmentIncome509Grp/CurrentTaxYearAmt 

    GvtFrnSrvcFcltsVl509_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl509Grp/CurrentTaxYearAmt 

    Ttl509_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/Total509Grp/CurrentTaxYearMinus2YearsAmt 

    Pst1975UBTI_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/Post1975UBTIGrp/CurrentTaxYearMinus1YearAmt 

    SbstntlCntrbtrsAmt_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/SubstantialContributorsAmtGrp/TotalAmt 

    SkdA_PblcSpprtCY509Pct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number: Part III Line 15  Description: Public support percentage (line 8 column(f) divided by line 13 column(f))  most recent xpath: /IRS990ScheduleA/PublicSupportCY509Pct 

    SbstntlCntrbtrsAmt_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/SubstantialContributorsAmtGrp/CurrentTaxYearMinus2YearsAmt 

    TxRvLvdOrgnztnlBnft509_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft509Grp/CurrentTaxYearMinus3YearsAmt 

    AmntsRcvdDsqlfyPrsn_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/AmountsRcvdDsqlfyPersonGrp/CurrentTaxYearAmt 

    OthrIncm509_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/OtherIncome509Grp/CurrentTaxYearMinus2YearsAmt 

    InvstmntIncmAndUBTI_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/InvestmentIncomeAndUBTIGrp/CurrentTaxYearAmt 

    AmntsRcvdDsqlfyPrsn_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/AmountsRcvdDsqlfyPersonGrp/CurrentTaxYearMinus2YearsAmt 

    TxRvLvdOrgnztnlBnft509_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft509Grp/CurrentTaxYearAmt 

    GrssInvstmntIncm509_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/GrossInvestmentIncome509Grp/CurrentTaxYearMinus1YearAmt 

    TtlSpprtClndrYr_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/TotalSupportCalendarYearGrp/CurrentTaxYearMinus3YearsAmt 

    Ttl509_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/Total509Grp/CurrentTaxYearMinus3YearsAmt 

    GrssRcptsNnUnrltBs_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/GrossReceiptsNonUnrltBusGrp/CurrentTaxYearMinus4YearsAmt 

    AmntsRcvdDsqlfyPrsn_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/AmountsRcvdDsqlfyPersonGrp/CurrentTaxYearMinus4YearsAmt 

    GftsGrntsCntrsRcvd509_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/GiftsGrantsContrisRcvd509Grp/TotalAmt 

    GftsGrntsCntrsRcvd509_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/GiftsGrantsContrisRcvd509Grp/CurrentTaxYearMinus1YearAmt 

    NtIncmFrmOthrUBI_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/NetIncomeFromOtherUBIGrp/CurrentTaxYearMinus4YearsAmt 

    GrssInvstmntIncm509_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/GrossInvestmentIncome509Grp/CurrentTaxYearMinus3YearsAmt 

    SbstAndDsqlfyPrsnsTt_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/SubstAndDsqlfyPrsnsTotGrp/CurrentTaxYearMinus3YearsAmt 

    GrssRcptsNnUnrltBs_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/GrossReceiptsNonUnrltBusGrp/CurrentTaxYearMinus2YearsAmt 

    InvstmntIncmAndUBTI_CrrntTxYrMns2YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (c)  Description:  Current tax year minus two years  most recent xpath: /IRS990ScheduleA/InvestmentIncomeAndUBTIGrp/CurrentTaxYearMinus2YearsAmt 

    GrssRcptsAdmssns_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/GrossReceiptsAdmissionsGrp/TotalAmt 

    SbstntlCntrbtrsAmt_CrrntTxYrMns3YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (b)  Description:  Current tax year minus three years  most recent xpath: /IRS990ScheduleA/SubstantialContributorsAmtGrp/CurrentTaxYearMinus3YearsAmt 

    NtIncmFrmOthrUBI_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (f)  Description:  Total  most recent xpath: /IRS990ScheduleA/NetIncomeFromOtherUBIGrp/TotalAmt 

    GvtFrnSrvcFcltsVl509_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/GovtFurnSrvcFcltsVl509Grp/CurrentTaxYearMinus4YearsAmt 

    NtIncmFrmOthrUBI_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/NetIncomeFromOtherUBIGrp/CurrentTaxYearAmt 

    OthrIncm509_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/OtherIncome509Grp/CurrentTaxYearMinus4YearsAmt 

    SkdA_InvstmntIncmPYPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number: Part III Line 18  Description: Investment income percentage from prior year's Schedule A, Part III, line 15a  most recent xpath: /IRS990ScheduleA/InvestmentIncomePYPct 

    SkdA_Frst5Yrs509Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part III Line 14  Description: First five years?  most recent xpath: /IRS990ScheduleA/First5Years509Ind 

    GrssRcptsNnUnrltBs_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/GrossReceiptsNonUnrltBusGrp/CurrentTaxYearAmt 

    InvstmntIncmAndUBTI_CrrntTxYrMns1YrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (d)  Description:  Current tax year minus one year  most recent xpath: /IRS990ScheduleA/InvestmentIncomeAndUBTIGrp/CurrentTaxYearMinus1YearAmt 

    SkdA_InvstmntIncmCYPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number: Part III Line 17  Description: Investment income percentage (line 10c column (f) divided by line 13 column(f))  most recent xpath: /IRS990ScheduleA/InvestmentIncomeCYPct 

    Ttl509_CrrntTxYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (e)  Description:  Current tax year  most recent xpath: /IRS990ScheduleA/Total509Grp/CurrentTaxYearAmt 

    TxRvLvdOrgnztnlBnft509_CrrntTxYrMns4YrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II and III Column (a)  Description:  Current tax year minus four years  most recent xpath: /IRS990ScheduleA/TaxRevLeviedOrgnztnlBnft509Grp/CurrentTaxYearMinus4YearsAmt 

#######
#
# IRS990ScheduleA - ScheduleA Part IV Supporting Organizations 
#
#######

class skeda_part_iv(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    TmlyPrvddDcmntsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section D Line 1  Description:  Timely provided written notice, copy of Form 990, and governing documents?  most recent xpath: /IRS990ScheduleA/Form990SchAType3SprtOrgAllGrp/TimelyProvidedDocumentsInd 

    PrntSpprtdOrgInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Part IV Section E Line 1b  Description:  Parent of each of its supported organizations  most recent xpath: /IRS990ScheduleA/Form990SchAType3FuncIntGrp/ParentSupportedOrgInd 

    AppntElctMjrtyOffcrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section E Line 3a  Description:  Power to regularly appoint or elect majority of the officers of each supported organization?  most recent xpath: /IRS990ScheduleA/Form990SchAType3FuncIntGrp/AppointElectMajorityOfficerInd 

    OprtBnftNnSprtOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section B Line 2  Description:  Operate for the benefit of any other supported organization?  most recent xpath: /IRS990ScheduleA/Form990SchAType1SuprtOrgGrp/OperateBenefitNonSuprtOrgInd 

    ExcssBsnssHldngsRlsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 10a  Description:  Subject to excess business holding rules?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/ExcessBusinessHoldingsRulesInd 

    ActvtsTstInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Part IV Section E Line 1a  Description:  Satisfied activities test  most recent xpath: /IRS990ScheduleA/Form990SchAType3FuncIntGrp/ActivitiesTestInd 

    OffcrsClsRltnshpInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section D Line 2  Description:  Maintained close and continuous working relationship with the supported organization?  most recent xpath: /IRS990ScheduleA/Form990SchAType3SprtOrgAllGrp/OfficersCloseRelationshipInd 

    SpprtNnSpprtdOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 6  Description:  Support anyone other than supported organizations?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/SupportNonSupportedOrgInd 

    PymntSbstntlCntrbtrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 7  Description:  Provide grant, loan, compensation to a substantial contributor?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/PaymentSubstantialContribtrInd 

    SprtExclsvlySc170c2BInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 3c  Description:  Ensure support used exclusively for section 170(c)(2)(B) purposes?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/SuprtExclusivelySec170c2BInd 

    CntrbtnCntrllrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 11a  Description:  A person who controls, alone or together with persons in (ii) and (iii) below, the governing body of the supported organization?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/ContributionControllerInd 

    ActvtsFrthrExmptPrpsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section E Line 2a  Description:  Substantially all activities during the year directly further exempt purposes of the supported organization?  most recent xpath: /IRS990ScheduleA/Form990SchAType3FuncIntGrp/ActivitiesFurtherExemptPrpsInd 

    CntrlldDsqlfdPrsnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 9a  Description:  Controlled by one or more disqualified persons?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/ControlledDisqualifiedPrsnInd 

    SpprtFrgnOrgNDtrmInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 4c  Description:  Support any foreign organizations that does not have IRS determination?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/SupportForeignOrgNoDetermInd 

    GvrnmntlEnttyInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Part IV Section E Line 1c  Description:  Supported a governmental entity  most recent xpath: /IRS990ScheduleA/Form990SchAType3FuncIntGrp/GovernmentalEntityInd 

    DsqlfdPrsnCntrllIntInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 9b  Description:  Disqualified person hold controlling interest in any entity which supporting org had an interest?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/DisqualifiedPrsnControllIntInd 

    ExrcsDrctnPlcsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section E Line 3b  Description:  Exercise a substantial degree of direction over policies, programs or activities of each supported org?  most recent xpath: /IRS990ScheduleA/Form990SchAType3FuncIntGrp/ExerciseDirectionPoliciesInd 

    SpprtdOrgQlfdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 3b  Description:  Confirmed supported org qualified?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/SupportedOrgQualifiedInd 

    ActvtsEnggdOrgInvlmntInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section E Line 2b  Description:  Constitute activities that, but for the organization's involvement, supported org would have been engaged?  most recent xpath: /IRS990ScheduleA/Form990SchAType3FuncIntGrp/ActivitiesEngagedOrgInvlmntInd 

    LnDsqlfdPrsnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 8  Description:  Loan to disqualified person?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/LoanDisqualifiedPersonInd 

    SpprtdOrgSctnC456Ind = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 3a  Description:  Supported org described in Section 501(c)(4), (5), (6)?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/SupportedOrgSectionC456Ind 

    SbstttnByndOrgCntlInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 5c  Description:  Substitution the result of an event beyond the organization's control?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/SubstitutionBeyondOrgCntlInd 

    ExcssBsnssHldngsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 10b  Description:  Excess business holdings in the tax year?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/ExcessBusinessHoldingsInd 

    DsqlfdPrsnOwnrIntInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 9c  Description:  Disqualified person have an ownership interest in assets which supporting org had an interest?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/DisqualifiedPrsnOwnrIntInd 

    SprtOrgNIRSDtrmntnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 2  Description:  Any supported organization that does not have IRS determination?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/SuprtOrgNoIRSDeterminationInd 

    SpprtdOrgNtOrgnzdUSInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 4a  Description:  Any supported organized not organized in the United States?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/SupportedOrgNotOrganizedUSInd 

    CntrlDcdngGrntFrgnOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 4b  Description:  Ultimate control in deciding whether to make grants to foreign supported org?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/ControlDecidingGrntFrgnOrgInd 

    SpprtdOrgClssDsgntdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 5b  Description:  Supported organization part of a class already designated in orgs organizing document?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/SupportedOrgClassDesignatedInd 

    LstdByNmGvrnngDcInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 1  Description:  All supported organizations listed by name in governing documents?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/ListedByNameGoverningDocInd 

    PwrAppntMjrtyDrTrstInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section B Line 1  Description:  Directors, trustees, or membership of supported org have power to regularly appoint or elect at least majority of orgs directors or trustees?  most recent xpath: /IRS990ScheduleA/Form990SchAType1SuprtOrgGrp/PowerAppointMajorityDirTrstInd 

    SpprtdOrgVcInvstmntInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section D Line 3  Description:  Supported organizations have significant voice in the organizations investment policies?  most recent xpath: /IRS990ScheduleA/Form990SchAType3SprtOrgAllGrp/SupportedOrgVoiceInvestmentInd 

    OrgnztnChngSprtOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 5a  Description:  Organization add, substitute or remove any supported org during the year?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/OrganizationChangeSuprtOrgInd 

    Cntrbtn35CntrlldInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 11c  Description:  A 35% controlled entity of a person described in (i) or (ii) above?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/Contribution35ControlledInd 

    CntrbtnFmlyInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Section A Line 11b  Description:  A family member of a party described in (i) above?  most recent xpath: /IRS990ScheduleA/Form990SchASupportingOrgGrp/ContributionFamilyInd 

    MjrtyDrTrstSpprtdOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part IV Section C Line 1  Description: Also a majority of the directors or trustees of each of the organizations supported orgs?  most recent xpath: /IRS990ScheduleA/MajorityDirTrstSupportedOrgInd 

#######
#
# IRS990ScheduleA - ScheduleA Part V Type III Non-Functionally Integrated 509(a)(3) Supporting Organizations 
#
#######

class skeda_part_v(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    DstrbtblAmnt_FrstYr3NnFncInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Part V Section C Line 7  Description:  First year as a non-functionally-integrated Type III supporting organization  most recent xpath: /IRS990ScheduleA/DistributableAmountGrp/FirstYearType3NonFuncInd 

    AdjstdGrssIncm_PrrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column A  Description:  Prior year amount  most recent xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/AdjustedGrossIncomeGrp/PriorYearAmt 

    DstrbtblAmnt_CYGrtrAdjstdMnmmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section C Line 4(B)  Description:  Greater of 85% adjusted net income amount and minimum assets amount  most recent xpath: /IRS990ScheduleA/DistributableAmountGrp/CYGreaterAdjustedMinimumAmt 

    DstrbtnAllctns_ExcssDstrbtnCyvYr3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 3(c)  Description:  Excess distributions carryover - year 3  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessDistributionCyovYr3Amt 

    RcvrsPYDstrbtns_PrrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column A  Description:  Prior year amount  most recent xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/RecoveriesPYDistributionsGrp/PriorYearAmt 

    FMVOthrNnExmptUsAsst_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column B  Description:  Current year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/FMVOtherNonExemptUseAssetGrp/CurrentYearAmt 

    ExcssFrmYr5Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 8a  Description:  Excess from year 5  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessFromYear5Amt 

    AvrgMnthlyCshBlncs_PrrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column A  Description:  Prior year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/AverageMonthlyCashBalancesGrp/PriorYearAmt 

    DstrbtnAllctns_TtlExcssDstrbtnCyvAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 3(f)(i)  Description:  Excess distributions carryover amount  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/TotalExcessDistributionCyovAmt 

    DstrbtnAllctns_ExcssDstrCyvTNxtYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 7(i)  Description:  Excess distribution carryover to next year  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessDistriCyovToNextYrAmt 

    DstrbtnAllctns_RmnngUndrdstrPYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 5(ii)  Description:  Remaining underdistributions - prior years  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/RemainingUnderdistriPYAmt 

    TtlMnmmAsst_PrrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column A  Description:  Prior year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/TotalMinimumAssetGrp/PriorYearAmt 

    DstrbtnAllctns_CYDstrbtblAsAdjstdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 1(iii)  Description:  Distributable amount for current year (from Section C, line 6)  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/CYDistributableAsAdjustedAmt 

    Dstrbtns_CYDstrbtnYrRt = models.TextField(null=True, blank=True)
    # Line number:  Part V Section D Line 10  Description: Distributions to attentive supported org divided by Distributable amount  most recent xpath: /IRS990ScheduleA/DistributionsGrp/CYDistributionYrRt 

    PctOfNtVlNnExmptUsAst_PrrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column A  Description:  Prior year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/PctOfNetVlNonExemptUseAstGrp/PriorYearAmt 

    DstrbtblAmnt_CYAdjNtIncmDstrbtblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section C Line 1(B)  Description:  Adjusted net income amount for prior year - distributable amount (from Section A, line 8, Column A)  most recent xpath: /IRS990ScheduleA/DistributableAmountGrp/CYAdjNetIncomeDistributableAmt 

    DstrbtblAmnt_CYDstrbtblAsAdjstdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section C Line 6(B)  Description:  Distributable amount as adjusted unless subject to emergency temporary reduction  most recent xpath: /IRS990ScheduleA/DistributableAmountGrp/CYDistributableAsAdjustedAmt 

    TtlAdjstdNtIncm_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column B  Description:  Current year amount  most recent xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/TotalAdjustedNetIncomeGrp/CurrentYearAmt 

    AvrgMnthlyFMVOfSc_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column B  Description:  Current year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/AverageMonthlyFMVOfSecGrp/CurrentYearAmt 

    DstrbtblAmnt_CYTtlMnAstDstrbtblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section C Line 3(B)  Description:  Minimum asset amount for prior year - distributable amount (from Section B, line 8, Column A)  most recent xpath: /IRS990ScheduleA/DistributableAmountGrp/CYTotalMinAstDistributableAmt 

    DstrbtblAmnt_CYPct85AdjstdNtIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section C Line 2(B)  Description:  85% Percent of adjusted net income amount - distributable amount  most recent xpath: /IRS990ScheduleA/DistributableAmountGrp/CYPct85AdjustedNetIncomeAmt 

    Dstrbtns_CYDstrAttntvSprtOrgAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section D Line 8  Description: Distributions to attentive supported organizations to which the org is responsive  most recent xpath: /IRS990ScheduleA/DistributionsGrp/CYDistriAttentiveSuprtOrgAmt 

    RcvrsPYDstrMnAsst_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column B  Description:  Current year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/RecoveriesPYDistriMinAssetGrp/CurrentYearAmt 

    AvrgMnthlyCshBlncs_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column B  Description:  Current year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/AverageMonthlyCashBalancesGrp/CurrentYearAmt 

    RcvrsPYDstrbtns_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column B  Description:  Current year amount  most recent xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/RecoveriesPYDistributionsGrp/CurrentYearAmt 

    DstrbtnAllctns_ExcssFrmYr1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 8e  Description:  Excess from year 1  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessFromYear1Amt 

    DstrbtblAmnt_CYIncmTxImpsdPYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section C Line 5(B)  Description:  Income tax imposed in prior year  most recent xpath: /IRS990ScheduleA/DistributableAmountGrp/CYIncomeTaxImposedPYAmt 

    MnmmAsstAmnt_DscntClmdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section B Line 1e  Description:  Discount claimed for blockage or other factors  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/DiscountClaimedAmt 

    DstrbtnAllctns_ExcssDstrbtnCyvYr2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 3(d)  Description:  Excess distributions carryover - year 2  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessDistributionCyovYr2Amt 

    Dstrbtns_CYAdmnstrtvExpnsPdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section D Line 3  Description: Administrative expenses paid to accomplish exempt purposes  most recent xpath: /IRS990ScheduleA/DistributionsGrp/CYAdministrativeExpensePaidAmt 

    DstrbtnAllctns_ExcssDstrbtnCyvAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 3(j)  Description:  Excess distributions carryover amount  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessDistributionCyovAmt 

    Dstrbtns_CYOthrDstrbtnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section D Line 6  Description: Other distributions - Current Year  most recent xpath: /IRS990ScheduleA/DistributionsGrp/CYOtherDistributionsAmt 

    OthrGrssIncm_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column B  Description:  Current year amount  most recent xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/OtherGrossIncomeGrp/CurrentYearAmt 

    DstrbtnAllctns_CyvAppldUndrdstrCPYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 3(h)(iii)  Description:  Carryover applied to current year  distributable amount  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/CyovAppliedUnderdistrCPYAmt 

    DstrbtnAllctns_ExcssFrmYr2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 8d  Description:  Excess from year 2  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessFromYear2Amt 

    AcqstnIndbtdnss_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column B  Description:  Current year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/AcquisitionIndebtednessGrp/CurrentYearAmt 

    OthrExpnss_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column B  Description:  Current year amount  most recent xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/OtherExpensesGrp/CurrentYearAmt 

    ExcssDstrbtnCyvYr4Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 3(b)  Description:  Excess distributions carryover - year 4  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessDistributionCyovYr4Amt 

    NtVlNnExmptUsAssts_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column B  Description:  Current year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/NetVlNonExemptUseAssetsGrp/CurrentYearAmt 

    AdjstdGrssIncm_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column B  Description:  Current year amount  most recent xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/AdjustedGrossIncomeGrp/CurrentYearAmt 

    AdjstdFMVLssIndbtdnss_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column B  Description:  Current year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/AdjustedFMVLessIndebtednessGrp/CurrentYearAmt 

    NtSTCptlGnAdjNtIncm_PrrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column A  Description:  Prior year amount  most recent xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/NetSTCapitalGainAdjNetIncmGrp/PriorYearAmt 

    RcvrsPYDstrMnAsst_PrrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column A  Description:  Prior year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/RecoveriesPYDistriMinAssetGrp/PriorYearAmt 

    PrdctnIncm_PrrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column A  Description:  Prior year amount  most recent xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/ProductionIncomeGrp/PriorYearAmt 

    DprctnDpltn_PrrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column A  Description:  Prior year amount  most recent xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/DepreciationDepletionGrp/PriorYearAmt 

    DstrbtnAllctns_UndrdstrbtnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 2(ii)  Description:  Underdistributions for years prior to current year  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/UnderdistributionsAmt 

    DstrbtnAllctns_CYTtlAnnlDstrbtnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 4  Description:  Total annual distributions from current year (from Section D, line 7)  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/CYTotalAnnualDistributionsAmt 

    OthrGrssIncm_PrrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column A  Description:  Prior year amount  most recent xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/OtherGrossIncomeGrp/PriorYearAmt 

    AcqstnIndbtdnss_PrrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column A  Description:  Prior year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/AcquisitionIndebtednessGrp/PriorYearAmt 

    CrryvrPYNtAppldAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 3(i)  Description:  Carryover from prior years not applied.  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/CarryoverPYNotAppliedAmt 

    DstrbtnAllctns_RmnngUndrdstrCYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 6(iii)  Description:  Remaining underdistributions - current years  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/RemainingUnderdistriCYAmt 

    ExcssDstrbtnCyvYr5Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 3(a)  Description:  Excess distributions carryover - year 5  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessDistributionCyovYr5Amt 

    PrdctnIncm_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column B  Description:  Current year amount  most recent xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/ProductionIncomeGrp/CurrentYearAmt 

    Dstrbtns_CYPdInExcssIncmActvtyAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section D Line 2  Description: Amounts paid to perform activity that directly furthers exempt purpose - in excess of income from activity  most recent xpath: /IRS990ScheduleA/DistributionsGrp/CYPdInExcessIncomeActivityAmt 

    Dstrbtns_CYDstrbtblAsAdjstdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section D Line 9  Description: Distributable amount for current year (from Section C, line 6)  most recent xpath: /IRS990ScheduleA/DistributionsGrp/CYDistributableAsAdjustedAmt 

    DstrbtnAllctns_ExcssDstrbtnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 4c(i)  Description:  Excess distributions current year amount  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessDistributionAmt 

    AdjstdFMVLssIndbtdnss_PrrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column A  Description:  Prior year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/AdjustedFMVLessIndebtednessGrp/PriorYearAmt 

    DstrbtnAllctns_ExcssFrmYr3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 8c  Description:  Excess from year 3  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessFromYear3Amt 

    DstrbtnAllctns_ExcssFrmYr4Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 8b  Description:  Excess from year 4  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessFromYear4Amt 

    DstrbtnAllctns_ExcssDstrbtnCyvYr1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 3(e)  Description:  Excess distributions carryover - year 1  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/ExcessDistributionCyovYr1Amt 

    Dstrbtns_ExmptUsAsstsAcqsPdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section D Line 4  Description: Amounts paid to acquire exempt-use assets  most recent xpath: /IRS990ScheduleA/DistributionsGrp/ExemptUseAssetsAcquisPaidAmt 

    TtlFMVOfNnExmptUsAsst_PrrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column A  Description:  Prior year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/TotalFMVOfNonExemptUseAssetGrp/PriorYearAmt 

    PctOfNtVlNnExmptUsAst_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column B  Description:  Current year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/PctOfNetVlNonExemptUseAstGrp/CurrentYearAmt 

    Dstrbtns_QlfdStAsdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section D Line 5  Description: Qualified set-aside amounts  most recent xpath: /IRS990ScheduleA/DistributionsGrp/QualifiedSetAsideAmt 

    DstrbtnAllctns_CyvAppldUndrdstrPYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 3(g)(ii)  Description:  Carryover applied to underdistributions of prior years  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/CyovAppliedUnderdistriPYAmt 

    NtSTCptlGnAdjNtIncm_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column B  Description:  Current year amount  most recent xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/NetSTCapitalGainAdjNetIncmGrp/CurrentYearAmt 

    TtlFMVOfNnExmptUsAsst_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column B  Description:  Current year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/TotalFMVOfNonExemptUseAssetGrp/CurrentYearAmt 

    OthrExpnss_PrrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column A  Description:  Prior year amount  most recent xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/OtherExpensesGrp/PriorYearAmt 

    DprctnDpltn_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column B  Description:  Current year amount  most recent xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/DepreciationDepletionGrp/CurrentYearAmt 

    DstrbtnAllctns_CYDstrbAppUndrdstrPYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 4a(ii)  Description:  Current year distributions applied to underdistributions of prior years  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/CYDistribAppUnderdistriPYAmt 

    TtlMnmmAsst_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column B  Description:  Current year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/TotalMinimumAssetGrp/CurrentYearAmt 

    AvrgMnthlyFMVOfSc_PrrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column A  Description:  Prior year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/AverageMonthlyFMVOfSecGrp/PriorYearAmt 

    NtVlNnExmptUsAssts_PrrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column A  Description:  Prior year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/NetVlNonExemptUseAssetsGrp/PriorYearAmt 

    FMVOthrNnExmptUsAsst_PrrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column A  Description:  Prior year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/FMVOtherNonExemptUseAssetGrp/PriorYearAmt 

    Dstrbtns_CYTtlAnnlDstrbtnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section D Line 7  Description: Total annual distributions - Current Year  most recent xpath: /IRS990ScheduleA/DistributionsGrp/CYTotalAnnualDistributionsAmt 

    CshDmdChrtbl_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column B  Description:  Current year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/CashDeemedCharitableGrp/CurrentYearAmt 

    TtlAdjstdNtIncm_PrrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column A  Description:  Prior year amount  most recent xpath: /IRS990ScheduleA/AdjustedNetIncomeGrp/TotalAdjustedNetIncomeGrp/PriorYearAmt 

    Dstrbtns_CYPdAccmplshExmptPrpsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section D Line 1  Description: Amounts paid to supported organizations to accomplish exempt purpose - Current Year  most recent xpath: /IRS990ScheduleA/DistributionsGrp/CYPaidAccomplishExemptPrpsAmt 

    DstrbtnAllctns_CYDstrAppDstrbtblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Section E Line 4b(iii)  Description:  Current year distributions applied to distributable amount  most recent xpath: /IRS990ScheduleA/DistributionAllocationsGrp/CYDistriAppDistributableAmt 

    CshDmdChrtbl_PrrYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Column A  Description:  Prior year amount  most recent xpath: /IRS990ScheduleA/MinimumAssetAmountGrp/CashDeemedCharitableGrp/PriorYearAmt 

    SkdA_TrstIntgrlPrtTstInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Line 1  Description: Organization satisfied Integral Part Test as qualifying trust  most recent xpath: /IRS990ScheduleA/TrustIntegralPartTestInd 

#######
#
# IRS990ScheduleA - ScheduleA Part VI Supplemental Information 
#
#######

class skeda_part_vi(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FctsAndCrcmstncsTstTxt = models.TextField(null=True, blank=True)
    # Line number: Part VI  Description: Facts and circumstances test  most recent xpath: /IRS990ScheduleA/FactsAndCircumstancesTestTxt 

#######
#
# IRS990ScheduleA - SkdAAgrcltrlNmAndAddrss
# A repeating structure from skeda_part_i
#
#######

class SkdAAgrcltrlNmAndAddrss(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number:  Part I Line 9  Description:  US city or foreign city  most recent xpath: /IRS990ScheduleA/AgriculturalNameAndAddressGrp/CityNm 

    SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part I Line 9  Description:  US address State  most recent xpath: /IRS990ScheduleA/AgriculturalNameAndAddressGrp/StateAbbreviationCd 

    BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part I Line 9  Description:  Business name line 2  most recent xpath: /IRS990ScheduleA/AgriculturalNameAndAddressGrp/CollegeUniversityName/BusinessNameLine2Txt 

    CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part I Line 9  Description:  Foreign address Country  most recent xpath: /IRS990ScheduleA/AgriculturalNameAndAddressGrp/CountryCd 

    BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part I Line 9  Description:  Business name line 1  most recent xpath: /IRS990ScheduleA/AgriculturalNameAndAddressGrp/CollegeUniversityName/BusinessNameLine1Txt 

#######
#
# IRS990ScheduleA - SkdAHsptlNmAndAddrss
# A repeating structure from skeda_part_i
#
#######

class SkdAHsptlNmAndAddrss(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part I Line 4  Description:  US address State  most recent xpath: /IRS990ScheduleA/HospitalNameAndAddressGrp/StateAbbreviationCd 

    CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part I Line 4  Description:  Foreign address Country  most recent xpath: /IRS990ScheduleA/HospitalNameAndAddressGrp/CountryCd 

    BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part I Line 4  Description:  Business name line 2  most recent xpath: /IRS990ScheduleA/HospitalNameAndAddressGrp/SupportedOrganizationName/BusinessNameLine2Txt 

    BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part I Line 4  Description:  Business name line 1  most recent xpath: /IRS990ScheduleA/HospitalNameAndAddressGrp/SupportedOrganizationName/BusinessNameLine1Txt 

    CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number:  Part I Line 4  Description:  US city or foreign city  most recent xpath: /IRS990ScheduleA/HospitalNameAndAddressGrp/CityNm 

#######
#
# IRS990ScheduleA - SkdASpprtdOrgInfrmtn
# A repeating structure from skeda_part_i
#
#######

class SkdASpprtdOrgInfrmtn(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    GvrnngDcmntLstdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part I Line 12g Column (iv)  Description:  Is the supported organization listed in your governing documents?  most recent xpath: /IRS990ScheduleA/SupportedOrgInformationGrp/GoverningDocumentListedInd 

    OrgnztnCd = models.TextField(null=True, blank=True)
    # Line number:  Part I Line 12g(iii)  Description:  Type of organization  most recent xpath: /IRS990ScheduleA/SupportedOrgInformationGrp/OrganizationTypeCd 

    OthrSpprtAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part I Line 12g Column (vi)  Description:  Estimated value of diversion  most recent xpath: /IRS990ScheduleA/SupportedOrgInformationGrp/OtherSupportAmt 

    BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part I Line 12g Column (i)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleA/SupportedOrgInformationGrp/SupportedOrganizationName/BusinessNameLine2Txt 

    SpprtAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part I Line 12g Column (v)  Description:  Amount of support  most recent xpath: /IRS990ScheduleA/SupportedOrgInformationGrp/SupportAmt 

    BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part I Line 12g Column (i)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleA/SupportedOrgInformationGrp/SupportedOrganizationName/BusinessNameLine1Txt 

    SupportedOrgEIN = models.CharField(null=True, blank=True, max_length=9)
    # Line number:  Part I Line 12g Column (ii)  Description:  EIN of supported organization  most recent xpath: /IRS990ScheduleA/SupportedOrgInformationGrp/EIN 

#######
#
# IRS990ScheduleA - SkdAFrm990SkdAPrtVI - Supplemental information for schedule A
# A repeating structure from skeda_part_vi
#
#######

class SkdAFrm990SkdAPrtVI(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    ExplntnTxt = models.TextField(null=True, blank=True)
    # Line number:  Schedule A Part VI  Description:  Form, part and line number reference explanation  most recent xpath: /IRS990ScheduleA/Form990ScheduleAPartVIGrp/ExplanationTxt 

    FrmAndLnRfrncDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Schedule A Part VI  Description:  Form, part and line number reference  most recent xpath: /IRS990ScheduleA/Form990ScheduleAPartVIGrp/FormAndLineReferenceDesc 

#######
#
# IRS990ScheduleB - ScheduleB Part 0 Prefatory material 
#
#######

class skedb_part_0(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    SpclRlMtOn3rdSprtTstInd = models.CharField(null=True, blank=True, max_length=1)
    # Description: For a section 501(c)(3) organization filing Form 990, or Form 990-EZ, that met the 33 1/3 % support test of the regulations under sections 509(a)(1)/170(b)(1)(A)(vi) and received from any one contributor, during the year, a contribution of the greater of $5,000 or 2% of the amount on line 1 of these forms  most recent xpath: /IRS990ScheduleB/SpclRuleMetOne3rdSuprtTestInd 

    Orgnztn501cInd = models.TextField(null=True, blank=True)
    # Description: Indicates a 501(c) organization  most recent xpath: /IRS990ScheduleB/Organization501cInd 

    Orgnztn501c3ExmptPFInd = models.CharField(null=True, blank=True, max_length=1)
    # Description: Organization 501(c)(3) exempt PF  most recent xpath: /IRS990ScheduleB/Organization501c3ExemptPFInd 

    TtCntrRcvdMr1000Ind = models.CharField(null=True, blank=True, max_length=1)
    # Description: For a section 501(c)(7), (8), or (10) organization filing Form 990, or Form 990-EZ, that received from any one contributor, during the year, aggregate contributions or bequests of more than $1,000 for use exclusively for religious, charitable, scientific, literary, or educational purposes, or the prevention of cruelty to children or animals  most recent xpath: /IRS990ScheduleB/TotContriRcvdMore1000Ind 

    TtCntrRcvdUpT1000Ind = models.TextField(null=True, blank=True)
    # Description: For a section 501(c)(7), (8), or (10) organization filing Form 990, or Form 990-EZ, that received from any one contributor, during the year, some contributions for use exclusively for religious, charitable, etc., purposes, but these contributions did not aggregate to more than $1,000  most recent xpath: /IRS990ScheduleB/TotContriRcvdUpTo1000Ind 

    Orgnztn527Ind = models.CharField(null=True, blank=True, max_length=1)
    # Description: Indicates a 527 organization  most recent xpath: /IRS990ScheduleB/Organization527Ind 

    Orgnztn49471NtPFInd = models.CharField(null=True, blank=True, max_length=1)
    # Description: Indicates a 4947(a)(1) organization not treated as a private foundation  most recent xpath: /IRS990ScheduleB/Organization4947a1NotPFInd 

    Orgnztn501c3TxblPFInd = models.CharField(null=True, blank=True, max_length=1)
    # Description: Indicates a 501(c)(3) taxable private foundation  most recent xpath: /IRS990ScheduleB/Organization501c3TaxablePFInd 

    Orgnztn49471TrtdPFInd = models.CharField(null=True, blank=True, max_length=1)
    # Description: Organization 4947(a)(1) treated as PF  most recent xpath: /IRS990ScheduleB/Organization4947a1TrtdPFInd 

    GnrlRlInd = models.CharField(null=True, blank=True, max_length=1)
    # Description: For organizations filing Form 990, or 990-EZ that received, during the year, $5000 or more (in money or property) from any one contributor  most recent xpath: /IRS990ScheduleB/GeneralRuleInd 

#######
#
# IRS990ScheduleB - ScheduleB Part II - Noncash Property 
#
#######

class skedb_part_ii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    TtlUndr1000CntrbtnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III  Description: Total of contributions of $1,000 or less  most recent xpath: /IRS990ScheduleB/TotalUnder1000ContributionsAmt 

#######
#
# IRS990ScheduleB - SkdBCntrbtrInfrmtn
# A repeating structure from skedb_part_i
#
#######

class SkdBCntrbtrInfrmtn(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    CntrbtrUSAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number:  Part I Column (b)  Description:  ZIP code  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorUSAddress/ZIPCd 

    CntrbtrInfrmtn_PyrllCntrbtnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Part I Column (d)  Description:  Type of contribution - Payroll  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/PayrollContributionInd 

    CntrbtrInfrmtn_CntrbtrPrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part I Column (b)  Description:  Contributor name - Individual  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorPersonNm 

    CntrbtrInfrmtn_NncshCntrbtnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Part I Column (d)  Description:  Type of contribution - Noncash  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/NoncashContributionInd 

    CntrbtrBsnssNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part I Column (b)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorBusinessName/BusinessNameLine2Txt 

    CntrbtrFrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part I Column (b)  Description:  Country  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorForeignAddress/CountryCd 

    CntrbtrInfrmtn_PrsnCntrbtnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Part I Column (d)  Description:  Type of contribution - Person  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/PersonContributionInd 

    CntrbtrFrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number:  Part I Column (b)  Description:  Postal code  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorForeignAddress/ForeignPostalCd 

    CntrbtrUSAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part I Column (b)  Description:  Address line 2  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorUSAddress/AddressLine2Txt 

    CntrbtrInfrmtn_CntrbtrNm = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part I Column (a)  Description:  Cotributor number  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorNum 

    AddrssNtApplcblCd = models.TextField(null=True, blank=True)
    # Line number:  Part I Column (b)  Description:  Contributor Address - "N/A  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/AddressNotApplicableCd 

    CntrbtrUSAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part I Column (b)  Description:  State  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorUSAddress/StateAbbreviationCd 

    CntrbtrBsnssNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part I Column (b)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorBusinessName/BusinessNameLine1Txt 

    CntrbtrInfrmtn_Pd527j1Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Part I Column (b)  Description:  Pd. 527(j)(1)  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/Paid527j1Ind 

    CntrbtrFrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part I Column (b)  Description:  Address line 1  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorForeignAddress/AddressLine1Txt 

    NmNtApplcblCd = models.TextField(null=True, blank=True)
    # Line number:  Part I Column (b)  Description:  Contributor name - "N/A  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/NameNotApplicableCd 

    CntrbtrFrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part I Column (b)  Description:  Address line 2  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorForeignAddress/AddressLine2Txt 

    CntrbtrFrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number:  Part I Column (b)  Description:  Province or state  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorForeignAddress/ProvinceOrStateNm 

    CntrbtrFrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number:  Part I Column (b)  Description:  City  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorForeignAddress/CityNm 

    CntrbtrInfrmtn_TtlCntrbtnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part I Column (c)  Description:  Aggregate contributions  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/TotalContributionsAmt 

    CntrbtrUSAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part I Column (b)  Description:  Address line 1  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorUSAddress/AddressLine1Txt 

    CntrbtrUSAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number:  Part I Column (b)  Description:  City  most recent xpath: /IRS990ScheduleB/ContributorInformationGrp/ContributorUSAddress/CityNm 

#######
#
# IRS990ScheduleB - SkdBChrtblCntrbtnsDtl
# A repeating structure from skedb_part_ii
#
#######

class SkdBChrtblCntrbtnsDtl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    TrnsfrUSAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part III Column (e)  Description:  State  most recent xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeUSAddress/StateAbbreviationCd 

    TrnsfrUSAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number:  Part III Column (e)  Description:  ZIP code  most recent xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeUSAddress/ZIPCd 

    TrnsfrFrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part III Column (e)  Description:  Country  most recent xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeForeignAddress/CountryCd 

    TrnsfrUSAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part III Column (e)  Description:  Address line 2  most recent xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeUSAddress/AddressLine2Txt 

    ChrtblCntrbtnsDtl_CntrbtrNm = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part III Column (a)  Description:  Contributor number from Part I  most recent xpath: /IRS990ScheduleB/CharitableContributionsDetail/ContributorNum 

    TrnsfrFrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number:  Part III Column (e)  Description:  Province or state  most recent xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeForeignAddress/ProvinceOrStateNm 

    TrnsfrFrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number:  Part III Column (e)  Description:  Postal code  most recent xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeForeignAddress/ForeignPostalCd 

    ChrtblCntrbtnsDtl_GftUsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part III Column (c)  Description:  Use of gift  most recent xpath: /IRS990ScheduleB/CharitableContributionsDetail/GiftUseTxt 

    TrnsfrFrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part III Column (e)  Description:  Address line 2  most recent xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeForeignAddress/AddressLine2Txt 

    TrnsfrFrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number:  Part III Column (e)  Description:  City  most recent xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeForeignAddress/CityNm 

    TrnsfrNmBsnss_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part III Column (e)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeNameBusiness/BusinessNameLine2Txt 

    ChrtblCntrbtnsDtl_RlnOfTrnsfrrTTrnsfrTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part III Column (e)  Description:  Relationship of transferor to transferee  most recent xpath: /IRS990ScheduleB/CharitableContributionsDetail/RlnOfTransferorToTransfereeTxt 

    TrnsfrFrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part III Column (e)  Description:  Address line 1  most recent xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeForeignAddress/AddressLine1Txt 

    TrnsfrUSAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part III Column (e)  Description:  Address line 1  most recent xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeUSAddress/AddressLine1Txt 

    ChrtblCntrbtnsDtl_TrnsfrNmIndvdl = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part III Column (e)  Description:  Transferee name - Individual  most recent xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeNameIndividual 

    TrnsfrUSAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number:  Part III Column (e)  Description:  City  most recent xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeUSAddress/CityNm 

    ChrtblCntrbtnsDtl_HwGftIsHldDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part III Column (d)  Description:  Description of how gift is held  most recent xpath: /IRS990ScheduleB/CharitableContributionsDetail/HowGiftIsHeldDesc 

    TrnsfrNmBsnss_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part III Column (e)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleB/CharitableContributionsDetail/TransfereeNameBusiness/BusinessNameLine1Txt 

    ChrtblCntrbtnsDtl_GftPrpsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part III Column (b)  Description:  Purpose of gift  most recent xpath: /IRS990ScheduleB/CharitableContributionsDetail/GiftPurposeTxt 

#######
#
# IRS990ScheduleB - SkdBNnCshPrprtyCntrbtn
# A repeating structure from skedb_part_ii
#
#######

class SkdBNnCshPrprtyCntrbtn(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    NncshPrprtyDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part II Column (b)  Description:  Description of noncash property given  most recent xpath: /IRS990ScheduleB/NonCashPropertyContributionGrp/NoncashPropertyDesc 

    RcvdDt = models.CharField(null=True, blank=True, max_length=31)
    # Line number:  Part II Column (d)  Description:  Date received  most recent xpath: /IRS990ScheduleB/NonCashPropertyContributionGrp/ReceivedDt 

    FrMrktVlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Column (c)  Description:  FMV (or estimate)  most recent xpath: /IRS990ScheduleB/NonCashPropertyContributionGrp/FairMarketValueAmt 

    CntrbtrNm = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Column (a)  Description:  Contributor number from Part I  most recent xpath: /IRS990ScheduleB/NonCashPropertyContributionGrp/ContributorNum 

#######
#
# IRS990ScheduleC - ScheduleC Part 0 Prefatory material 
#
#######

class skedc_part_0(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    Sctn4955MngrsTxAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I-B Line 2  Description: Enter the amount of any excise tax incurred by organization managers under section 4955  most recent xpath: /IRS990ScheduleC/Section4955ManagersTaxAmt 

    Sctn4955OrgnztnTxAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I-B Line 1  Description: Enter the amount of any excise tax incurred under section 4955  most recent xpath: /IRS990ScheduleC/Section4955OrganizationTaxAmt 

    Expndd527ActvtsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I-C Line 1  Description: Enter the amount directly expended by the filing organization for section 527 exempt function activities  most recent xpath: /IRS990ScheduleC/Expended527ActivitiesAmt 

    VlntrHrsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I-A Line 3  Description: Volunteer hours  most recent xpath: /IRS990ScheduleC/VolunteerHoursCnt 

    TtlExmptFnctnExpndAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I-C Line 3  Description: Total of direct and indirect exempt function expenditures. Add lines 1 and 2  most recent xpath: /IRS990ScheduleC/TotalExemptFunctionExpendAmt 

    Frm4720FldSctn4955TxInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I-B Line 3  most recent xpath: /IRS990ScheduleC/Form4720FiledSection4955TaxInd 

    PltclExpndtrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I-A Line 2  Description: Political expenditures  most recent xpath: /IRS990ScheduleC/PoliticalExpendituresAmt 

    IntrnlFndsCntrbtdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I-C Line 2  Description: Enter the amount of the filing organization's own internal funds contributed to other organizations for section 527 exempt function activities  most recent xpath: /IRS990ScheduleC/InternalFundsContributedAmt 

    Frm1120POLFldInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I-C Line 4  Description: Did the filing organization file Form 1120-POL for this year?  most recent xpath: /IRS990ScheduleC/Form1120POLFiledInd 

    CrrctnMdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I-B Line 4a  Description: If the filing organization incurred in a section 4955 tax, did it file Form 4720 for this year?  most recent xpath: /IRS990ScheduleC/CorrectionMadeInd 

#######
#
# IRS990ScheduleC - ScheduleC Part II-A : Political Campaign and Lobbying Activities 
#
#######

class skedc_part_iia(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    LbbyngNntxblAmnt_AffltdGrpTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (b)  Description:  Affiliated group totals  most recent xpath: /IRS990ScheduleC/LobbyingNontaxableAmountGrp/AffiliatedGroupTotalAmt 

    AvgGrssrtsNntxbl_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (d)  Description:  Current year  most recent xpath: /IRS990ScheduleC/AvgGrassrootsNontaxableGrp/CurrentYearAmt 

    SkdC_GrssrtsClngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II-A Line 2e(e)  Description: Grassroots ceiling amount (150% of line 2d(e))  most recent xpath: /IRS990ScheduleC/GrassrootsCeilingAmt 

    AvgGrssrtsNntxbl_CrrntYrMns3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (a)  Description:  Current year minus 3  most recent xpath: /IRS990ScheduleC/AvgGrassrootsNontaxableGrp/CurrentYearMinus3Amt 

    AvgLbbyngNntxblAmnt_CrrntYrMns2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (b)  Description:  Current year minus 2  most recent xpath: /IRS990ScheduleC/AvgLobbyingNontaxableAmountGrp/CurrentYearMinus2Amt 

    TtlLbbyngExpnd_AffltdGrpTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (b)  Description:  Affiliated group totals  most recent xpath: /IRS990ScheduleC/TotalLobbyingExpendGrp/AffiliatedGroupTotalAmt 

    AvgGrssrtsLbbyngExpnd_CrrntYrMns3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (a)  Description:  Current year minus 3  most recent xpath: /IRS990ScheduleC/AvgGrassrootsLobbyingExpendGrp/CurrentYearMinus3Amt 

    TtLbbyngGrssrtMnsNnTx_AffltdGrpTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (b)  Description:  Affiliated group totals  most recent xpath: /IRS990ScheduleC/TotLbbyngGrassrootMnsNonTxGrp/AffiliatedGroupTotalAmt 

    AvgGrssrtsNntxbl_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (e)  Description:  Total  most recent xpath: /IRS990ScheduleC/AvgGrassrootsNontaxableGrp/TotalAmt 

    SkdC_OrgnztnBlngsAffltInd = models.TextField(null=True, blank=True)
    # Line number: Part II-A Line A  Description: Check if the organization belongs to an affiliated group  most recent xpath: /IRS990ScheduleC/OrganizationBelongsAffltGrpInd 

    AvgTtlLbbyngExpnd_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (d)  Description:  Current year  most recent xpath: /IRS990ScheduleC/AvgTotalLobbyingExpendGrp/CurrentYearAmt 

    AvgLbbyngNntxblAmnt_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (d)  Description:  Current year  most recent xpath: /IRS990ScheduleC/AvgLobbyingNontaxableAmountGrp/CurrentYearAmt 

    AvgLbbyngNntxblAmnt_CrrntYrMns1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (c)  Description:  Current year minus 1  most recent xpath: /IRS990ScheduleC/AvgLobbyingNontaxableAmountGrp/CurrentYearMinus1Amt 

    OthrExmptPrpsExpnd_AffltdGrpTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (b)  Description:  Affiliated group totals  most recent xpath: /IRS990ScheduleC/OtherExemptPurposeExpendGrp/AffiliatedGroupTotalAmt 

    AvgLbbyngNntxblAmnt_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (e)  Description:  Total  most recent xpath: /IRS990ScheduleC/AvgLobbyingNontaxableAmountGrp/TotalAmt 

    AvgGrssrtsNntxbl_CrrntYrMns2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (b)  Description:  Current year minus 2  most recent xpath: /IRS990ScheduleC/AvgGrassrootsNontaxableGrp/CurrentYearMinus2Amt 

    TtlDrctLbbyng_FlngOrgnztnsTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (a)  Description:  Filing organization's totals  most recent xpath: /IRS990ScheduleC/TotalDirectLobbyingGrp/FilingOrganizationsTotalAmt 

    AvgTtlLbbyngExpnd_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (e)  Description:  Total  most recent xpath: /IRS990ScheduleC/AvgTotalLobbyingExpendGrp/TotalAmt 

    AvgGrssrtsLbbyngExpnd_CrrntYrMns2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (b)  Description:  Current year minus 2  most recent xpath: /IRS990ScheduleC/AvgGrassrootsLobbyingExpendGrp/CurrentYearMinus2Amt 

    TtlGrssrtsLbbyng_AffltdGrpTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (b)  Description:  Affiliated group totals  most recent xpath: /IRS990ScheduleC/TotalGrassrootsLobbyingGrp/AffiliatedGroupTotalAmt 

    TtLbbyExpndMnsLbbyngNnTx_FlngOrgnztnsTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (a)  Description:  Filing organization's totals  most recent xpath: /IRS990ScheduleC/TotLbbyExpendMnsLbbyngNonTxGrp/FilingOrganizationsTotalAmt 

    AvgGrssrtsLbbyngExpnd_CrrntYrMns1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (c)  Description:  Current year minus 1  most recent xpath: /IRS990ScheduleC/AvgGrassrootsLobbyingExpendGrp/CurrentYearMinus1Amt 

    SkdC_LbbyngClngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II-A Line 2b(e)  Description: Lobbying ceiling amount (150% of line 2a(e))  most recent xpath: /IRS990ScheduleC/LobbyingCeilingAmt 

    AvgTtlLbbyngExpnd_CrrntYrMns3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (a)  Description:  Current year minus 3  most recent xpath: /IRS990ScheduleC/AvgTotalLobbyingExpendGrp/CurrentYearMinus3Amt 

    AvgTtlLbbyngExpnd_CrrntYrMns1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (c)  Description:  Current year minus 1  most recent xpath: /IRS990ScheduleC/AvgTotalLobbyingExpendGrp/CurrentYearMinus1Amt 

    GrssrtsNntxbl_AffltdGrpTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (b)  Description:  Affiliated group totals  most recent xpath: /IRS990ScheduleC/GrassrootsNontaxableGrp/AffiliatedGroupTotalAmt 

    AvgGrssrtsNntxbl_CrrntYrMns1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (c)  Description:  Current year minus 1  most recent xpath: /IRS990ScheduleC/AvgGrassrootsNontaxableGrp/CurrentYearMinus1Amt 

    TtlGrssrtsLbbyng_FlngOrgnztnsTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (a)  Description:  Filing organization's totals  most recent xpath: /IRS990ScheduleC/TotalGrassrootsLobbyingGrp/FilingOrganizationsTotalAmt 

    TtlExmptPrpsExpnd_AffltdGrpTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (b)  Description:  Affiliated group totals  most recent xpath: /IRS990ScheduleC/TotalExemptPurposeExpendGrp/AffiliatedGroupTotalAmt 

    LbbyngNntxblAmnt_FlngOrgnztnsTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (a)  Description:  Filing organization's totals  most recent xpath: /IRS990ScheduleC/LobbyingNontaxableAmountGrp/FilingOrganizationsTotalAmt 

    AvgLbbyngNntxblAmnt_CrrntYrMns3Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (a)  Description:  Current year minus 3  most recent xpath: /IRS990ScheduleC/AvgLobbyingNontaxableAmountGrp/CurrentYearMinus3Amt 

    TtlLbbyngExpnd_FlngOrgnztnsTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (a)  Description:  Filing organization's totals  most recent xpath: /IRS990ScheduleC/TotalLobbyingExpendGrp/FilingOrganizationsTotalAmt 

    SkdC_LmtdCntrlPrvsnsAppInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part II-A Line B  Description: Check if "A" is checked and "limited control" provisions apply  most recent xpath: /IRS990ScheduleC/LimitedControlProvisionsAppInd 

    SkdC_Frm4720FldInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part II-A Line 1j  Description: If there is an amount other than zero on either line h or line i, did the organization file Form 4720 reporting section 4911 tax for this year?  most recent xpath: /IRS990ScheduleC/Form4720FiledInd 

    TtLbbyngGrssrtMnsNnTx_FlngOrgnztnsTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (a)  Description:  Filing organization's totals  most recent xpath: /IRS990ScheduleC/TotLbbyngGrassrootMnsNonTxGrp/FilingOrganizationsTotalAmt 

    TtLbbyExpndMnsLbbyngNnTx_AffltdGrpTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (b)  Description:  Affiliated group totals  most recent xpath: /IRS990ScheduleC/TotLbbyExpendMnsLbbyngNonTxGrp/AffiliatedGroupTotalAmt 

    TtlDrctLbbyng_AffltdGrpTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (b)  Description:  Affiliated group totals  most recent xpath: /IRS990ScheduleC/TotalDirectLobbyingGrp/AffiliatedGroupTotalAmt 

    AvgGrssrtsLbbyngExpnd_CrrntYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (d)  Description:  Current year  most recent xpath: /IRS990ScheduleC/AvgGrassrootsLobbyingExpendGrp/CurrentYearAmt 

    GrssrtsNntxbl_FlngOrgnztnsTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (a)  Description:  Filing organization's totals  most recent xpath: /IRS990ScheduleC/GrassrootsNontaxableGrp/FilingOrganizationsTotalAmt 

    TtlExmptPrpsExpnd_FlngOrgnztnsTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (a)  Description:  Filing organization's totals  most recent xpath: /IRS990ScheduleC/TotalExemptPurposeExpendGrp/FilingOrganizationsTotalAmt 

    AvgTtlLbbyngExpnd_CrrntYrMns2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (b)  Description:  Current year minus 2  most recent xpath: /IRS990ScheduleC/AvgTotalLobbyingExpendGrp/CurrentYearMinus2Amt 

    AvgGrssrtsLbbyngExpnd_TtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (e)  Description:  Total  most recent xpath: /IRS990ScheduleC/AvgGrassrootsLobbyingExpendGrp/TotalAmt 

    OthrExmptPrpsExpnd_FlngOrgnztnsTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II-A Column (a)  Description:  Filing organization's totals  most recent xpath: /IRS990ScheduleC/OtherExemptPurposeExpendGrp/FilingOrganizationsTotalAmt 

#######
#
# IRS990ScheduleC - ScheduleC Part II-B : Political Campaign and Lobbying Activities 
#
#######

class skedc_part_iib(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    DrctCntctLgsltrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II-B Line 1g Column (b)  Description: Direct contact with legislators, their staffs, government officials, or a legislative body (only for section 501(c)(3))  most recent xpath: /IRS990ScheduleC/DirectContactLegislatorsAmt 

    RllsDmnstrtnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II-B Line 1h Column (b)  Description: Rallies, demonstrations, seminars, conventions, speeches, lectures, or any other means (only for section 501(c)(3))  most recent xpath: /IRS990ScheduleC/RalliesDemonstrationsAmt 

    GrntsOthrOrgnztnsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part II-B Line 1f Column (a)  Description: Grants to other organizations for lobbying purposes?  most recent xpath: /IRS990ScheduleC/GrantsOtherOrganizationsInd 

    MdAdvrtsmntsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part II-B Line 1c Column(a)  Description: Media advertisements?  most recent xpath: /IRS990ScheduleC/MediaAdvertisementsInd 

    TtlLbbyngExpndtrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II-B Line 1j Column (b)  Description: Total Line 1c through 1i (only for section 501(c)(3))  most recent xpath: /IRS990ScheduleC/TotalLobbyingExpendituresAmt 

    Frm4720Fld4912TxInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part II-B Line 2d Column (a)  Description: If the filing organization incurred a section 4912 tax, did it file Form 4720 for this year?  most recent xpath: /IRS990ScheduleC/Form4720Filed4912TaxInd 

    Tx4912Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II-B Line 2b Column (b)  Description: If "Yes," enter the amount of any tax incurred under section 4912  most recent xpath: /IRS990ScheduleC/Tax4912Amt 

    MlngsMmbrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II-B Line 1d Column (b)  Description: Media advertisements amount (only for section 501(c)(3))  most recent xpath: /IRS990ScheduleC/MailingsMembersAmt 

    MlngsMmbrsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part II-B Line 1d Column (a)  Description: Mailings to members, legislators, or to the public?  most recent xpath: /IRS990ScheduleC/MailingsMembersInd 

    DrctCntctLgsltrsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part II-B Line 1g Column (a)  Description: Direct contact with legislators, their staffs, government officials, or a legislative body?  most recent xpath: /IRS990ScheduleC/DirectContactLegislatorsInd 

    OthrActvtsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II-B Line 1i Column (b)  Description: Other activities amount  most recent xpath: /IRS990ScheduleC/OtherActivitiesAmt 

    PblctnsOrBrdcstAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II-B Line 1e Column (b)  Description: Publications, or published or broadcast statements (only for section 501(c)(3))  most recent xpath: /IRS990ScheduleC/PublicationsOrBroadcastAmt 

    MdAdvrtsmntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II-B Line 1c Column (b)  Description: Media advertisements amount (only for section 501(c)(3))  most recent xpath: /IRS990ScheduleC/MediaAdvertisementsAmt 

    GrntsOthrOrgnztnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II-B Line 1f Column (b)  Description: Grants to other organizations for lobbying purposes (only for section 501(c)(3))  most recent xpath: /IRS990ScheduleC/GrantsOtherOrganizationsAmt 

    VlntrsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part II-B Line 1a Column (a)  Description: Volunteers?  most recent xpath: /IRS990ScheduleC/VolunteersInd 

    RllsDmnstrtnsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part II-B Line 1h Column (a)  Description: Rallies, demonstrations, seminars, conventions, speeches, lectures, or any other means?  most recent xpath: /IRS990ScheduleC/RalliesDemonstrationsInd 

    NtDscrbdSctn501c3Ind = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part II-B Line 2a Column (a)  Description: Did the activities in line 1 cause the organization to be not described in section 501(c)(3)?  most recent xpath: /IRS990ScheduleC/NotDescribedSection501c3Ind 

    Mngrs4912TxAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II-B Line 2c Column (b)  Description: If "Yes," enter the amount of any tax incurred by organization managers under section 4912  most recent xpath: /IRS990ScheduleC/Managers4912TaxAmt 

    OthrActvtsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part II-B Line 1i Column (a)  Description: Other activities?  most recent xpath: /IRS990ScheduleC/OtherActivitiesInd 

    PblctnsOrBrdcstInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part II-B Line 1e Column(a)  Description: Publications, or published or broadcast statements?  most recent xpath: /IRS990ScheduleC/PublicationsOrBroadcastInd 

    PdStffOrMngmntInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part II-B Line 1b Column (a)  Description: Paid staff or management?  most recent xpath: /IRS990ScheduleC/PaidStaffOrManagementInd 

#######
#
# IRS990ScheduleC - ScheduleC Part III-A : Political Campaign and Lobbying Activities 
#
#######

class skedc_part_iiia(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    OnlyInHsLbbyngInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part III-A Line 2  Description: Did the organization make only in-house lobbying expenditures of $2,000 or less?  most recent xpath: /IRS990ScheduleC/OnlyInHouseLobbyingInd 

    SbstntllyAllDsNnddInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part III-A Line 1  Description: Were substantially all (90% or more) dues received nondeductible by members?  most recent xpath: /IRS990ScheduleC/SubstantiallyAllDuesNondedInd 

    AgrCrryvrPrrYrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part III-A Line 3  Description: Did the organization agree to carryover lobbying and political expenditures from the prior year?  most recent xpath: /IRS990ScheduleC/AgreeCarryoverPriorYearInd 

#######
#
# IRS990ScheduleC - ScheduleC Part III-B : Political Campaign and Lobbying Activities 
#
#######

class skedc_part_iiib(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    NnDdctblLbbyngPltclTtAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III-B Line 2c  Description: Total  most recent xpath: /IRS990ScheduleC/NonDeductibleLbbyngPltclTotAmt 

    NnDdctblLbbyngPltclCYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III-B Line 2a  Description: Current year  most recent xpath: /IRS990ScheduleC/NonDeductibleLbbyngPltclCYAmt 

    NnDdLbbyngPltclCyvAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III-B Line 2b  Description: Carryover from last year  most recent xpath: /IRS990ScheduleC/NonDedLbbyngPltclCyovAmt 

    DsAssssmntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III-B Line 1  Description: Dues, assessments and similar amounts from members  most recent xpath: /IRS990ScheduleC/DuesAssessmentsAmt 

    AggrgtRprtdDsNtcAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III-B Line 3  Description: Aggregate amount reported in section 6033(e)(1)(A) notices of nondeductible section 162(e) dues  most recent xpath: /IRS990ScheduleC/AggregateReportedDuesNtcAmt 

    CrrdOvrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III-B Line 4  Description: If notices were sent and the amount on line 2c exceeds the amount on line 3, what portion of that amount does the organization agree to carryover to the reasonable estimate of nondeductible lobbying and political expenditure next year?  most recent xpath: /IRS990ScheduleC/CarriedOverAmt 

    TxblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III-B Line 5  Description: Taxable amount of lobbying and political expenditures (line 2c total minus 3 and 4)  most recent xpath: /IRS990ScheduleC/TaxableAmt 

#######
#
# IRS990ScheduleC - SkdCSctn527PltclOrg - State the names, addresses and Employer Identification Number (EIN) of all section 527 political organizations to which payments were made
# A repeating structure from skedc_part_0
#
#######

class SkdCSctn527PltclOrg(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part I-C Line 5(b)  Description:  Country  most recent xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/ForeignAddress/CountryCd 

    FrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part I-C Line 5(b)  Description:  Address line 1  most recent xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/ForeignAddress/AddressLine1Txt 

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number: Part I-C Line 5(b)  Description:  ZIP code  most recent xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/USAddress/ZIPCd 

    FrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number: Part I-C Line 5(b)  Description:  Postal code  most recent xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/ForeignAddress/ForeignPostalCd 

    FrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number: Part I-C Line 5(b)  Description:  City  most recent xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/ForeignAddress/CityNm 

    FrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number: Part I-C Line 5(b)  Description:  Province or state  most recent xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/ForeignAddress/ProvinceOrStateNm 

    OrgnztnBsnssNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part I-C Line 5(a)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/OrganizationBusinessName/BusinessNameLine1Txt 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number: Part I-C Line 5(b)  Description:  City  most recent xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/USAddress/CityNm 

    Sctn527PltclOrg_PdIntrnlFndsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I-C Line 5(d)  Description:  Amount paid from internal funds  most recent xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/PaidInternalFundsAmt 

    Sctn527PltclOrg_EIN = models.CharField(null=True, blank=True, max_length=9)
    # Line number: Part I-C Line 5(c)  Description:  EIN  most recent xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/EIN 

    OrgnztnBsnssNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part I-C Line 5(a)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/OrganizationBusinessName/BusinessNameLine2Txt 

    Sctn527PltclOrg_CntrbtnsRcvdDlvrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I-C Line 5(e)  Description:  Amount of contributions received and delivered  most recent xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/ContributionsRcvdDlvrAmt 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part I-C Line 5(b)  Description:  Address line 1  most recent xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/USAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part I-C Line 5(b)  Description:  Address line 2  most recent xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/USAddress/AddressLine2Txt 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part I-C Line 5(b)  Description:  State  most recent xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/USAddress/StateAbbreviationCd 

    FrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part I-C Line 5(b)  Description:  Address line 2  most recent xpath: /IRS990ScheduleC/Section527PoliticalOrgGrp/ForeignAddress/AddressLine2Txt 

#######
#
# IRS990ScheduleC - SkdCSpplmntlInfrmtnDtl - Part IV contents
# A repeating structure from skedc_part_iv
#
#######

class SkdCSpplmntlInfrmtnDtl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    ExplntnTxt = models.TextField(null=True, blank=True)
    # Line number: Part IV  Description:  Form, part and line number reference explanation  most recent xpath: /IRS990ScheduleC/SupplementalInformationDetail/ExplanationTxt 

    FrmAndLnRfrncDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part IV  Description:  Form, part and line number reference  most recent xpath: /IRS990ScheduleC/SupplementalInformationDetail/FormAndLineReferenceDesc 

#######
#
# IRS990ScheduleD - ScheduleD Part I Organizations Maintaining Donor Advised Funds or Other Similar Funds or Accounts 
#
#######

class skedd_part_i(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    DnrAdvsdFndsHldCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 1 Column (a)  Description: Enter the total number of donor advised funds maintained at the end of the tax year  most recent xpath: /IRS990ScheduleD/DonorAdvisedFundsHeldCnt 

    FndsAndOthrAccntsCntrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 2 Column (b)  Description: Contributions, gifts, grants, and similar amounts received: funds and other accounts  most recent xpath: /IRS990ScheduleD/FundsAndOtherAccountsContriAmt 

    FndsAndOthrAccntsHldCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 1 Column (b)  Description: Enter the total number of separate accounts for participating donors where donors have the right to provide advice on the use or distribution of funds owned at the end of the tax year  most recent xpath: /IRS990ScheduleD/FundsAndOtherAccountsHeldCnt 

    FndsAndOthrAccntsGrntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 3 Column (b)  Description: Grants from funds and other accounts  most recent xpath: /IRS990ScheduleD/FundsAndOtherAccountsGrantsAmt 

    DsclsdFrChrtblPrpsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 6  Description: Did the organization inform all grantees, donors, and donor advisors in writing that grant funds may be used only for charitable purposes and not for the benefit of the donor or donor advisor?  most recent xpath: /IRS990ScheduleD/DisclosedForCharitablePrpsInd 

    DsclsdOrgLgCtrlInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 5  Description: Did the organization inform all donors and donor advisors in writing that the assets held in DAFs are the organization's property, subject to the organization's exclusive legal control?  most recent xpath: /IRS990ScheduleD/DisclosedOrgLegCtrlInd 

    DnrAdvsdFndsGrntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 3 Column (a)  Description: Grants and allocations from donor advised funds  most recent xpath: /IRS990ScheduleD/DonorAdvisedFundsGrantsAmt 

    DnrAdvsdFndsVlEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 4 Column (a)  Description: Enter the aggregate value of assets held in all donor advised funds at the end of the tax year  most recent xpath: /IRS990ScheduleD/DonorAdvisedFundsVlEOYAmt 

    FndsAndOthrAccntsVlEOYAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 4 Column (b)  Description: Enter the aggregate value of assets held in all funds and other accounts at the end of the tax year  most recent xpath: /IRS990ScheduleD/FundsAndOtherAccountsVlEOYAmt 

    DnrAdvsdFndsCntrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 2 Column (a)  Description: Contributions, gifts, grants, and similar amounts received: donor advised funds  most recent xpath: /IRS990ScheduleD/DonorAdvisedFundsContriAmt 

#######
#
# IRS990ScheduleD - ScheduleD Part II Conservation Easements 
#
#######

class skedd_part_ii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    SttsEsmntsHldCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 4  Description: Number of states in which the organization held an easement  most recent xpath: /IRS990ScheduleD/StatesEasementsHeldCnt 

    TtlAcrgCnt = models.DecimalField(null=True, blank=True, max_digits=22, decimal_places=2)
    # Line number: Part II Line 2b  Description: Total acreage subject to easements  most recent xpath: /IRS990ScheduleD/TotalAcreageCnt 

    HstrcStrctrEsmntsAftrCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 2d  Description: Number of historic structure easements acquired after 8-17-2006  most recent xpath: /IRS990ScheduleD/HistoricStrctrEasementsAftrCnt 

    HstrcLndArInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part II Line 1  Description: Historic land area  most recent xpath: /IRS990ScheduleD/HistoricLandAreaInd 

    HstrcStrctrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part II Line 1  Description: Historic structure  most recent xpath: /IRS990ScheduleD/HistoricStructureInd 

    ExpnssIncrrdEnfrcmntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 7  Description: Amount of expenses incurred in monitoring or enforcing easements during the taxable year  most recent xpath: /IRS990ScheduleD/ExpensesIncurredEnforcementAmt 

    WrttnPlcyMntrngInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part II Line 5  Description: Does the organization have a written policy regarding the periodic monitoring, inspection, and enforcement of the easements it holds?  most recent xpath: /IRS990ScheduleD/WrittenPolicyMonitoringInd 

    MdfdEsmntsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 3  Description: Number of conservation easements modified, transferred, released, or terminated by the organization during the taxable year  most recent xpath: /IRS990ScheduleD/ModifiedEasementsCnt 

    HstrcStrctrEsmntsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 2c  Description: Number of easements on a certified historic structure included in (a)  most recent xpath: /IRS990ScheduleD/HistoricStructureEasementsCnt 

    PrtctnNtrlHbttInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part II Line 1  Description: Protection of natural habitat  most recent xpath: /IRS990ScheduleD/ProtectionNaturalHabitatInd 

    PrsrvtnOpnSpcInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part II Line 1  Description: Preservation of open space  most recent xpath: /IRS990ScheduleD/PreservationOpenSpaceInd 

    PrsrvtnPblcUsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part II Line 1  Description: Preservation for  public use  most recent xpath: /IRS990ScheduleD/PreservationPublicUseInd 

    StffHrsSpntEnfrcmntCnt = models.DecimalField(null=True, blank=True, max_digits=22, decimal_places=2)
    # Line number: Part II Line 6  Description: Staff hours devoted to monitoring or enforcing easements during the year  most recent xpath: /IRS990ScheduleD/StaffHoursSpentEnforcementCnt 

    Sctn170hRqrStsfdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part II Line 8  Description: Does each conservation easement reported on line 2(d) above satisfy the requirements of section 170(h)(4)(B)(i) and 170(h)(4)(B)(ii)?  most recent xpath: /IRS990ScheduleD/Section170hRqrStsfdInd 

    TtlEsmntsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 2a  Description: Total number of easements  most recent xpath: /IRS990ScheduleD/TotalEasementsCnt 

#######
#
# IRS990ScheduleD - ScheduleD Part III Organizations Maintaining Collections of Art, Historical Treasures, or Other Similar Assets 
#
#######

class skedd_part_iii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    CllctnUsdOthrPrpss_OthrPrpssDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part III Line 3e  Description: Collection used for other purposes and description  most recent xpath: /IRS990ScheduleD/CollectionUsedOtherPurposesGrp/OtherPurposesDesc 

    ArtPblcExhbtnAmnts_RvnsInclddAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part III Line 1b(i) OR Line 2a  Description:  Revenues on Form 990, Part VIII, line 1  most recent xpath: /IRS990ScheduleD/ArtPublicExhibitionAmountsGrp/RevenuesIncludedAmt 

    HldWrksArt_AsstsInclddAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part III Line 1b(ii) OR Line 2b  Description:  Assets in Form 990, Part X  most recent xpath: /IRS990ScheduleD/HeldWorksArtGrp/AssetsIncludedAmt 

    HldWrksArt_RvnsInclddAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part III Line 1b(i) OR Line 2a  Description:  Revenues on Form 990, Part VIII, line 1  most recent xpath: /IRS990ScheduleD/HeldWorksArtGrp/RevenuesIncludedAmt 

    SkdD_CllctnUsdPrsrvtnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part III Line 3c  Description: Collection used for preservation  most recent xpath: /IRS990ScheduleD/CollectionUsedPreservationInd 

    SkdD_CllUsdSchlrlyRsrchInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part III Line 3b  Description: Collection used for scholarly research  most recent xpath: /IRS990ScheduleD/CollUsedScholarlyRsrchInd 

    SkdD_CllctnUsdPbExhbtnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part III Line 3a  Description: Collection used for public exhibition  most recent xpath: /IRS990ScheduleD/CollectionUsedPubExhibitionInd 

    CllctnUsdOthrPrpss_CllctnUsdOthrPrpssInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part III Line 3e  Description: Collection used for other purposes and description  most recent xpath: /IRS990ScheduleD/CollectionUsedOtherPurposesGrp/CollectionUsedOtherPurposesInd 

    SkdD_CllUsdLnOrExchPrgInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part III Line 3d  Description: Collection used for loan or exchange programs  most recent xpath: /IRS990ScheduleD/CollUsedLoanOrExchProgInd 

    ArtPblcExhbtnAmnts_AsstsInclddAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part III Line 1b(ii) OR Line 2b  Description:  Assets in Form 990, Part X  most recent xpath: /IRS990ScheduleD/ArtPublicExhibitionAmountsGrp/AssetsIncludedAmt 

    SkdD_SlctdAsstsSlInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part III Line 5  Description: During the year, did the organization solicit or receive donations of art, historical treasures or other similar assets to be sold to raise funds rather than to be maintained as part of the organization's collection?  most recent xpath: /IRS990ScheduleD/SolicitedAssetsSaleInd 

#######
#
# IRS990ScheduleD - ScheduleD Part IV Trust, Escrow and Custodial Arrangements 
#
#######

class skedd_part_iv(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    InclEscrwCstdlAcctLbInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part IV Line 2a  Description: Did the organization include an amount on Form 990, Part X, line 21?  most recent xpath: /IRS990ScheduleD/InclEscrowCustodialAcctLiabInd 

    ExplntnPrvddInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part IV Line 2b  Description: Part XIII contains an explanation for Part IV, Line 2b  most recent xpath: /IRS990ScheduleD/ExplanationProvidedInd 

    BgnnngBlncAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IV Line 1c  Description: Beginning balance  most recent xpath: /IRS990ScheduleD/BeginningBalanceAmt 

    AgntTrstEtcInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part IV Line 1a  Description: Is the organization an agent, trustee, custodian or other intermediary for contributions or other assets not included on Form 990, Part X?  most recent xpath: /IRS990ScheduleD/AgentTrusteeEtcInd 

    EndngBlncAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IV Line 1f  Description: Ending balance  most recent xpath: /IRS990ScheduleD/EndingBalanceAmt 

    AddtnsDrngYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IV Line 1d  Description: Additions during the year  most recent xpath: /IRS990ScheduleD/AdditionsDuringYearAmt 

    DstrbtnsDrngYrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IV Line 1e  Description: Distributions during the year  most recent xpath: /IRS990ScheduleD/DistributionsDuringYearAmt 

#######
#
# IRS990ScheduleD - ScheduleD Part V Endowment Funds 
#
#######

class skedd_part_v(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    SkdD_PrmnntEndwmntBlncEOYPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number: Part V Line 2b  Description: Permanent endowment EOY balance  most recent xpath: /IRS990ScheduleD/PrmnntEndowmentBalanceEOYPct 

    CYMns2YrEndwmtFnd_EndYrBlncAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1g  Description:  End of year balance  most recent xpath: /IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/EndYearBalanceAmt 

    SkdD_EndwmntsHldRltdOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 3a(ii)  Description: Endowments held by related organizations?  most recent xpath: /IRS990ScheduleD/EndowmentsHeldRelatedOrgInd 

    CYEndwmtFnd_EndYrBlncAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1g  Description:  End of year balance  most recent xpath: /IRS990ScheduleD/CYEndwmtFundGrp/EndYearBalanceAmt 

    SkdD_BrdDsgntdBlncEOYPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number: Part V Line 2a  Description: Board designated EOY balance  most recent xpath: /IRS990ScheduleD/BoardDesignatedBalanceEOYPct 

    CYMns3YrEndwmtFnd_OthrExpndtrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1e  Description:  Other expenditures  most recent xpath: /IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/OtherExpendituresAmt 

    CYMns4YrEndwmtFnd_AdmnstrtvExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1f  Description:  Administrative expenses  most recent xpath: /IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/AdministrativeExpensesAmt 

    CYMns1YrEndwmtFnd_AdmnstrtvExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1f  Description:  Administrative expenses  most recent xpath: /IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/AdministrativeExpensesAmt 

    CYMns3YrEndwmtFnd_CntrbtnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1b  Description:  Contributions  most recent xpath: /IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/ContributionsAmt 

    CYMns2YrEndwmtFnd_BgnnngYrBlncAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1a  Description:  Beginning of year balance  most recent xpath: /IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/BeginningYearBalanceAmt 

    SkdD_RltdOrgLstSchRInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 3b  Description: Are related orgs listed on Schedule R?  most recent xpath: /IRS990ScheduleD/RelatedOrgListSchRInd 

    CYMns1YrEndwmtFnd_CntrbtnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1b  Description:  Contributions  most recent xpath: /IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/ContributionsAmt 

    CYMns4YrEndwmtFnd_CntrbtnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1b  Description:  Contributions  most recent xpath: /IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/ContributionsAmt 

    CYMns3YrEndwmtFnd_AdmnstrtvExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1f  Description:  Administrative expenses  most recent xpath: /IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/AdministrativeExpensesAmt 

    CYMns4YrEndwmtFnd_InvstmntErnngsOrLsssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1c  Description:  Investment earnings or losses  most recent xpath: /IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/InvestmentEarningsOrLossesAmt 

    CYMns2YrEndwmtFnd_InvstmntErnngsOrLsssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1c  Description:  Investment earnings or losses  most recent xpath: /IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/InvestmentEarningsOrLossesAmt 

    CYMns2YrEndwmtFnd_OthrExpndtrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1e  Description:  Other expenditures  most recent xpath: /IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/OtherExpendituresAmt 

    CYEndwmtFnd_CntrbtnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1b  Description:  Contributions  most recent xpath: /IRS990ScheduleD/CYEndwmtFundGrp/ContributionsAmt 

    CYMns3YrEndwmtFnd_GrntsOrSchlrshpsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1d  Description:  Grants or scholarships  most recent xpath: /IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/GrantsOrScholarshipsAmt 

    CYMns1YrEndwmtFnd_EndYrBlncAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1g  Description:  End of year balance  most recent xpath: /IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/EndYearBalanceAmt 

    SkdD_TrmEndwmntBlncEOYPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number: Part V Line 2c  Description: Term endowment EOY balance  most recent xpath: /IRS990ScheduleD/TermEndowmentBalanceEOYPct 

    CYMns2YrEndwmtFnd_AdmnstrtvExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1f  Description:  Administrative expenses  most recent xpath: /IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/AdministrativeExpensesAmt 

    CYMns3YrEndwmtFnd_BgnnngYrBlncAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1a  Description:  Beginning of year balance  most recent xpath: /IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/BeginningYearBalanceAmt 

    CYMns1YrEndwmtFnd_BgnnngYrBlncAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1a  Description:  Beginning of year balance  most recent xpath: /IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/BeginningYearBalanceAmt 

    CYMns4YrEndwmtFnd_GrntsOrSchlrshpsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1d  Description:  Grants or scholarships  most recent xpath: /IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/GrantsOrScholarshipsAmt 

    CYMns1YrEndwmtFnd_InvstmntErnngsOrLsssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1c  Description:  Investment earnings or losses  most recent xpath: /IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/InvestmentEarningsOrLossesAmt 

    CYMns1YrEndwmtFnd_OthrExpndtrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1e  Description:  Other expenditures  most recent xpath: /IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/OtherExpendituresAmt 

    CYEndwmtFnd_OthrExpndtrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1e  Description:  Other expenditures  most recent xpath: /IRS990ScheduleD/CYEndwmtFundGrp/OtherExpendituresAmt 

    CYEndwmtFnd_InvstmntErnngsOrLsssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1c  Description:  Investment earnings or losses  most recent xpath: /IRS990ScheduleD/CYEndwmtFundGrp/InvestmentEarningsOrLossesAmt 

    CYEndwmtFnd_BgnnngYrBlncAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1a  Description:  Beginning of year balance  most recent xpath: /IRS990ScheduleD/CYEndwmtFundGrp/BeginningYearBalanceAmt 

    CYMns4YrEndwmtFnd_BgnnngYrBlncAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1a  Description:  Beginning of year balance  most recent xpath: /IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/BeginningYearBalanceAmt 

    CYMns1YrEndwmtFnd_GrntsOrSchlrshpsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1d  Description:  Grants or scholarships  most recent xpath: /IRS990ScheduleD/CYMinus1YrEndwmtFundGrp/GrantsOrScholarshipsAmt 

    CYMns4YrEndwmtFnd_EndYrBlncAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1g  Description:  End of year balance  most recent xpath: /IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/EndYearBalanceAmt 

    CYMns3YrEndwmtFnd_EndYrBlncAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1g  Description:  End of year balance  most recent xpath: /IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/EndYearBalanceAmt 

    CYMns2YrEndwmtFnd_CntrbtnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1b  Description:  Contributions  most recent xpath: /IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/ContributionsAmt 

    CYMns2YrEndwmtFnd_GrntsOrSchlrshpsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1d  Description:  Grants or scholarships  most recent xpath: /IRS990ScheduleD/CYMinus2YrEndwmtFundGrp/GrantsOrScholarshipsAmt 

    CYMns4YrEndwmtFnd_OthrExpndtrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1e  Description:  Other expenditures  most recent xpath: /IRS990ScheduleD/CYMinus4YrEndwmtFundGrp/OtherExpendituresAmt 

    CYEndwmtFnd_GrntsOrSchlrshpsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1d  Description:  Grants or scholarships  most recent xpath: /IRS990ScheduleD/CYEndwmtFundGrp/GrantsOrScholarshipsAmt 

    SkdD_EndwmntsHldUnrltdOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 3a(i)  Description: Endowments held by unrelated organizations?  most recent xpath: /IRS990ScheduleD/EndowmentsHeldUnrelatedOrgInd 

    CYMns3YrEndwmtFnd_InvstmntErnngsOrLsssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1c  Description:  Investment earnings or losses  most recent xpath: /IRS990ScheduleD/CYMinus3YrEndwmtFundGrp/InvestmentEarningsOrLossesAmt 

    CYEndwmtFnd_AdmnstrtvExpnssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 1f  Description:  Administrative expenses  most recent xpath: /IRS990ScheduleD/CYEndwmtFundGrp/AdministrativeExpensesAmt 

#######
#
# IRS990ScheduleD - ScheduleD Part VI Land, Buildings and Equipment 
#
#######

class skedd_part_vi(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    LshldImprvmnts_DprctnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Column (c)  Description:  Depreciation  most recent xpath: /IRS990ScheduleD/LeaseholdImprovementsGrp/DepreciationAmt 

    Eqpmnt_OthrCstOrOthrBssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Column (b)  Description:  Other cost or other basis  most recent xpath: /IRS990ScheduleD/EquipmentGrp/OtherCostOrOtherBasisAmt 

    LshldImprvmnts_OthrCstOrOthrBssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Column (b)  Description:  Other cost or other basis  most recent xpath: /IRS990ScheduleD/LeaseholdImprovementsGrp/OtherCostOrOtherBasisAmt 

    OthrLndBldngs_DprctnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Column (c)  Description:  Depreciation  most recent xpath: /IRS990ScheduleD/OtherLandBuildingsGrp/DepreciationAmt 

    Lnd_OthrCstOrOthrBssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Column (b)  Description:  Other cost or other basis  most recent xpath: /IRS990ScheduleD/LandGrp/OtherCostOrOtherBasisAmt 

    OthrLndBldngs_OthrCstOrOthrBssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Column (b)  Description:  Other cost or other basis  most recent xpath: /IRS990ScheduleD/OtherLandBuildingsGrp/OtherCostOrOtherBasisAmt 

    Lnd_BkVlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Column (d)  Description:  Book value  most recent xpath: /IRS990ScheduleD/LandGrp/BookValueAmt 

    Bldngs_InvstmntCstOrOthrBssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Column (a)  Description:  Investment cost or other basis  most recent xpath: /IRS990ScheduleD/BuildingsGrp/InvestmentCostOrOtherBasisAmt 

    Eqpmnt_BkVlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Column (d)  Description:  Book value  most recent xpath: /IRS990ScheduleD/EquipmentGrp/BookValueAmt 

    Lnd_InvstmntCstOrOthrBssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Column (a)  Description:  Investment cost or other basis  most recent xpath: /IRS990ScheduleD/LandGrp/InvestmentCostOrOtherBasisAmt 

    LshldImprvmnts_InvstmntCstOrOthrBssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Column (a)  Description:  Investment cost or other basis  most recent xpath: /IRS990ScheduleD/LeaseholdImprovementsGrp/InvestmentCostOrOtherBasisAmt 

    LshldImprvmnts_BkVlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Column (d)  Description:  Book value  most recent xpath: /IRS990ScheduleD/LeaseholdImprovementsGrp/BookValueAmt 

    Eqpmnt_InvstmntCstOrOthrBssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Column (a)  Description:  Investment cost or other basis  most recent xpath: /IRS990ScheduleD/EquipmentGrp/InvestmentCostOrOtherBasisAmt 

    Bldngs_BkVlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Column (d)  Description:  Book value  most recent xpath: /IRS990ScheduleD/BuildingsGrp/BookValueAmt 

    SkdD_TtlBkVlLndBldngsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Line 1  Description: Total of book value  most recent xpath: /IRS990ScheduleD/TotalBookValueLandBuildingsAmt 

    Bldngs_OthrCstOrOthrBssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Column (b)  Description:  Other cost or other basis  most recent xpath: /IRS990ScheduleD/BuildingsGrp/OtherCostOrOtherBasisAmt 

    Bldngs_DprctnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Column (c)  Description:  Depreciation  most recent xpath: /IRS990ScheduleD/BuildingsGrp/DepreciationAmt 

    Eqpmnt_DprctnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Column (c)  Description:  Depreciation  most recent xpath: /IRS990ScheduleD/EquipmentGrp/DepreciationAmt 

    OthrLndBldngs_BkVlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Column (d)  Description:  Book value  most recent xpath: /IRS990ScheduleD/OtherLandBuildingsGrp/BookValueAmt 

    OthrLndBldngs_InvstmntCstOrOthrBssAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part VI Column (a)  Description:  Investment cost or other basis  most recent xpath: /IRS990ScheduleD/OtherLandBuildingsGrp/InvestmentCostOrOtherBasisAmt 

#######
#
# IRS990ScheduleD - ScheduleD Part VII Investments, Other Securities
#
#######

class skedd_part_vii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    ClslyHldEqtyIntrsts_MthdVltnCd = models.TextField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Method of valuation  most recent xpath: /IRS990ScheduleD/CloselyHeldEquityInterestsGrp/MethodValuationCd 

    FnnclDrvtvs_MthdVltnCd = models.TextField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Method of valuation  most recent xpath: /IRS990ScheduleD/FinancialDerivativesGrp/MethodValuationCd 

    ClslyHldEqtyIntrsts_BkVlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Book value  most recent xpath: /IRS990ScheduleD/CloselyHeldEquityInterestsGrp/BookValueAmt 

    FnnclDrvtvs_BkVlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Book value  most recent xpath: /IRS990ScheduleD/FinancialDerivativesGrp/BookValueAmt 

    SkdD_TtlBkVlScrtsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VII Column (b)  Description: Total of book value  most recent xpath: /IRS990ScheduleD/TotalBookValueSecuritiesAmt 

#######
#
# IRS990ScheduleD - ScheduleD Part VIII Investments - Program Related 
#
#######

class skedd_part_viii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    TtlBkVlPrgrmRltdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VIII Column (b)  Description: Total of book value  most recent xpath: /IRS990ScheduleD/TotalBookValueProgramRltdAmt 

#######
#
# IRS990ScheduleD - ScheduleD Part IX Other Assets 
#
#######

class skedd_part_ix(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    TtlBkVlOthrAsstsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IX Column (b)  Description: Total book value  most recent xpath: /IRS990ScheduleD/TotalBookValueOtherAssetsAmt 

#######
#
# IRS990ScheduleD - ScheduleD Part X Other Liabilities 
#
#######

class skedd_part_x(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    TtlLbltyAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part X Column (b)  Description: Total of liability amounts  most recent xpath: /IRS990ScheduleD/TotalLiabilityAmt 

    FtntTxtInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part X Line 2  Description: Part XIII contains the text of the footnote for Part X, Line 2  most recent xpath: /IRS990ScheduleD/FootnoteTextInd 

    FdrlIncmTxLbltyAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part X Column (b)  Description: Federal income tax liability  most recent xpath: /IRS990ScheduleD/FederalIncomeTaxLiabilityAmt 

#######
#
# IRS990ScheduleD - ScheduleD Part XI Reconciliation of Revenue per Audited Financial Statements with Revenue per Return 
#
#######

class skedd_part_xi(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    OthrRvnsNtInclddAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 4b  Description: Other revenues not included  most recent xpath: /IRS990ScheduleD/OtherRevenuesNotIncludedAmt 

    InvstmntExpnssNtIncldAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 4a  Description: Investment expenses not included on Form 990, Part VIII, line 7b  most recent xpath: /IRS990ScheduleD/InvestmentExpensesNotIncldAmt 

    RvnNtRprtdFnclStmtAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 4c  Description: Total amounts, add lines 4a and 4b  most recent xpath: /IRS990ScheduleD/RevenueNotReportedFinclStmtAmt 

    TtlRvEtcAdtdFnclStmtAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 1  Description: Total revenue, gains and other support per audited financial statments  most recent xpath: /IRS990ScheduleD/TotalRevEtcAuditedFinclStmtAmt 

    NtUnrlzdGnsInvstAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 2a  Description: Net unrealized gains on investments  most recent xpath: /IRS990ScheduleD/NetUnrealizedGainsInvstAmt 

    TtlRvnPrFrm990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 5  Description: Total revenue (Form 990, Part 1, Line 12). Add lines 3 and 4c  most recent xpath: /IRS990ScheduleD/TotalRevenuePerForm990Amt 

    OthrRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 2d  Description: Other revenues  most recent xpath: /IRS990ScheduleD/OtherRevenueAmt 

    RvnNtRprtdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 2e  Description: Total amounts, add lines 2a through 2d  most recent xpath: /IRS990ScheduleD/RevenueNotReportedAmt 

    RvnSbttlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 3  Description: Part XI line 1 minus Part XI line 2e  most recent xpath: /IRS990ScheduleD/RevenueSubtotalAmt 

    RcvrsPrrYrGrntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 2c  Description: Recoveries of prior year grants  most recent xpath: /IRS990ScheduleD/RecoveriesPriorYearGrantsAmt 

    DntdSrvcsAndUsFcltsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XI Line 2b  Description: Donated services and use of facilities  most recent xpath: /IRS990ScheduleD/DonatedServicesAndUseFcltsAmt 

#######
#
# IRS990ScheduleD - ScheduleD Part XII Reconciliation of Expenses per Audited Financial Statements with Expenses per Return 
#
#######

class skedd_part_xii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    PrrYrAdjstmntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XII Line 2b  Description: Prior year adjustments  most recent xpath: /IRS990ScheduleD/PriorYearAdjustmentsAmt 

    ExpnssSbttlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XII Line 3  Description: Part XII line 1 minus Part XII line 2e  most recent xpath: /IRS990ScheduleD/ExpensesSubtotalAmt 

    TtExpnsEtcAdtdFnclStmtAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XII Line 1  Description: Total Expenses, and Losses per audited financial statments  most recent xpath: /IRS990ScheduleD/TotExpnsEtcAuditedFinclStmtAmt 

    ExpnssNtRptFnclStmtAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XII Line 4c  Description: Total amounts, add lines 4a through 4b  most recent xpath: /IRS990ScheduleD/ExpensesNotRptFinclStmtAmt 

    InvstmntExpnssNtIncld2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XII Line 4a  Description: Investment expenses not included on Form 990, Part VIII, line 7b  most recent xpath: /IRS990ScheduleD/InvestmentExpensesNotIncld2Amt 

    ExpnssNtRprtdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XII Line 2e  Description: Total amounts, add lines 2a through 2d  most recent xpath: /IRS990ScheduleD/ExpensesNotReportedAmt 

    OthrExpnssNtInclddAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XII Line 4b  Description: Other expenses  most recent xpath: /IRS990ScheduleD/OtherExpensesNotIncludedAmt 

    LsssRprtdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XII Line 2c  Description: Losses reported  most recent xpath: /IRS990ScheduleD/LossesReportedAmt 

    DntdSrvcsUsFcltsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XII Line 2a  Description: Donated Services and Use of Facilities  most recent xpath: /IRS990ScheduleD/DonatedServicesUseFcltsAmt 

    OthrExpnssInclddAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XII Line 2d  Description: Other expenses included  most recent xpath: /IRS990ScheduleD/OtherExpensesIncludedAmt 

    TtlExpnssPrFrm990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part XII Line 5  Description: Total expenses (Form 990, Part I, Line 18). Add lines 3 and 4c  most recent xpath: /IRS990ScheduleD/TotalExpensesPerForm990Amt 

#######
#
# IRS990ScheduleD - SkdDOthrScrts
# A repeating structure from skedd_part_vii
#
#######

class SkdDOthrScrts(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    Dsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (a)  Description:  Description  most recent xpath: /IRS990ScheduleD/OtherSecuritiesGrp/Desc 

    MthdVltnCd = models.TextField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Method of valuation  most recent xpath: /IRS990ScheduleD/OtherSecuritiesGrp/MethodValuationCd 

    BkVlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Book value  most recent xpath: /IRS990ScheduleD/OtherSecuritiesGrp/BookValueAmt 

#######
#
# IRS990ScheduleD - SkdDInvstPrgrmRltdOrg
# A repeating structure from skedd_part_viii
#
#######

class SkdDInvstPrgrmRltdOrg(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    MthdVltnCd = models.TextField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Method of valuation  most recent xpath: /IRS990ScheduleD/InvstProgramRelatedOrgGrp/MethodValuationCd 

    Dsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (a)  Description:  Description  most recent xpath: /IRS990ScheduleD/InvstProgramRelatedOrgGrp/Desc 

    BkVlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Book value  most recent xpath: /IRS990ScheduleD/InvstProgramRelatedOrgGrp/BookValueAmt 

#######
#
# IRS990ScheduleD - SkdDOthrAsstsOrg
# A repeating structure from skedd_part_ix
#
#######

class SkdDOthrAsstsOrg(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    Dsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (a)  Description:  Description  most recent xpath: /IRS990ScheduleD/OtherAssetsOrgGrp/Desc 

    BkVlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Book value  most recent xpath: /IRS990ScheduleD/OtherAssetsOrgGrp/BookValueAmt 

#######
#
# IRS990ScheduleD - SkdDOthrLbltsOrg
# A repeating structure from skedd_part_x
#
#######

class SkdDOthrLbltsOrg(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    Dsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (a)  Description:  Description  most recent xpath: /IRS990ScheduleD/OtherLiabilitiesOrgGrp/Desc 

    Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Amount  most recent xpath: /IRS990ScheduleD/OtherLiabilitiesOrgGrp/Amt 

#######
#
# IRS990ScheduleD - SkdDSpplmntlInfrmtnDtl - Part XIII contents
# A repeating structure from skedd_part_xiii
#
#######

class SkdDSpplmntlInfrmtnDtl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    ExplntnTxt = models.TextField(null=True, blank=True)
    # Line number: Part XIII  Description:  Form part and line number reference explanation  most recent xpath: /IRS990ScheduleD/SupplementalInformationDetail/ExplanationTxt 

    FrmAndLnRfrncDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part XIII  Description:  Form part and line number reference  most recent xpath: /IRS990ScheduleD/SupplementalInformationDetail/FormAndLineReferenceDesc 

#######
#
# IRS990ScheduleE - ScheduleE Part I 
#
#######

class skede_part_i(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    DscrmntRcAthltPrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Line 5g  Description: Does the organization discriminate by race in any way athletic programs?  most recent xpath: /IRS990ScheduleE/DiscriminateRaceAthltProgInd 

    DscrmntRcEmplmFcltyInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Line 5c  Description: Does the organization discriminate by race in any way employment of faculty or administrative staff?  most recent xpath: /IRS990ScheduleE/DiscriminateRaceEmplmFcultyInd 

    DscrmntRcSchsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Line 5d  Description: Does the organization discriminate by race in any way scholarships or other financial assistance?  most recent xpath: /IRS990ScheduleE/DiscriminateRaceSchsInd 

    PlcyStmtInBrchrsEtcInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Line 2  Description: Does the organization have policy statement in brochures, etc?  most recent xpath: /IRS990ScheduleE/PolicyStmtInBrochuresEtcInd 

    MntnCpyOfBrchrsEtcInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Line 4c  Description: Does the organization maintain copies of brochures, etc?  most recent xpath: /IRS990ScheduleE/MaintainCpyOfBrochuresEtcInd 

    CmplncWthRvPrc7550Ind = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Line 7  Description: Compliance with Rev. Proc. 75-50, 1975-2 C.B. 587?  most recent xpath: /IRS990ScheduleE/ComplianceWithRevProc7550Ind 

    DscrmntRcOthrActyInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Line 5h  Description: Does the organization discriminate by race in any way other extracurricular activities?  most recent xpath: /IRS990ScheduleE/DiscriminateRaceOtherActyInd 

    MntnRclCmpRcsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Line 4a  Description: Does the organization maintain racial composition records?  most recent xpath: /IRS990ScheduleE/MaintainRacialCompRecsInd 

    DscrmntRcStdntsRghtsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Line 5a  Description: Does the organization discriminate by race in any way students' rights or privileges?  most recent xpath: /IRS990ScheduleE/DiscriminateRaceStdntsRghtsInd 

    PlcyPblczdVBrdcstMdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Line 3  Description: Has the organization publicized the policy through broadcast media?  most recent xpath: /IRS990ScheduleE/PlcyPblczdViaBroadcastMediaInd 

    NndscrmntryPlcyStmtInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Line 1  Description: Does the organization have a racially nondiscriminatory policy statement?  most recent xpath: /IRS990ScheduleE/NondiscriminatoryPolicyStmtInd 

    DscrmntRcEdcPlcyInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Line 5e  Description: Does the organization discriminate by race in any way educational policies?  most recent xpath: /IRS990ScheduleE/DiscriminateRaceEducPlcyInd 

    MntnCpyOfAllSlInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Line 4d  Description: Does the organization maintain copies of all solicitations?  most recent xpath: /IRS990ScheduleE/MaintainCpyOfAllSolInd 

    MntnSchlrshpsRcsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Line 4b  Description: Does the organization maintain scholarships records?  most recent xpath: /IRS990ScheduleE/MaintainScholarshipsRecsInd 

    DscrmntRcAdmssPlcyInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Line 5b  Description: Does the organization discriminate by race in any way admissions policies?  most recent xpath: /IRS990ScheduleE/DiscriminateRaceAdmissPlcyInd 

    GvrnmntFnnclAdRvkdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Line 6b  Description: Has the organization's right to such aid ever been revoked or suspended?  most recent xpath: /IRS990ScheduleE/GovernmentFinancialAidRvkdInd 

    DscrmntRcUsOfFcltsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Line 5f  Description: Does the organization discriminate by race in any way use of facilities?  most recent xpath: /IRS990ScheduleE/DiscriminateRaceUseOfFcltsInd 

    GvrnmntFnnclAdRcvdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Line 6a  Description: Does the organization receive any financial aid or assistance from a governmental agency?  most recent xpath: /IRS990ScheduleE/GovernmentFinancialAidRcvdInd 

#######
#
# IRS990ScheduleE - SkdESpplmntlInfrmtnDtl - Part II contents
# A repeating structure from skede_part_ii
#
#######

class SkdESpplmntlInfrmtnDtl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FrmAndLnRfrncDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part II  Description:  Form, part and line number reference  most recent xpath: /IRS990ScheduleE/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = models.TextField(null=True, blank=True)
    # Line number: Part II  Description:  Form, part, and line number reference explanation  most recent xpath: /IRS990ScheduleE/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleF - ScheduleF Part I General Activities Outside the U.S. 
#
#######

class skedf_part_i(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    CntnttnTtlOffcCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 3b Column (b)  Description: Total offices from continuation sheets to Part I  most recent xpath: /IRS990ScheduleF/ContinutationTotalOfficeCnt 

    TtlOffcCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 3c Column (b)  Description: Total number of offices  most recent xpath: /IRS990ScheduleF/TotalOfficeCnt 

    CntntnSpntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 3b Column (f)  Description: Total amouunt from continuation sheets to Part I  most recent xpath: /IRS990ScheduleF/ContinuationSpentAmt 

    GrntRcrdsMntndInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 1  Description: For grantmakers: Does the organization maintain records to substantiate the amount of the grants or assistance, the grantees' eligibility for the grants or assistance, and the selection criteria used to award the grants or assistance?  most recent xpath: /IRS990ScheduleF/GrantRecordsMaintainedInd 

    TtlSpntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 3c Column (f)  Description: Total amount spent  most recent xpath: /IRS990ScheduleF/TotalSpentAmt 

    SbttlEmplysCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 3a Column (c)  Description: Subtotal number of employees  most recent xpath: /IRS990ScheduleF/SubtotalEmployeesCnt 

    SbttlOffcsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 3a Column (b)  Description: Subtotal number of offices  most recent xpath: /IRS990ScheduleF/SubtotalOfficesCnt 

    TtlEmplyCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 3c Column (c)  Description: Total number of employees  most recent xpath: /IRS990ScheduleF/TotalEmployeeCnt 

    CntnttnTtlEmplyCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 3b Column (c)  Description: Total employees from continuation sheets to Part I  most recent xpath: /IRS990ScheduleF/ContinuationTotalEmployeeCnt 

    CntnttnTtlEmplyCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 3b Column (c)  Description: Total employees from continuation sheets to Part I  most recent xpath: /IRS990ScheduleF/ContinutationTotalEmployeeCnt 

    SbttlSpntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 3a Column (f)  Description: Subtotal amount spent  most recent xpath: /IRS990ScheduleF/SubtotalSpentAmt 

    CntnttnTtlOffcCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 3b Column (b)  Description: Total offices from continuation sheets to Part I  most recent xpath: /IRS990ScheduleF/ContinuationTotalOfficeCnt 

#######
#
# IRS990ScheduleF - ScheduleF Part II Grants and Other Assistance to Organizations or Entities Outside the United States 
#
#######

class skedf_part_ii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    Ttl501c3OrgCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II line 2  Description: Total number of 501(c)(3) organizations  most recent xpath: /IRS990ScheduleF/Total501c3OrgCnt 

    TtlOthrOrgCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II line 3  Description: Total number of other organizations or entities  most recent xpath: /IRS990ScheduleF/TotalOtherOrgCnt 

#######
#
# IRS990ScheduleF - ScheduleF Part IV Foreign Forms 
#
#######

class skedf_part_iv(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FrgnCrpOwnrshpInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part IV Line 3  Description: Did the organization have an ownership interest in a foreign corporation during the tax year?  most recent xpath: /IRS990ScheduleF/ForeignCorpOwnershipInd 

    PssvFrgnInvstmstCInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part IV Line 4  Description: Was the organization a direct or indirect shareholder of a passive foreign investment company or a qualified electing fund during the tax year?  most recent xpath: /IRS990ScheduleF/PassiveForeignInvestmestCoInd 

    FrgnPrtnrshpInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part IV Line 5  Description: Did the organization have an ownership interest in a foreign partnership during the tax year?  most recent xpath: /IRS990ScheduleF/ForeignPartnershipInd 

    BycttCntrsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part IV Line 6  Description: Did the organization have any operations in or related to any boycotting countries during the tax year?  most recent xpath: /IRS990ScheduleF/BoycottCountriesInd 

    IntrstInFrgnTrstInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part IV Line 2  Description: Did the organization have an interest in a foreign trust during the tax year?  most recent xpath: /IRS990ScheduleF/InterestInForeignTrustInd 

    TrnsfrTFrgnCrpInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part IV Line 1  Description: Was the organization a U.S. transferor of property to a foreign corporation during the tax year?  most recent xpath: /IRS990ScheduleF/TransferToForeignCorpInd 

#######
#
# IRS990ScheduleF - SkdFAccntActvtsOtsdUS
# A repeating structure from skedf_part_i
#
#######

class SkdFAccntActvtsOtsdUS(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    RgnTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part I Line 3 Column (a)  Description:  Region  most recent xpath: /IRS990ScheduleF/AccountActivitiesOutsideUSGrp/RegionTxt 

    RgnTtlExpndtrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part I Line 3 Column (f)  Description:  Total expenditures in region  most recent xpath: /IRS990ScheduleF/AccountActivitiesOutsideUSGrp/RegionTotalExpendituresAmt 

    SpcfcSrvcsPrvddTxt = models.TextField(null=True, blank=True)
    # Line number:  Part I Line 3 Column (e)  Description:  If activity listed in (d) is a program service, describe specific type of service(s) in region  most recent xpath: /IRS990ScheduleF/AccountActivitiesOutsideUSGrp/SpecificServicesProvidedTxt 

    OffcsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part I Line 3 Column (b)  Description:  Number of offices in the region  most recent xpath: /IRS990ScheduleF/AccountActivitiesOutsideUSGrp/OfficesCnt 

    OfActvtsCndctdTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part I Line 3 Column (d)  Description:  Activities conducted in region (by type) (i.e., fundraising, program services, grants to recipients located in the region)  most recent xpath: /IRS990ScheduleF/AccountActivitiesOutsideUSGrp/TypeOfActivitiesConductedTxt 

    EmplyCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part I Line 3 Column (c)  Description:  Number of employees or agents in region  most recent xpath: /IRS990ScheduleF/AccountActivitiesOutsideUSGrp/EmployeeCnt 

#######
#
# IRS990ScheduleF - SkdFGrntsTOrgOtsdUS
# A repeating structure from skedf_part_ii
#
#######

class SkdFGrntsTOrgOtsdUS(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    PrpsOfGrntTxt = models.TextField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Purpose of grant  most recent xpath: /IRS990ScheduleF/GrantsToOrgOutsideUSGrp/PurposeOfGrantTxt 

    VltnMthdUsdDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (i)  Description:  Method of valuation  most recent xpath: /IRS990ScheduleF/GrantsToOrgOutsideUSGrp/ValuationMethodUsedDesc 

    DscrptnOfNnCshAsstTxt = models.TextField(null=True, blank=True)
    # Line number:  Column (h)  Description:  Description of non-cash assistance  most recent xpath: /IRS990ScheduleF/GrantsToOrgOutsideUSGrp/DescriptionOfNonCashAsstTxt 

    MnnrOfCshDsbrsmntTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (f)  Description:  Manner of cash disbursement  most recent xpath: /IRS990ScheduleF/GrantsToOrgOutsideUSGrp/MannerOfCashDisbursementTxt 

    CshGrntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Amount of cash grant  most recent xpath: /IRS990ScheduleF/GrantsToOrgOutsideUSGrp/CashGrantAmt 

    RgnTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (c)  Description:  Region  most recent xpath: /IRS990ScheduleF/GrantsToOrgOutsideUSGrp/RegionTxt 

    NnCshAssstncAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (g)  Description:  Amount of non-cash assistance  most recent xpath: /IRS990ScheduleF/GrantsToOrgOutsideUSGrp/NonCashAssistanceAmt 

#######
#
# IRS990ScheduleF - SkdFFrgnIndvdlsGrnts
# A repeating structure from skedf_part_iii
#
#######

class SkdFFrgnIndvdlsGrnts(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    VltnMthdUsdDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (h)  Description:  Method of valuation  most recent xpath: /IRS990ScheduleF/ForeignIndividualsGrantsGrp/ValuationMethodUsedDesc 

    DscrptnOfNnCshAsstTxt = models.TextField(null=True, blank=True)
    # Line number:  Column (g)  Description:  Description of non-cash assistance  most recent xpath: /IRS990ScheduleF/ForeignIndividualsGrantsGrp/DescriptionOfNonCashAsstTxt 

    CshGrntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Amount of cash grant  most recent xpath: /IRS990ScheduleF/ForeignIndividualsGrantsGrp/CashGrantAmt 

    MnnrOfCshDsbrsmntTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (e)  Description:  Manner of cash disbursement  most recent xpath: /IRS990ScheduleF/ForeignIndividualsGrantsGrp/MannerOfCashDisbursementTxt 

    OfAssstncTxt = models.TextField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Type of assistance  most recent xpath: /IRS990ScheduleF/ForeignIndividualsGrantsGrp/TypeOfAssistanceTxt 

    RgnTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (b)  Description:  Region  most recent xpath: /IRS990ScheduleF/ForeignIndividualsGrantsGrp/RegionTxt 

    RcpntCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Number of recipients  most recent xpath: /IRS990ScheduleF/ForeignIndividualsGrantsGrp/RecipientCnt 

    NnCshAssstncAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (f)  Description:  Amount of non-cash assistance  most recent xpath: /IRS990ScheduleF/ForeignIndividualsGrantsGrp/NonCashAssistanceAmt 

#######
#
# IRS990ScheduleF - SkdFSpplmntlInfrmtnDtl - Part V contents
# A repeating structure from skedf_part_v
#
#######

class SkdFSpplmntlInfrmtnDtl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    ExplntnTxt = models.TextField(null=True, blank=True)
    # Line number: Part V  Description:  Form, part and line number reference explanation  most recent xpath: /IRS990ScheduleF/SupplementalInformationDetail/ExplanationTxt 

    FrmAndLnRfrncDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part V  Description:  Form, part and line number reference  most recent xpath: /IRS990ScheduleF/SupplementalInformationDetail/FormAndLineReferenceDesc 

#######
#
# IRS990ScheduleG - ScheduleG Part I Fundraising Activities 
#
#######

class skedg_part_i(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    SlcttnOfGvtGrntsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 1  Description: Solicitation of government grants  most recent xpath: /IRS990ScheduleG/SolicitationOfGovtGrantsInd 

    SpclFndrsngEvntsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 1  Description: Special fundraising events  most recent xpath: /IRS990ScheduleG/SpecialFundraisingEventsInd 

    TtlGrssRcptsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 2b(iv)  Description: Total gross receipts  most recent xpath: /IRS990ScheduleG/TotalGrossReceiptsAmt 

    AgrmtPrfFndrsngActyInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 2a  Description: Did the organization have a written or oral agreement with any individual (including officers, directors, trustees or key employees listed in Form 990, Part VII) or entity in connection with professional fundraising activities?  most recent xpath: /IRS990ScheduleG/AgrmtProfFundraisingActyInd 

    TtlNtTOrgnztnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 2b(vi)  Description: Total net to organization  most recent xpath: /IRS990ScheduleG/TotalNetToOrganizationAmt 

    PhnSlcttnsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 1  Description: Phone solicitations  most recent xpath: /IRS990ScheduleG/PhoneSolicitationsInd 

    SlcttnOfNnGvtGrntsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 1  Description: Solicitation of non-govt grants  most recent xpath: /IRS990ScheduleG/SolicitationOfNonGovtGrantsInd 

    TtlRtndByCntrctrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 2b(v)  Description: Total retained by contractors  most recent xpath: /IRS990ScheduleG/TotalRetainedByContractorsAmt 

    AllSttsCd = models.TextField(null=True, blank=True)
    # Line number: Part I Line 3  Description: Literal for all states  most recent xpath: /IRS990ScheduleG/AllStatesCd 

    InPrsnSlcttnsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 1  Description: In-person solicitations  most recent xpath: /IRS990ScheduleG/InPersonSolicitationsInd 

    EmlSlcttnsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 1  Description: Email solicitations  most recent xpath: /IRS990ScheduleG/EmailSolicitationsInd 

    MlSlcttnsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 1  Description: Mail solicitations  most recent xpath: /IRS990ScheduleG/MailSolicitationsInd 

#######
#
# IRS990ScheduleG - ScheduleG Part II Events 
#
#######

class skedg_part_ii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    DrctExpnsSmmryEvntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 10 Column (d)  Description:  Direct expense summary  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/DirectExpenseSummaryEventsAmt 

    CshPrzsEvnt1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 4 Column (a)  Description:  Cash prizes, event no.1  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/CashPrizesEvent1Amt 

    FdAndBvrgEvnt2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 7 Column (b)  Description:  Food and beverage expenses, event no.2  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/FoodAndBeverageEvent2Amt 

    CshPrzsOthrEvntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 4 Column (c)  Description:  Cash prizes, other events  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/CashPrizesOtherEventsAmt 

    OthrDrctExpnssEvnt2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 9 Column (b)  Description:  Other direct expenses, event no.2  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/OtherDirectExpensesEvent2Amt 

    GrssRcptsTtlAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 1 Column (d)  Description:  Gross receipts, total  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/GrossReceiptsTotalAmt 

    EntrtnmntEvnt1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 8 Column (a)  Description:  Entertainment expenses, event no.1  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/EntertainmentEvent1Amt 

    NtIncmSmmryAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 11 Column (d)  Description:  Net income summary  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/NetIncomeSummaryAmt 

    FdAndBvrgEvnt1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 7 Column (a)  Description:  Food and beverage expenses, event no.1  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/FoodAndBeverageEvent1Amt 

    FdAndBvrgTtlEvntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 7 Column (d)  Description:  Food and beverage costs, total  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/FoodAndBeverageTotalEventsAmt 

    GrssRvnOthrEvntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 3 Column (c)  Description:  Gross revenue, other events  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/GrossRevenueOtherEventsAmt 

    NnCshPrzsEvnt1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 5 Column (a)  Description:  Non-cash prizes, event no.1  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/NonCashPrizesEvent1Amt 

    RntFcltyCstsTtlEvntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 6 Column (d)  Description:  Rent or facility costs, total  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/RentFcltyCostsTotalEventsAmt 

    ChrtblCntrbtnsTtAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 2 Column (d)  Description:  Charitable contributions, total  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/CharitableContributionsTotAmt 

    Evnt1Nm = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (a)  Description:  Name of event no.1  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/Event1Nm 

    OthrDrctExpnssEvnt1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 9 Column (a)  Description:  Other direct expenses, event no.1  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/OtherDirectExpensesEvent1Amt 

    NnCshPrzsOthrEvntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 5 Column (c)  Description:  Non-cash prizes, other events  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/NonCashPrizesOtherEventsAmt 

    RntFcltyCstsEvnt1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 6 Column (a)  Description:  Rent or facility costs, event no.1  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/RentFacilityCostsEvent1Amt 

    EntrtnmntTtlEvntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 8 Column (d)  Description:  Entertainment costs, total  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/EntertainmentTotalEventsAmt 

    CshPrzsEvnt2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 4 Column (b)  Description:  Cash prizes, event no.2  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/CashPrizesEvent2Amt 

    ChrtblCntrEvnt1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 2 Column (a)  Description:  Charitable contributions, event no.1  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/CharitableContriEvent1Amt 

    EntrtnmntEvnt2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 8 Column (b)  Description:  Entertainment expenses, event no.2  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/EntertainmentEvent2Amt 

    RntFcltyCstsEvnt2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 6 Column (b)  Description:  Rent or facility costs, event no.2  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/RentFacilityCostsEvent2Amt 

    GrssRvnEvnt2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 3 Column (b)  Description:  Gross revenue, event no.2  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/GrossRevenueEvent2Amt 

    GrssRcptsOthrEvntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 1 Column (c)  Description:  Gross receipts, other events  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/GrossReceiptsOtherEventsAmt 

    EntrtnmntOthrEvntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 8 Column (c)  Description:  Entertainment expenses, other events  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/EntertainmentOtherEventsAmt 

    OthDrctExpnssTtlEvntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 9 Column (d)  Description:  Other direct expenses, total  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/OthDirectExpnssTotalEventsAmt 

    OthrEvntsTtlCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Other events: total number  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/OtherEventsTotalCnt 

    NnCshPrzsTtlEvntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 5 Column (d)  Description:  Non-cash prizes, total  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/NonCashPrizesTotalEventsAmt 

    OthDrctExpnssOthrEvntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 9 Column (c)  Description:  Other direct expenses, other events  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/OthDirectExpnssOtherEventsAmt 

    FdAndBvrgOthrEvntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 7 Column (c)  Description:  Food and beverage expenses, other events  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/FoodAndBeverageOtherEventsAmt 

    RntFcltyCstsOthrEvntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 6 Column (c)  Description:  Rent or facility costs, other events  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/RentFcltyCostsOtherEventsAmt 

    GrssRvnEvnt1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 3 Column (a)  Description:  Gross revenue, event no.1  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/GrossRevenueEvent1Amt 

    GrssRcptsEvnt1Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 1 Column (a)  Description:  Gross receipts, event no.1  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/GrossReceiptsEvent1Amt 

    ChrtblCntrEvnt2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 2 Column (b)  Description:  Charitable contributions, event no.2  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/CharitableContriEvent2Amt 

    NnCshPrzsEvnt2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 5 Column (b)  Description:  Non-cash prizes, event no.2  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/NonCashPrizesEvent2Amt 

    ChrtblCntrOthrEvntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 2 Column (c)  Description:  Charitable contributions, other events  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/CharitableContriOtherEventsAmt 

    CshPrzsTtlEvntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 4 Column (d)  Description:  Cash prizes, total  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/CashPrizesTotalEventsAmt 

    GrssRvnTtlEvntsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 3 Column (d)  Description:  Gross revenue, total  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/GrossRevenueTotalEventsAmt 

    Evnt2Nm = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (b)  Description:  Name of event no.2  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/Event2Nm 

    GrssRcptsEvnt2Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 1 Column (b)  Description:  Gross receipts, event no.2  most recent xpath: /IRS990ScheduleG/FundraisingEventInformationGrp/GrossReceiptsEvent2Amt 

#######
#
# IRS990ScheduleG - ScheduleG Part III Gaming Information 
#
#######

class skedg_part_iii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    GmngInfrmtn_OthrDrctExpnssBngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 5 Column (a)  Description:  Other direct expenses, bingo  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/OtherDirectExpensesBingoAmt 

    GmngInfrmtn_NnCshPrzsBngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 3 Column (a)  Description:  Non-cash prizes, bingo  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/NonCashPrizesBingoAmt 

    SkdG_ThrdPrtyPrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part III Line 15c  Description: Person name of third party  most recent xpath: /IRS990ScheduleG/ThirdPartyPersonNm 

    GmngMngrBsnssNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part III Line 16  Description:  Business name line 1  most recent xpath: /IRS990ScheduleG/GamingManagerBusinessName/BusinessNameLine1Txt 

    PrsnsWthBksUSAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part III Line 14  Description:  Address line 2  most recent xpath: /IRS990ScheduleG/PersonsWithBooksUSAddress/AddressLine2Txt 

    PrsnsWthBksUSAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number: Part III Line 14  Description:  ZIP code  most recent xpath: /IRS990ScheduleG/PersonsWithBooksUSAddress/ZIPCd 

    SkdG_ChrtblDstrbtnRqrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part III Line 17a  Description: Charitable distributions required?  most recent xpath: /IRS990ScheduleG/CharitableDistributionRqrInd 

    ThrdPrtyFrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part III Line 15c  Description:  Address line 2  most recent xpath: /IRS990ScheduleG/ThirdPartyForeignAddress/AddressLine2Txt 

    GmngInfrmtn_OthrDrctExpnssPllTbsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 5 Column (b)  Description:  Other direct expenses, pull tabs  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/OtherDirectExpensesPullTabsAmt 

    PrsnsWthBksFrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part III Line 14  Description:  Address line 1  most recent xpath: /IRS990ScheduleG/PersonsWithBooksForeignAddress/AddressLine1Txt 

    SkdG_GmngMngrIsEmplyInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part III Line 16  Description: Gaming manager is an employee  most recent xpath: /IRS990ScheduleG/GamingManagerIsEmployeeInd 

    SkdG_DstrbtdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Line 17b  Description: Amount distributed  most recent xpath: /IRS990ScheduleG/DistributedAmt 

    SkdG_ExplntnIfNTxt = models.TextField(null=True, blank=True)
    # Line number: Part III Line 9b  Description: Explanation if no license  most recent xpath: /IRS990ScheduleG/ExplanationIfNoTxt 

    ThrdPrtyUSAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part III Line 15c  Description:  Address line 2  most recent xpath: /IRS990ScheduleG/ThirdPartyUSAddress/AddressLine2Txt 

    GmngInfrmtn_CshPrzsPllTbsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 2 Column (b)  Description:  Cash prizes, pull tabs  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/CashPrizesPullTabsAmt 

    SkdG_GmngRvnRtnBy3PrtyAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Line 15b  Description: Amount of gaming revenue retained by 3rd party  most recent xpath: /IRS990ScheduleG/GamingRevenueRtnBy3PrtyAmt 

    SkdG_GmngMngrPrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part III Line 16  Description: Gaming manager person name  most recent xpath: /IRS990ScheduleG/GamingManagerPersonNm 

    GmngInfrmtn_NtGmngIncmSmmryAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 8  Description:  Net gaming income summary  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/NetGamingIncomeSummaryAmt 

    SkdG_GmngWthNnmmbrsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part III Line 11  Description: Does organization operate gaming activities with nonmembers?  most recent xpath: /IRS990ScheduleG/GamingWithNonmembersInd 

    ThrdPrtyUSAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number: Part III Line 15c  Description:  ZIP code  most recent xpath: /IRS990ScheduleG/ThirdPartyUSAddress/ZIPCd 

    ThrdPrtyUSAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part III Line 15c  Description:  State  most recent xpath: /IRS990ScheduleG/ThirdPartyUSAddress/StateAbbreviationCd 

    SkdG_GmngMngrCmpnstnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Line 16  Description: Gaming manager compensation  most recent xpath: /IRS990ScheduleG/GamingManagerCompensationAmt 

    GmngInfrmtn_CshPrzsTtlGmngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 2 Column (d)  Description:  Cash prizes, total  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/CashPrizesTotalGamingAmt 

    GmngInfrmtn_VlntrLbrOthrGmngPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Line 6 Column (c)  Description:  volunteer labor percentage, other gaming  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/VolunteerLaborOtherGamingPct 

    SkdG_LcnsdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part III Line 9a  Description: Is organization licensed in each state?  most recent xpath: /IRS990ScheduleG/LicensedInd 

    GmngInfrmtn_RntFcltyCstsOthrGmngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 4 Column (c)  Description:  Rent or facility costs, other gaming  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/RentFcltyCostsOtherGamingAmt 

    GmngInfrmtn_GrssRvnPllTbsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 1 Column (b)  Description:  Gross revenue, pull tabs  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/GrossRevenuePullTabsAmt 

    PrsnsWthBksUSAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part III Line 14  Description:  Address line 1  most recent xpath: /IRS990ScheduleG/PersonsWithBooksUSAddress/AddressLine1Txt 

    SkdG_LcnsSspnddEtcInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part III Line 10a  Description: Were any gaming licenses revoked, suspended, or terminated during the tax year?  most recent xpath: /IRS990ScheduleG/LicenseSuspendedEtcInd 

    GmngInfrmtn_VlntrLbrOthrGmngInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Line 6 Column (c)  Description:  volunteer labor, other gaming  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/VolunteerLaborOtherGamingInd 

    SkdG_GmngOwnFcltyPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number: Part III Line 13a  Description: Percentage of gaming in own facility  most recent xpath: /IRS990ScheduleG/GamingOwnFacilityPct 

    SkdG_ExplntnIfYsTxt = models.TextField(null=True, blank=True)
    # Line number: Part III Line 10b  Description: Explanation if license revoked, suspended, or termination  most recent xpath: /IRS990ScheduleG/ExplanationIfYesTxt 

    PrsnsWthBksFrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number: Part III Line 14  Description:  Postal code  most recent xpath: /IRS990ScheduleG/PersonsWithBooksForeignAddress/ForeignPostalCd 

    ThrdPrtyUSAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number: Part III Line 15c  Description:  City  most recent xpath: /IRS990ScheduleG/ThirdPartyUSAddress/CityNm 

    GmngMngrBsnssNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part III Line 16  Description:  Business name line 2  most recent xpath: /IRS990ScheduleG/GamingManagerBusinessName/BusinessNameLine2Txt 

    ThrdPrtyBsnssNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part III Line 15c  Description:  Business name line 1  most recent xpath: /IRS990ScheduleG/ThirdPartyBusinessName/BusinessNameLine1Txt 

    GmngInfrmtn_CshPrzsOthrGmngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 2 Column (c)  Description:  Cash prizes, other gaming  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/CashPrizesOtherGamingAmt 

    SkdG_MmbrOfOthrEnttyInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part III Line 12  Description: Is organization formed to administer charitable gaming?  most recent xpath: /IRS990ScheduleG/MemberOfOtherEntityInd 

    GmngInfrmtn_NnCshPrzsOthrGmngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 3 Column (c)  Description:  Non-cash prizes, other gaming  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/NonCashPrizesOtherGamingAmt 

    ThrdPrtyFrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number: Part III Line 15c  Description:  City  most recent xpath: /IRS990ScheduleG/ThirdPartyForeignAddress/CityNm 

    GmngInfrmtn_DrctExpnsSmmryGmngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 7  Description:  Direct expense summary  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/DirectExpenseSummaryGamingAmt 

    GmngInfrmtn_VlntrLbrBngPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Line 6 Column (a)  Description:  volunteer labor percentage, bingo  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/VolunteerLaborBingoPct 

    SkdG_GmngMngrIsIndCntrctInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part III Line 16  Description: Gaming manager is an independent contractor  most recent xpath: /IRS990ScheduleG/GamingManagerIsIndCntrctInd 

    GmngInfrmtn_GrssRvnTtlGmngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 1 Column (d)  Description:  Gross revenue, total  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/GrossRevenueTotalGamingAmt 

    GmngInfrmtn_RntFcltyCstsPllTbsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 4 Column (b)  Description:  Rent or facility costs, pull tabs  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/RentFacilityCostsPullTabsAmt 

    GmngInfrmtn_CshPrzsBngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 2 Column (a)  Description:  Cash prizes, bingo  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/CashPrizesBingoAmt 

    ThrdPrtyFrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part III Line 15c  Description:  Country  most recent xpath: /IRS990ScheduleG/ThirdPartyForeignAddress/CountryCd 

    GmngInfrmtn_VlntrLbrBngInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Line 6 Column (a)  Description:  volunteer labor, bingo  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/VolunteerLaborBingoInd 

    GmngInfrmtn_OthDrctExpnssOthrGmngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 5 Column (c)  Description:  Other direct expenses, other gaming  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/OthDirectExpnssOtherGamingAmt 

    GmngInfrmtn_RntFcltyCstsTtlGmngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 4 Column (d)  Description:  Rent or facility costs, total  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/RentFcltyCostsTotalGamingAmt 

    ThrdPrtyUSAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part III Line 15c  Description:  Address line 1  most recent xpath: /IRS990ScheduleG/ThirdPartyUSAddress/AddressLine1Txt 

    ThrdPrtyBsnssNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part III Line 15c  Description:  Business name line 2  most recent xpath: /IRS990ScheduleG/ThirdPartyBusinessName/BusinessNameLine2Txt 

    PrsnsWthBksUSAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part III Line 14  Description:  State  most recent xpath: /IRS990ScheduleG/PersonsWithBooksUSAddress/StateAbbreviationCd 

    GmngInfrmtn_NnCshPrzsPllTbsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 3 Column (b)  Description:  Non-cash prizes, pull tabs  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/NonCashPrizesPullTabsAmt 

    SkdG_GmngMngrSrvcsPrvTxt = models.TextField(null=True, blank=True)
    # Line number: Part III Line 16  Description: Gamaing manager services provided  most recent xpath: /IRS990ScheduleG/GamingManagerServicesProvTxt 

    GmngInfrmtn_GrssRvnOthrGmngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 1 Column (c)  Description:  Gross revenue, other gaming  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/GrossRevenueOtherGamingAmt 

    GmngInfrmtn_VlntrLbrPllTbsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Line 6 Column (b)  Description:  volunteer labor percentage, pull tabs  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/VolunteerLaborPullTabsPct 

    PrsnsWthBksNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part III Line 14  Description:  Business name line 2  most recent xpath: /IRS990ScheduleG/PersonsWithBooksName/BusinessNameLine2Txt 

    PrsnsWthBksFrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number: Part III Line 14  Description:  Province or state  most recent xpath: /IRS990ScheduleG/PersonsWithBooksForeignAddress/ProvinceOrStateNm 

    PrsnsWthBksNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part III Line 14  Description:  Business name line 1  most recent xpath: /IRS990ScheduleG/PersonsWithBooksName/BusinessNameLine1Txt 

    GmngInfrmtn_OthDrctExpnssTtlGmngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 5 Column (d)  Description:  Other direct expenses, total  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/OthDirectExpnssTotalGamingAmt 

    PrsnsWthBksFrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part III Line 14  Description:  Address line 2  most recent xpath: /IRS990ScheduleG/PersonsWithBooksForeignAddress/AddressLine2Txt 

    GmngInfrmtn_RntFcltyCstsBngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 4 Column (a)  Description:  Rent or facility costs, bingo  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/RentFacilityCostsBingoAmt 

    PrsnsWthBksUSAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number: Part III Line 14  Description:  City  most recent xpath: /IRS990ScheduleG/PersonsWithBooksUSAddress/CityNm 

    SkdG_GmngRvnRcvdByOrgAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Line 15b  Description: Amount of gaming revenue received by organization  most recent xpath: /IRS990ScheduleG/GamingRevenueReceivedByOrgAmt 

    ThrdPrtyFrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number: Part III Line 15c  Description:  Postal code  most recent xpath: /IRS990ScheduleG/ThirdPartyForeignAddress/ForeignPostalCd 

    ThrdPrtyFrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part III Line 15c  Description:  Address line 1  most recent xpath: /IRS990ScheduleG/ThirdPartyForeignAddress/AddressLine1Txt 

    SkdG_GmngOthrFcltyPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number: Part III Line 13b  Description: Percentage of gaming in other facility  most recent xpath: /IRS990ScheduleG/GamingOtherFacilityPct 

    GmngInfrmtn_GrssRvnBngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 1 Column (a)  Description:  Gross revenue, bingo  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/GrossRevenueBingoAmt 

    PrsnsWthBksFrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number: Part III Line 14  Description:  City  most recent xpath: /IRS990ScheduleG/PersonsWithBooksForeignAddress/CityNm 

    ThrdPrtyFrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number: Part III Line 15c  Description:  Province or state  most recent xpath: /IRS990ScheduleG/ThirdPartyForeignAddress/ProvinceOrStateNm 

    SkdG_CntrctWth3rdPrtyFrGmRvInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part III Line 15a  Description: Is there a third party contract for gaming revenue?  most recent xpath: /IRS990ScheduleG/CntrctWith3rdPrtyForGameRevInd 

    GmngInfrmtn_NnCshPrzsTtlGmngAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Line 3 Column (d)  Description:  Non-cash prizes, total  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/NonCashPrizesTotalGamingAmt 

    PrsnsWthBksFrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part III Line 14  Description:  Country  most recent xpath: /IRS990ScheduleG/PersonsWithBooksForeignAddress/CountryCd 

    SkdG_GmngMngrIsDrctrOfcrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part III Line 16  Description: Gaming manager is a director or officer  most recent xpath: /IRS990ScheduleG/GamingManagerIsDirectorOfcrInd 

    SkdG_IndvdlWthBksNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part III Line 14  Description: Person name of gaming records keeper  most recent xpath: /IRS990ScheduleG/IndividualWithBooksNm 

    GmngInfrmtn_VlntrLbrPllTbsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Line 6 Column (b)  Description:  volunteer labor, pull tabs  most recent xpath: /IRS990ScheduleG/GamingInformationGrp/VolunteerLaborPullTabsInd 

#######
#
# IRS990ScheduleG - SkdGFndrsrActvtyInf
# A repeating structure from skedg_part_i
#
#######

class SkdGFndrsrActvtyInf(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FndrsrActvtyInf_RtndByCntrctrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part I Line 2b(v)  Description:  Amount paid to (or retained by) fundraiser listed in (i)  most recent xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/RetainedByContractorAmt 

    FndrsrActvtyInf_ActvtyTxt = models.TextField(null=True, blank=True)
    # Line number:  Line 2b Column (ii)  Description:  Activity  most recent xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/ActivityTxt 

    FndrsrActvtyInf_GrssRcptsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part I Line 2b(iv)  Description:  Gross receipts from activity  most recent xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/GrossReceiptsAmt 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Line 2b Column (i)  Description:  Address line 2  most recent xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/USAddress/AddressLine2Txt 

    FrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Line 2b Column (i)  Description:  Address line 1  most recent xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/ForeignAddress/AddressLine1Txt 

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number:  Line 2b Column (i)  Description:  ZIP code  most recent xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/USAddress/ZIPCd 

    FrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number:  Line 2b Column (i)  Description:  City  most recent xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/ForeignAddress/CityNm 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number:  Line 2b Column (i)  Description:  City  most recent xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Line 2b Column (i)  Description:  State  most recent xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/USAddress/StateAbbreviationCd 

    FndrsrActvtyInf_NtTOrgnztnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part I Line 2b(vi)  Description:  Amount paid to (or retained by) organization  most recent xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/NetToOrganizationAmt 

    FrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number:  Line 2b Column (i)  Description:  Province or state  most recent xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/ForeignAddress/ProvinceOrStateNm 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Line 2b Column (i)  Description:  Address line 1  most recent xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/USAddress/AddressLine1Txt 

    OrgnztnBsnssNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Line 2b Column (i)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/OrganizationBusinessName/BusinessNameLine2Txt 

    OrgnztnBsnssNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Line 2b Column (i)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/OrganizationBusinessName/BusinessNameLine1Txt 

    FrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Line 2b Column (i)  Description:  Country  most recent xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/ForeignAddress/CountryCd 

    FrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Line 2b Column (i)  Description:  Address line 2  most recent xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/ForeignAddress/AddressLine2Txt 

    FndrsrActvtyInf_FndrsrCntrlOfFndsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Line 2b Column (iii)  Description:  Fundraiser control of funds?  most recent xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/FundraiserControlOfFundsInd 

    FndrsrActvtyInf_PrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Line 2b Column (i)  Description:  Name of individual  most recent xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/PersonNm 

    FrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number:  Line 2b Column (i)  Description:  Postal code  most recent xpath: /IRS990ScheduleG/FundraiserActivityInfoGrp/ForeignAddress/ForeignPostalCd 

#######
#
# IRS990ScheduleG - SkdGLcnsdSttsCd - List all states in which the organization is registered or licensed to solicit funds or has been notified it is exempt from registration or licensing
# A repeating structure from skedg_part_i
#
#######

class SkdGLcnsdSttsCd(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    LcnsdSttsCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part I Line 3  Description: List all states in which the organization is registered or licensed to solicit funds or has been notified it is exempt from registration or licensing  most recent xpath: /IRS990ScheduleG/LicensedStatesCd 

#######
#
# IRS990ScheduleG - SkdGSttsWhrGmngCndctdCd - Enter state where organization conducts gaming activities
# A repeating structure from skedg_part_iii
#
#######

class SkdGSttsWhrGmngCndctdCd(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    SttsWhrGmngCndctdCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part III Line 9  Description: Enter state where organization conducts gaming activities  most recent xpath: /IRS990ScheduleG/StatesWhereGamingConductedCd 

#######
#
# IRS990ScheduleG - SkdGSpplmntlInfrmtnDtl - Part IV contents
# A repeating structure from skedg_part_iv
#
#######

class SkdGSpplmntlInfrmtnDtl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FrmAndLnRfrncDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part IV  Description:  Form, part and line number reference  most recent xpath: /IRS990ScheduleG/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = models.TextField(null=True, blank=True)
    # Line number: Part IV  Description:  Form, part and line number reference explanation  most recent xpath: /IRS990ScheduleG/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleH - ScheduleH Part I - Community Benefit Report 
#
#######

class skedh_part_i(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    TtlCmmntyBnfts_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community benefit expense  most recent xpath: /IRS990ScheduleH/TotalCommunityBenefitsGrp/NetCommunityBenefitExpnsAmt 

    CmmntyHlthSrvcs_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community benefit expense  most recent xpath: /IRS990ScheduleH/CommunityHealthServicesGrp/NetCommunityBenefitExpnsAmt 

    CmmntyHlthSrvcs_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/CommunityHealthServicesGrp/PersonsServedCnt 

    CmmntyHlthSrvcs_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/CommunityHealthServicesGrp/DirectOffsettingRevenueAmt 

    SkdH_FPGRfrncFrCrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 3a  Description: FPG reference free care?  most recent xpath: /IRS990ScheduleH/FPGReferenceFreeCareInd 

    Rsrch_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community benefit expense  most recent xpath: /IRS990ScheduleH/ResearchGrp/TotalCommunityBenefitExpnsAmt 

    UnrmbrsdCsts_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community benefit expense  most recent xpath: /IRS990ScheduleH/UnreimbursedCostsGrp/TotalCommunityBenefitExpnsAmt 

    TtlOthrBnfts_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community benefit expense  most recent xpath: /IRS990ScheduleH/TotalOtherBenefitsGrp/NetCommunityBenefitExpnsAmt 

    TtlFnnclAssstncTyp_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/TotalFinancialAssistanceTyp/TotalExpensePct 

    UnrmbrsdCsts_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/UnreimbursedCostsGrp/DirectOffsettingRevenueAmt 

    UnrmbrsdMdcd_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community benefit expense  most recent xpath: /IRS990ScheduleH/UnreimbursedMedicaidGrp/TotalCommunityBenefitExpnsAmt 

    FnnclAssstncAtCstTyp_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/FinancialAssistanceAtCostTyp/DirectOffsettingRevenueAmt 

    HlthPrfssnsEdctn_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/HealthProfessionsEducationGrp/ActivitiesOrProgramsCnt 

    CshAndInKndCntrbtns_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/CashAndInKindContributionsGrp/PersonsServedCnt 

    HlthPrfssnsEdctn_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community benefit expense  most recent xpath: /IRS990ScheduleH/HealthProfessionsEducationGrp/NetCommunityBenefitExpnsAmt 

    SkdH_Prcnt200DInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 3b  Description: 200%  most recent xpath: /IRS990ScheduleH/Percent200DInd 

    SkdH_MstHsptlsPlcyInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 2  Description: Policy applied to most hospitals  most recent xpath: /IRS990ScheduleH/MostHospitalsPolicyInd 

    CshAndInKndCntrbtns_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/CashAndInKindContributionsGrp/TotalExpensePct 

    SbsdzdHlthSrvcs_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/SubsidizedHealthServicesGrp/TotalExpensePct 

    CmmntyHlthSrvcs_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/CommunityHealthServicesGrp/TotalExpensePct 

    CshAndInKndCntrbtns_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/CashAndInKindContributionsGrp/DirectOffsettingRevenueAmt 

    HlthPrfssnsEdctn_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/HealthProfessionsEducationGrp/TotalExpensePct 

    FrCrOthPrcntg_OthrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 3a  Description: Other  most recent xpath: /IRS990ScheduleH/FreeCareOthPercentageGrp/OtherInd 

    TtlOthrBnfts_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/TotalOtherBenefitsGrp/ActivitiesOrProgramsCnt 

    SbsdzdHlthSrvcs_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/SubsidizedHealthServicesGrp/ActivitiesOrProgramsCnt 

    DscntdCrOthPrcntg_DscntdCrOthrPct = models.DecimalField(null=True, blank=True, max_digits=22, decimal_places=12)
    # Line number: Part I Line 3b  Description: Discounted other percentage  most recent xpath: /IRS990ScheduleH/DiscountedCareOthPercentageGrp/DiscountedCareOtherPct 

    UnrmbrsdMdcd_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/UnreimbursedMedicaidGrp/PersonsServedCnt 

    UnrmbrsdMdcd_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/UnreimbursedMedicaidGrp/ActivitiesOrProgramsCnt 

    SbsdzdHlthSrvcs_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community benefit expense  most recent xpath: /IRS990ScheduleH/SubsidizedHealthServicesGrp/NetCommunityBenefitExpnsAmt 

    SkdH_RprtPblcllyAvlblInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 6b  Description: Report publically available?  most recent xpath: /IRS990ScheduleH/ReportPublicallyAvailableInd 

    TtlOthrBnfts_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/TotalOtherBenefitsGrp/DirectOffsettingRevenueAmt 

    SkdH_IndvHsptlTlrdPlcyInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 2  Description: Policy tailored to individual hospitals  most recent xpath: /IRS990ScheduleH/IndivHospitalTailoredPolicyInd 

    TtlCmmntyBnfts_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community benefit expense  most recent xpath: /IRS990ScheduleH/TotalCommunityBenefitsGrp/TotalCommunityBenefitExpnsAmt 

    SkdH_FrCrMdcllyIndgntInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 4  Description: Free or discounted care to medically indigent?  most recent xpath: /IRS990ScheduleH/FreeCareMedicallyIndigentInd 

    SkdH_ExpnssExcdBdgtInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 5b  Description: Expenses exceeded budget?  most recent xpath: /IRS990ScheduleH/ExpensesExceedBudgetInd 

    Rsrch_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/ResearchGrp/TotalExpensePct 

    TtlCmmntyBnfts_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/TotalCommunityBenefitsGrp/PersonsServedCnt 

    TtlFnnclAssstncTyp_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/TotalFinancialAssistanceTyp/DirectOffsettingRevenueAmt 

    Rsrch_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community benefit expense  most recent xpath: /IRS990ScheduleH/ResearchGrp/NetCommunityBenefitExpnsAmt 

    CmmntyHlthSrvcs_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/CommunityHealthServicesGrp/ActivitiesOrProgramsCnt 

    FnnclAssstncAtCstTyp_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/FinancialAssistanceAtCostTyp/ActivitiesOrProgramsCnt 

    SkdH_Prcnt200Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 3a  Description: 200%  most recent xpath: /IRS990ScheduleH/Percent200Ind 

    TtlCmmntyBnfts_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/TotalCommunityBenefitsGrp/TotalExpensePct 

    UnrmbrsdMdcd_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community benefit expense  most recent xpath: /IRS990ScheduleH/UnreimbursedMedicaidGrp/NetCommunityBenefitExpnsAmt 

    TtlCmmntyBnfts_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/TotalCommunityBenefitsGrp/DirectOffsettingRevenueAmt 

    DscntdCrOthPrcntg_OthrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 3b  Description: Other  most recent xpath: /IRS990ScheduleH/DiscountedCareOthPercentageGrp/OtherInd 

    SkdH_UnblTPrvdCrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 5c  Description: Unable to provide care?  most recent xpath: /IRS990ScheduleH/UnableToProvideCareInd 

    TtlFnnclAssstncTyp_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/TotalFinancialAssistanceTyp/PersonsServedCnt 

    FrCrOthPrcntg_FrCrOthrPct = models.DecimalField(null=True, blank=True, max_digits=22, decimal_places=12)
    # Line number: Part I Line 3a  Description: Free other percentage  most recent xpath: /IRS990ScheduleH/FreeCareOthPercentageGrp/FreeCareOtherPct 

    SbsdzdHlthSrvcs_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/SubsidizedHealthServicesGrp/PersonsServedCnt 

    CshAndInKndCntrbtns_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community benefit expense  most recent xpath: /IRS990ScheduleH/CashAndInKindContributionsGrp/NetCommunityBenefitExpnsAmt 

    Rsrch_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/ResearchGrp/DirectOffsettingRevenueAmt 

    TtlFnnclAssstncTyp_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/TotalFinancialAssistanceTyp/ActivitiesOrProgramsCnt 

    UnrmbrsdMdcd_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/UnreimbursedMedicaidGrp/TotalExpensePct 

    SkdH_Prcnt100Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 3a  Description: 100%  most recent xpath: /IRS990ScheduleH/Percent100Ind 

    SkdH_AnnlCmmntyBnftRprtInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 6a  Description: Annual community benefit report?  most recent xpath: /IRS990ScheduleH/AnnualCommunityBnftReportInd 

    SkdH_Prcnt250Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 3b  Description: 250%  most recent xpath: /IRS990ScheduleH/Percent250Ind 

    UnrmbrsdCsts_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community benefit expense  most recent xpath: /IRS990ScheduleH/UnreimbursedCostsGrp/NetCommunityBenefitExpnsAmt 

    TtlFnnclAssstncTyp_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community benefit expense  most recent xpath: /IRS990ScheduleH/TotalFinancialAssistanceTyp/NetCommunityBenefitExpnsAmt 

    FnnclAssstncAtCstTyp_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/FinancialAssistanceAtCostTyp/TotalExpensePct 

    TtlOthrBnfts_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/TotalOtherBenefitsGrp/TotalExpensePct 

    TtlOthrBnfts_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community benefit expense  most recent xpath: /IRS990ScheduleH/TotalOtherBenefitsGrp/TotalCommunityBenefitExpnsAmt 

    SkdH_WrttnPlcyInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 1b  Description: Written policy?  most recent xpath: /IRS990ScheduleH/WrittenPolicyInd 

    Rsrch_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/ResearchGrp/PersonsServedCnt 

    Rsrch_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/ResearchGrp/ActivitiesOrProgramsCnt 

    CmmntyHlthSrvcs_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community benefit expense  most recent xpath: /IRS990ScheduleH/CommunityHealthServicesGrp/TotalCommunityBenefitExpnsAmt 

    SkdH_Prcnt300Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 3b  Description: 300%  most recent xpath: /IRS990ScheduleH/Percent300Ind 

    FnnclAssstncAtCstTyp_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community benefit expense  most recent xpath: /IRS990ScheduleH/FinancialAssistanceAtCostTyp/TotalCommunityBenefitExpnsAmt 

    UnrmbrsdCsts_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/UnreimbursedCostsGrp/TotalExpensePct 

    FnnclAssstncAtCstTyp_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/FinancialAssistanceAtCostTyp/PersonsServedCnt 

    TtlFnnclAssstncTyp_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community benefit expense  most recent xpath: /IRS990ScheduleH/TotalFinancialAssistanceTyp/TotalCommunityBenefitExpnsAmt 

    SkdH_Prcnt350Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 3b  Description: 350%  most recent xpath: /IRS990ScheduleH/Percent350Ind 

    SkdH_FnnclAssstncPlcyInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 1a  Description: Financial assistance policy?  most recent xpath: /IRS990ScheduleH/FinancialAssistancePolicyInd 

    HlthPrfssnsEdctn_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/HealthProfessionsEducationGrp/PersonsServedCnt 

    UnrmbrsdMdcd_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/UnreimbursedMedicaidGrp/DirectOffsettingRevenueAmt 

    TtlOthrBnfts_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/TotalOtherBenefitsGrp/PersonsServedCnt 

    HlthPrfssnsEdctn_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/HealthProfessionsEducationGrp/DirectOffsettingRevenueAmt 

    SkdH_Prcnt400Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 3b  Description: 400%  most recent xpath: /IRS990ScheduleH/Percent400Ind 

    SbsdzdHlthSrvcs_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community benefit expense  most recent xpath: /IRS990ScheduleH/SubsidizedHealthServicesGrp/TotalCommunityBenefitExpnsAmt 

    SkdH_FPGRfrncDscntdCrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 3b  Description: FPG reference discounted care  most recent xpath: /IRS990ScheduleH/FPGReferenceDiscountedCareInd 

    SbsdzdHlthSrvcs_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/SubsidizedHealthServicesGrp/DirectOffsettingRevenueAmt 

    SkdH_AllHsptlsPlcyInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 2  Description: Policy applied to all hospitals  most recent xpath: /IRS990ScheduleH/AllHospitalsPolicyInd 

    UnrmbrsdCsts_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/UnreimbursedCostsGrp/PersonsServedCnt 

    CshAndInKndCntrbtns_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/CashAndInKindContributionsGrp/ActivitiesOrProgramsCnt 

    FnnclAssstncAtCstTyp_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community benefit expense  most recent xpath: /IRS990ScheduleH/FinancialAssistanceAtCostTyp/NetCommunityBenefitExpnsAmt 

    TtlCmmntyBnfts_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/TotalCommunityBenefitsGrp/ActivitiesOrProgramsCnt 

    SkdH_FnnclAssstncBdgtInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 5a  Description: Amounts budgeted for financial assistance?  most recent xpath: /IRS990ScheduleH/FinancialAssistanceBudgetInd 

    UnrmbrsdCsts_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/UnreimbursedCostsGrp/ActivitiesOrProgramsCnt 

    SkdH_Prcnt150Ind = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 3a  Description: 150%  most recent xpath: /IRS990ScheduleH/Percent150Ind 

    HlthPrfssnsEdctn_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community benefit expense  most recent xpath: /IRS990ScheduleH/HealthProfessionsEducationGrp/TotalCommunityBenefitExpnsAmt 

    CshAndInKndCntrbtns_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community benefit expense  most recent xpath: /IRS990ScheduleH/CashAndInKindContributionsGrp/TotalCommunityBenefitExpnsAmt 

#######
#
# IRS990ScheduleH - ScheduleH Part II 
#
#######

class skedh_part_ii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    LdrshpDvlpmnt_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/LeadershipDevelopmentGrp/TotalExpensePct 

    TtlCmmnttyBldngActy_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/TotalCommuntityBuildingActyGrp/ActivitiesOrProgramsCnt 

    LdrshpDvlpmnt_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/LeadershipDevelopmentGrp/ActivitiesOrProgramsCnt 

    HlthImprvmntAdvccy_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/HealthImprovementAdvocacyGrp/TotalExpensePct 

    PhysclImprvAndHsng_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community building expense  most recent xpath: /IRS990ScheduleH/PhysicalImprvAndHousingGrp/NetCommunityBenefitExpnsAmt 

    TtlCmmnttyBldngActy_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community building expense  most recent xpath: /IRS990ScheduleH/TotalCommuntityBuildingActyGrp/NetCommunityBenefitExpnsAmt 

    LdrshpDvlpmnt_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/LeadershipDevelopmentGrp/DirectOffsettingRevenueAmt 

    EcnmcDvlpmnt_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community building expense  most recent xpath: /IRS990ScheduleH/EconomicDevelopmentGrp/TotalCommunityBenefitExpnsAmt 

    LdrshpDvlpmnt_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/LeadershipDevelopmentGrp/PersonsServedCnt 

    EcnmcDvlpmnt_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/EconomicDevelopmentGrp/PersonsServedCnt 

    PhysclImprvAndHsng_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/PhysicalImprvAndHousingGrp/ActivitiesOrProgramsCnt 

    HlthImprvmntAdvccy_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/HealthImprovementAdvocacyGrp/PersonsServedCnt 

    WrkfrcDvlpmnt_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/WorkforceDevelopmentGrp/PersonsServedCnt 

    CmmntySpprt_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/CommunitySupportGrp/DirectOffsettingRevenueAmt 

    OthrCmmnttyBldngActy_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/OtherCommuntityBuildingActyGrp/PersonsServedCnt 

    OthrCmmnttyBldngActy_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community building expense  most recent xpath: /IRS990ScheduleH/OtherCommuntityBuildingActyGrp/NetCommunityBenefitExpnsAmt 

    PhysclImprvAndHsng_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/PhysicalImprvAndHousingGrp/DirectOffsettingRevenueAmt 

    EnvrnmntlImprvmnts_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/EnvironmentalImprovementsGrp/DirectOffsettingRevenueAmt 

    WrkfrcDvlpmnt_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/WorkforceDevelopmentGrp/TotalExpensePct 

    CmmntySpprt_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/CommunitySupportGrp/PersonsServedCnt 

    LdrshpDvlpmnt_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community building expense  most recent xpath: /IRS990ScheduleH/LeadershipDevelopmentGrp/NetCommunityBenefitExpnsAmt 

    WrkfrcDvlpmnt_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/WorkforceDevelopmentGrp/DirectOffsettingRevenueAmt 

    TtlCmmnttyBldngActy_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/TotalCommuntityBuildingActyGrp/DirectOffsettingRevenueAmt 

    PhysclImprvAndHsng_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community building expense  most recent xpath: /IRS990ScheduleH/PhysicalImprvAndHousingGrp/TotalCommunityBenefitExpnsAmt 

    CltnBldng_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/CoalitionBuildingGrp/ActivitiesOrProgramsCnt 

    EcnmcDvlpmnt_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/EconomicDevelopmentGrp/TotalExpensePct 

    WrkfrcDvlpmnt_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/WorkforceDevelopmentGrp/ActivitiesOrProgramsCnt 

    OthrCmmnttyBldngActy_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/OtherCommuntityBuildingActyGrp/ActivitiesOrProgramsCnt 

    EcnmcDvlpmnt_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/EconomicDevelopmentGrp/DirectOffsettingRevenueAmt 

    OthrCmmnttyBldngActy_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/OtherCommuntityBuildingActyGrp/DirectOffsettingRevenueAmt 

    PhysclImprvAndHsng_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/PhysicalImprvAndHousingGrp/TotalExpensePct 

    LdrshpDvlpmnt_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community building expense  most recent xpath: /IRS990ScheduleH/LeadershipDevelopmentGrp/TotalCommunityBenefitExpnsAmt 

    TtlCmmnttyBldngActy_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community building expense  most recent xpath: /IRS990ScheduleH/TotalCommuntityBuildingActyGrp/TotalCommunityBenefitExpnsAmt 

    EnvrnmntlImprvmnts_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community building expense  most recent xpath: /IRS990ScheduleH/EnvironmentalImprovementsGrp/NetCommunityBenefitExpnsAmt 

    OthrCmmnttyBldngActy_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community building expense  most recent xpath: /IRS990ScheduleH/OtherCommuntityBuildingActyGrp/TotalCommunityBenefitExpnsAmt 

    CmmntySpprt_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/CommunitySupportGrp/TotalExpensePct 

    EnvrnmntlImprvmnts_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/EnvironmentalImprovementsGrp/TotalExpensePct 

    EnvrnmntlImprvmnts_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/EnvironmentalImprovementsGrp/PersonsServedCnt 

    EcnmcDvlpmnt_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/EconomicDevelopmentGrp/ActivitiesOrProgramsCnt 

    TtlCmmnttyBldngActy_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/TotalCommuntityBuildingActyGrp/TotalExpensePct 

    HlthImprvmntAdvccy_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community building expense  most recent xpath: /IRS990ScheduleH/HealthImprovementAdvocacyGrp/TotalCommunityBenefitExpnsAmt 

    CmmntySpprt_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/CommunitySupportGrp/ActivitiesOrProgramsCnt 

    OthrCmmnttyBldngActy_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/OtherCommuntityBuildingActyGrp/TotalExpensePct 

    CltnBldng_TtlExpnsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Column (f)  Description:  Percent of total expense  most recent xpath: /IRS990ScheduleH/CoalitionBuildingGrp/TotalExpensePct 

    HlthImprvmntAdvccy_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/HealthImprovementAdvocacyGrp/DirectOffsettingRevenueAmt 

    EnvrnmntlImprvmnts_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community building expense  most recent xpath: /IRS990ScheduleH/EnvironmentalImprovementsGrp/TotalCommunityBenefitExpnsAmt 

    TtlCmmnttyBldngActy_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/TotalCommuntityBuildingActyGrp/PersonsServedCnt 

    CmmntySpprt_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community building expense  most recent xpath: /IRS990ScheduleH/CommunitySupportGrp/TotalCommunityBenefitExpnsAmt 

    CltnBldng_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/CoalitionBuildingGrp/PersonsServedCnt 

    WrkfrcDvlpmnt_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community building expense  most recent xpath: /IRS990ScheduleH/WorkforceDevelopmentGrp/NetCommunityBenefitExpnsAmt 

    WrkfrcDvlpmnt_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community building expense  most recent xpath: /IRS990ScheduleH/WorkforceDevelopmentGrp/TotalCommunityBenefitExpnsAmt 

    PhysclImprvAndHsng_PrsnsSrvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Persons served  most recent xpath: /IRS990ScheduleH/PhysicalImprvAndHousingGrp/PersonsServedCnt 

    EcnmcDvlpmnt_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community building expense  most recent xpath: /IRS990ScheduleH/EconomicDevelopmentGrp/NetCommunityBenefitExpnsAmt 

    EnvrnmntlImprvmnts_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/EnvironmentalImprovementsGrp/ActivitiesOrProgramsCnt 

    CmmntySpprt_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community building expense  most recent xpath: /IRS990ScheduleH/CommunitySupportGrp/NetCommunityBenefitExpnsAmt 

    CltnBldng_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community building expense  most recent xpath: /IRS990ScheduleH/CoalitionBuildingGrp/NetCommunityBenefitExpnsAmt 

    CltnBldng_DrctOffsttngRvnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Direct offsetting revenue  most recent xpath: /IRS990ScheduleH/CoalitionBuildingGrp/DirectOffsettingRevenueAmt 

    HlthImprvmntAdvccy_ActvtsOrPrgrmsCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Number of activities or programs  most recent xpath: /IRS990ScheduleH/HealthImprovementAdvocacyGrp/ActivitiesOrProgramsCnt 

    HlthImprvmntAdvccy_NtCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (e)  Description:  Net community building expense  most recent xpath: /IRS990ScheduleH/HealthImprovementAdvocacyGrp/NetCommunityBenefitExpnsAmt 

    CltnBldng_TtlCmmntyBnftExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Total community building expense  most recent xpath: /IRS990ScheduleH/CoalitionBuildingGrp/TotalCommunityBenefitExpnsAmt 

#######
#
# IRS990ScheduleH - ScheduleH Part III - Bad Debt, Medicare, and Collection Practices 
#
#######

class skedh_part_iii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    CstAccntngSystmInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part III Section B Line 8  Description:  Cost accounting system  most recent xpath: /IRS990ScheduleH/CostingMethodologyUsedGrp/CostAccountingSystemInd 

    BdDbtExpnsRprtdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part III Section A Line 1  Description: Bad debt expense reported?  most recent xpath: /IRS990ScheduleH/BadDebtExpenseReportedInd 

    RmbrsdByMdcrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Section B Line 5  Description: Amount reimbursed by Medicare  most recent xpath: /IRS990ScheduleH/ReimbursedByMedicareAmt 

    WrttnDbtCllctnPlcyInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part III Section C Line 9a  Description: Written debt collection policy?  most recent xpath: /IRS990ScheduleH/WrittenDebtCollectionPolicyInd 

    FnnclAssstncPrvsnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part III Section C Line 9b  Description: Provision for financial assistance?  most recent xpath: /IRS990ScheduleH/FinancialAssistancePrvsnInd 

    BdDbtExpnsAttrbtblAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Section A Line 3  Description: Amount attributable to  most recent xpath: /IRS990ScheduleH/BadDebtExpenseAttributableAmt 

    CstTChrgRtInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part III Section B Line 8  Description:  Cost to charge ratio  most recent xpath: /IRS990ScheduleH/CostingMethodologyUsedGrp/CostToChargeRatioInd 

    OthrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part III Section B Line 8  Description:  Other  most recent xpath: /IRS990ScheduleH/CostingMethodologyUsedGrp/OtherInd 

    BdDbtExpnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Section A Line 2  Description: Bad debt expense amount  most recent xpath: /IRS990ScheduleH/BadDebtExpenseAmt 

    CstOfCrRmbrsdByMdcrAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Section B Line 6  Description: Cost of care reimbursed by Medicare  most recent xpath: /IRS990ScheduleH/CostOfCareReimbursedByMedcrAmt 

    MdcrSrplsOrShrtfllAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Section B Line 7  Description: Line 5 less line 6  most recent xpath: /IRS990ScheduleH/MedicareSurplusOrShortfallAmt 

#######
#
# IRS990ScheduleH - ScheduleH Part V-A - Facility Information 
#
#######

class skedh_part_va(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    HsptlFcltsCnt = models.IntegerField(null=True, blank=True)
    # Line number: Part V Section A  Description: How many hospital facilities did the organization operate during the tax year?  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesCnt 

#######
#
# IRS990ScheduleH - ScheduleH Part V-D - Other Health Care Facilities 
#
#######

class skedh_part_vd(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FcltyNm = models.IntegerField(null=True, blank=True)
    # Line number: Part V Section D  Description: Number of other facilities  most recent xpath: /IRS990ScheduleH/FacilityNum 

#######
#
# IRS990ScheduleH - SkdHMngmntCAndJntVntrs - Part IV repeating group
# A repeating structure from skedh_part_iv
#
#######

class SkdHMngmntCAndJntVntrs(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part IV Column (a)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleH/ManagementCoAndJntVenturesGrp/EntityName/BusinessNameLine1Txt 

    BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part IV Column (a)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleH/ManagementCoAndJntVenturesGrp/EntityName/BusinessNameLine2Txt 

    PhyscnsPrftOrOwnrshpPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number: Part IV Column (e)  Description:  Physican's profit % or ownership %  most recent xpath: /IRS990ScheduleH/ManagementCoAndJntVenturesGrp/PhysiciansProfitOrOwnershipPct 

    OrgPrftOrOwnrshpPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number: Part IV Column (c)  Description:  Organization's profit % or ownership %  most recent xpath: /IRS990ScheduleH/ManagementCoAndJntVenturesGrp/OrgProfitOrOwnershipPct 

    OfcrEtcPrftOrOwnrshpPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number: Part IV Column (d)  Description:  Officers, etc. profit % or ownership %  most recent xpath: /IRS990ScheduleH/ManagementCoAndJntVenturesGrp/OfcrEtcProfitOrOwnershipPct 

    PrmryActvtsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part IV Column (b)  Description:  Description of entity's primary activity  most recent xpath: /IRS990ScheduleH/ManagementCoAndJntVenturesGrp/PrimaryActivitiesTxt 

#######
#
# IRS990ScheduleH - SkdHHsptlFclts - Part V Section A repeating group
# A repeating structure from skedh_part_va
#
#######

class SkdHHsptlFclts(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    HsptlFclts_WbstAddrssTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part V Section A  Description:  Primary website address of the hospital facility  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/WebsiteAddressTxt 

    HsptlFclts_FcltyRprtngGrpCd = models.TextField(null=True, blank=True)
    # Line number: Part V Section A  Description:  Facility reporting group  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/FacilityReportingGroupCd 

    BsnssNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part V Section A  Description:  Business name line 1  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/BusinessName/BusinessNameLine1Txt 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number: Part V Section A  Description:  City  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/USAddress/CityNm 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part V Section A  Description:  Address line 1  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/USAddress/AddressLine1Txt 

    HsptlFclts_RsrchFcltyInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section A  Description:  Research facility  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/ResearchFacilityInd 

    HsptlFclts_FcltyNm = models.IntegerField(null=True, blank=True)
    # Line number: Part V Section A  Description:  Hospital facility number  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/FacilityNum 

    HsptlFclts_LcnsdHsptlInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section A  Description:  Licensed hospital  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/LicensedHospitalInd 

    BsnssNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part V Section A  Description:  Business name line 2  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/BusinessName/BusinessNameLine2Txt 

    HsptlFclts_CrtclAccssHsptlInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section A  Description:  Critical Access hospital  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/CriticalAccessHospitalInd 

    HsptlFclts_EmrgncyRm24HrsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section A  Description:  ER - 24 hours  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/EmergencyRoom24HrsInd 

    HsptlFclts_TchngHsptlInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section A  Description:  Teaching hospital  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/TeachingHospitalInd 

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number: Part V Section A  Description:  ZIP code  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/USAddress/ZIPCd 

    HsptlFclts_GnrlMdclAndSrgclInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section A  Description:  General medical and surgical  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/GeneralMedicalAndSurgicalInd 

    HsptlFclts_EmrgncyRmOthrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section A  Description:  ER - other  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/EmergencyRoomOtherInd 

    HsptlFclts_SttLcnsNm = models.TextField(null=True, blank=True)
    # Line number: Part V Section A  Description:  Hospital facilities state license number  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/StateLicenseNum 

    HsptlFclts_ChldrnsHsptlInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section A  Description:  Children's hospital  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/ChildrensHospitalInd 

    HsptlFclts_SbrdntHsptlEIN = models.CharField(null=True, blank=True, max_length=9)
    # Line number: Part V Section A  Description:  EIN, subordinate hospital  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/SubordinateHospitalEIN 

    SbrdntHsptlNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part V Section A  Description:  Business name line 2  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/SubordinateHospitalName/BusinessNameLine2Txt 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part V Section A  Description:  Address line 2  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/USAddress/AddressLine2Txt 

    SbrdntHsptlNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part V Section A  Description:  Business name line 1  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/SubordinateHospitalName/BusinessNameLine1Txt 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part V Section A  Description:  State  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/USAddress/StateAbbreviationCd 

    HsptlFclts_OthrDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part V Section A  Description:  Other  most recent xpath: /IRS990ScheduleH/HospitalFacilitiesGrp/OtherDesc 

#######
#
# IRS990ScheduleH - SkdHHsptlFcltyPlcsPrctc - Part V Section B repeating group
# A repeating structure from skedh_part_vb
#
#######

class SkdHHsptlFcltyPlcsPrctc(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FAPAvlblOnWbstInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 16a  Description:  FAP widely available on a website  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPAvailableOnWebsiteInd 

    DscrbdInfInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 15a  Description:  Described information as part of application.  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/DescribedInfoInd 

    IncmLvlCrtrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 13b  Description:  Income level criteria  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/IncomeLevelCriteriaInd 

    OthrCrtrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 13h  Description:  Other criteria  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherCriteriaInd 

    EnggdSllngDbtInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 19b  Description:  Selling debt engaged  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/EngagedSellingDebtInd 

    OthrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 3j  Description:  CHNA describes other  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherInd 

    FAPActnsOnNnpymntInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 17  Description:  Policy explains actions taken upon non-payment?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPActionsOnNonpaymentInd 

    CmmntyHlthNdsIdPrcssInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 3g  Description:  Identifying process  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CommunityHlthNeedsIdProcessInd 

    InsrncSttsCrtrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 13e  Description:  Insurance status criteria  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/InsuranceStatusCriteriaInd 

    StrtgyAttchdInd = models.TextField(null=True, blank=True)
    # Line number: Part V Section B Line 10b  Description:  Implementation strategy attached to return?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/StrategyAttachedInd 

    OthrActnsTknInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 20e  Description:  Other action taken  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherActionsTakenInd 

    FcltyNm = models.IntegerField(null=True, blank=True)
    # Line number: Part V Section B  Description:  Line number of hospital facility  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FacilityNum 

    PrcssdFAPApplctnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 20c  Description:  Processed incomplete and complete FAP applications  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ProcessedFAPApplicationInd 

    PprCpyPblcInspctnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 7c  Description:  Made paper copy  available for public inspection  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PaperCopyPublicInspectionInd 

    HwDtObtndInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 3d  Description:  How data obtained  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/HowDataObtainedInd 

    CHNACndctdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 3  Description:  Conduct community needs health assessments?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CHNAConductedInd 

    FAPAvlblOnRqstNChrgInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 16d  Description:  FAP available upon request and without charge  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPAvlblOnRequestNoChargeInd 

    EnggDfrDnyRqrPymntInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 19c  Description:  Engaged actions to defer, deny or requirment payment before providing care  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/EngageDeferDenyRqrPaymentInd 

    AmntsGnrllyBlldInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 23  Description:  Charged more than amount generally billed?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/AmountsGenerallyBilledInd 

    FAPSmmryOnWbstURLTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part V Section B Line 16c  Description:  FAP plain language summary website URL  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPSummaryOnWebsiteURLTxt 

    OthrHlthIsssInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 3f  Description:  Other health issues  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherHealthIssuesInd 

    MdEffrtOrllyNtfyInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 20b  Description:  Reasonable effort to orally notify individual about FAP  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/MadeEffortOrallyNotifyInd 

    FAPTrnsltdInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 16i  Description:  FAP translated into primary language spoken  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPTranslatedInd 

    OthrWbstInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 7b  Description:  Other website  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherWebsiteInd 

    NndsEmrgncyCrPlcyInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 21  Description:  Non-discriminatory emergency medical care policy?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/NondisEmergencyCarePolicyInd 

    FPGFmlyIncmLmtFrDscntInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 13a  Description:  Explained free care percent and discounted care percent  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FPGFamilyIncmLmtFreeDscntInd 

    BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part V Section B  Description:  Business name line 1  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/HospitalFacilityName/BusinessNameLine1Txt 

    FAPAvlblOnWbstURLTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part V Section B Line 16a  Description:  FAP website URL  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPAvailableOnWebsiteURLTxt 

    FPGFmlyIncmLmtDscntCrPct = models.DecimalField(null=True, blank=True, max_digits=22, decimal_places=12)
    # Line number: Part V Section B Line 13a  Description:  Percentage of FPG used to determine discount care  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FPGFamilyIncmLmtDscntCarePct 

    FAPSmmryOnWbstInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 16c  Description:  FAP plain language summary on a website  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPSummaryOnWebsiteInd 

    StrtgyWbstURLTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part V Section B Line 10a  Description:  Implementation strategy website URL  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/StrategyWebsiteURLTxt 

    TxExmptHsptlCYOrPYInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 2  Description:  Acquired or placed into service as tax-exempt hospital in current year or  preceding prior year?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/TaxExemptHospitalCYOrPYInd 

    NnMdInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 20f  Description:  None of these efforts were made  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/NoneMadeInd 

    OthrWbstURLTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part V Section B Line 7b  Description:  Other website URL  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherWebsiteURLTxt 

    NEmrgncyCrPlcyInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 21b  Description:  No emergency policy  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/NoEmergencyCarePolicyInd 

    TkIntAccntOthrsInptInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 5  Description:  Take community input into account  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/TakeIntoAccountOthersInputInd 

    BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part V Section B  Description:  Business name line 2  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/HospitalFacilityName/BusinessNameLine2Txt 

    ExcsRprtFrm4720FrAllAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part V Section B Line 12c  Description:  Total amount of section 4959 excise tax reported on Form 4720 for all of its hospital facilities?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ExciseReportForm4720ForAllAmt 

    CmmntyDmgrphcsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 3b  Description:  Demographics of community  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CommunityDemographicsInd 

    OthrPblctyInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 16j  Description:  Other publicity  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherPublicityInd 

    DscrbdSprtDcInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 15b  Description:  Described supporting documentation as part of application.  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/DescribedSuprtDocInd 

    PrspctvMdcrMdcdInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 22d  Description:  Prospective medicare or medicaid method  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ProspectiveMedicareMedicaidInd 

    AsstLvlCrtrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 13c  Description:  Asset level criteria  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/AssetLevelCriteriaInd 

    CHNACndctdWthOthrFcltsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 6a  Description:  Other hospital facilities?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CHNAConductedWithOtherFcltsInd 

    PrmtRprtTCrdtAgncyInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 18a  Description:  Report to credit agency permitted  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PermitReportToCreditAgencyInd 

    FPGFmlyIncmLmtFrCrPct = models.DecimalField(null=True, blank=True, max_digits=22, decimal_places=12)
    # Line number: Part V Section B Line 13a  Description:  Percentage of FPG used to determine free care  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FPGFamilyIncmLmtFreeCarePct 

    ElgCrtrExplndInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 13  Description:  Policy explains eligibility criteria for financial assistance?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/EligCriteriaExplainedInd 

    CHNACndctdYr = models.TextField(null=True, blank=True)
    # Line number: Part V Section B Line 4  Description:  Year last conducted CHNA  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CHNAConductedYr 

    PrmtOthrActnsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 18e  Description:  Other actions permitted  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PermitOtherActionsInd 

    EmrgncyCrLmtdInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 21c  Description:  Limits emergency care  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/EmergencyCareLimitedInd 

    LkBckMdcrPrvtInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 22b  Description:  Look-back method based on claims allowed by medicare fee for service and all private health insurance  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/LookBackMedicarePrivateInd 

    AppFnnclAsstExplnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 15  Description:  Policy explains method for applying for assistance?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/AppFinancialAsstExplnInd 

    PrvddWrttnNtcInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 20a  Description:  Provided written notice and plain language summary of FAP  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ProvidedWrittenNoticeInd 

    LkBckMdcdMdcrPrvtInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 22c  Description:  Look-back method based on claims allowed by nedicaid, medicare fee for service and all private health insurance  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/LookBackMedicaidMedcrPrvtInd 

    NtfdFAPCpyBllDsplyInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 16g  Description:  Notified of FAP by paper copy, on billing statement, and public displays  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/NotifiedFAPCopyBillDisplayInd 

    PrmtNActnsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 18f  Description:  None of these actions or similar actions permitted  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PermitNoActionsInd 

    PrvddHsptlCntctInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 15c  Description:  Provided  contact information of hospital staff.  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ProvidedHospitalContactInd 

    RptAvlblOnOwnWbstInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 7a  Description:  Available on own website  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/RptAvailableOnOwnWebsiteInd 

    CmmntyDfntnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 3a  Description:  Definition of community served  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CommunityDefinitionInd 

    CllctnActvtsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 19  Description:  Authorize third-party to engage in collection activities?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CollectionActivitiesInd 

    CnsltngPrcssInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 3h  Description:  Consulting process  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ConsultingProcessInd 

    NEmrgncyCrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 21a  Description:  No emergency care  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/NoEmergencyCareInd 

    FAPAppAvlblOnWbstURLTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part V Section B Line 16b  Description:  FAP application form website URL  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPAppAvailableOnWebsiteURLTxt 

    ExplndBssInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 14  Description:  Policy explains basis for calculating amounts?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ExplainedBasisInd 

    CHNACndctdWthNnFcltsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 6b  Description:  Other than hospital facilities?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CHNAConductedWithNonFcltsInd 

    MdPrsmptvElgDtrmInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 20d  Description:  Made presumptive eligibility determinations  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/MadePresumptiveEligDetermInd 

    RptAvlblThrOthrMthdInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 7d  Description:  Available other method  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/RptAvailableThruOtherMethodInd 

    FrstLcnsdCYOrPYInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 1  Description:  First licensed, registered or recognized by a State in current year or preceding prior year?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FirstLicensedCYOrPYInd 

    Frm4720FldInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 12b  Description:  File Form 4720 to report the section 4959 excise tax?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/Form4720FiledInd 

    PrrCHNAImpctInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 3i  Description:  Impact of actions taken identified in prior CHNA  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PriorCHNAImpactInd 

    GrssChrgsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 24  Description:  Gross charges in billing?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/GrossChargesInd 

    OwnWbstURLTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part V Section B Line 7a  Description:  Hospital facilities website URL  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OwnWebsiteURLTxt 

    OrgnztnIncrExcsTxInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 12a  Description:  Incur an excise tax under section 4959 for the hospital facility's failure to conduct a CHNA as required by section 501(r)(3)?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OrganizationIncurExciseTaxInd 

    FAPAppAvlblOnWbstInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 16b  Description:  FAP application form widely available on a website  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPAppAvailableOnWebsiteInd 

    PrvddNnprftCntctInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 15d  Description:  Provided contact information of nonprofit organization.  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ProvidedNonprofitContactInd 

    RprtngTCrdtAgncyInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 19a  Description:  Credit agency engaged  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ReportingToCreditAgencyInd 

    StrtgyPstdWbstInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 10  Description:  Implementation strategy posted on website?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/StrategyPostedWebsiteInd 

    ImplmnttnStrtgyAdptInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 8  Description:  Adopt implementation strategy?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ImplementationStrategyAdoptInd 

    FAPAppAvlblOnRqstNChrgInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 16e  Description:  FAP application form available upon request and without charge  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPAppAvlblOnRequestNoChrgInd 

    CHNARprtWdlyAvlblInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 7  Description:  CHNA widely available to public?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CHNAReportWidelyAvailableInd 

    RsdncyCrtrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 13g  Description:  Residency criteria  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ResidencyCriteriaInd 

    OthrRsnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 21d  Description:  Other reason  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherReasonInd 

    PrmtLglJdclPrcssInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 18d  Description:  Actions that required a legal or judicial process  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PermitLegalJudicialProcessInd 

    CmmnttyNtfdFAPInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 16h  Description:  Notified community about availability of FAP  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CommuntityNotifiedFAPInd 

    UndrnsrncSttCrtrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 13f  Description:  Underinsurance status criteria  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/UnderinsuranceStatCriteriaInd 

    LkBckMdcrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 22a  Description:  Look-back method based on claims allowed by medicare fee for service  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/LookBackMedicareInd 

    OthrActnsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 19e  Description:  Other actions engaged  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherActionsInd 

    MdclIndgncyCrtrInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 13d  Description:  Medical indigency criteria  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/MedicalIndigencyCriteriaInd 

    OthrMthdInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 15e  Description:  Other method used to explain.  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/OtherMethodInd 

    IncldsPblctyMsrsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Section B Line 16  Description:  Policy includes publicity measures?  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/IncludesPublicityMeasuresInd 

    EnggdLglJdclPrcssInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 19d  Description:  Engaged actions that required a legal or judicial process  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/EngagedLegalJudicialProcessInd 

    PrmtDfrDnyRqrPymntInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 18c  Description:  Deferring, denying or requiring payment before care due to previous nonpayment permitted.  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PermitDeferDenyRqrPaymentInd 

    PrmtSllngDbtInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 18b  Description:  Selling debt permitted  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/PermitSellingDebtInd 

    ExstngRsrcsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 3c  Description:  Existing health care facilities and resources  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ExistingResourcesInd 

    FAPSmAvlblOnRqstNChrgInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 16f  Description:  FAP plain language summary available upon request and without charge  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/FAPSumAvlblOnRequestNoChrgInd 

    CmmntyHlthNdsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part V Section B Line 3e  Description:  Health needs of community  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/CommunityHealthNeedsInd 

    ImplmnttnStrtgyAdptYr = models.TextField(null=True, blank=True)
    # Line number: Part V Section B Line 9  Description:  Year last adopted implementation strategy  most recent xpath: /IRS990ScheduleH/HospitalFcltyPoliciesPrctcGrp/ImplementationStrategyAdptYr 

#######
#
# IRS990ScheduleH - SkdHSpplmntlInfrmtn - Part V Section C, Supplemental Information for Part V Section B
# A repeating structure from skedh_part_vc
#
#######

class SkdHSpplmntlInfrmtn(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FrmAndLnRfrncDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part V  Description:  Form, part and line number reference  most recent xpath: /IRS990ScheduleH/SupplementalInformationGrp/FormAndLineReferenceDesc 

    ExplntnTxt = models.TextField(null=True, blank=True)
    # Line number: Part V  Description:  Form, part and line number reference explanation  most recent xpath: /IRS990ScheduleH/SupplementalInformationGrp/ExplanationTxt 

#######
#
# IRS990ScheduleH - SkdHOthHlthCrFclts - Part V section D, other health care facilities; ; Part V Section D repeating group
# A repeating structure from skedh_part_vd
#
#######

class SkdHOthHlthCrFclts(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part V Section D  Description:  Business name line 2  most recent xpath: /IRS990ScheduleH/OthHlthCareFcltsNotHospitalGrp/OthHlthCareFcltsGrp/BusinessName/BusinessNameLine2Txt 

    AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part V Section D  Description:  Address line 1  most recent xpath: /IRS990ScheduleH/OthHlthCareFcltsNotHospitalGrp/OthHlthCareFcltsGrp/USAddress/AddressLine1Txt 

    FcltyTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part V Section D  Description:  Facility type  most recent xpath: /IRS990ScheduleH/OthHlthCareFcltsNotHospitalGrp/OthHlthCareFcltsGrp/FacilityTxt 

    ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number: Part V Section D  Description:  ZIP code  most recent xpath: /IRS990ScheduleH/OthHlthCareFcltsNotHospitalGrp/OthHlthCareFcltsGrp/USAddress/ZIPCd 

    SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part V Section D  Description:  State  most recent xpath: /IRS990ScheduleH/OthHlthCareFcltsNotHospitalGrp/OthHlthCareFcltsGrp/USAddress/StateAbbreviationCd 

    BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part V Section D  Description:  Business name line 1  most recent xpath: /IRS990ScheduleH/OthHlthCareFcltsNotHospitalGrp/OthHlthCareFcltsGrp/BusinessName/BusinessNameLine1Txt 

    AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part V Section D  Description:  Address line 2  most recent xpath: /IRS990ScheduleH/OthHlthCareFcltsNotHospitalGrp/OthHlthCareFcltsGrp/USAddress/AddressLine2Txt 

    CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number: Part V Section D  Description:  City  most recent xpath: /IRS990ScheduleH/OthHlthCareFcltsNotHospitalGrp/OthHlthCareFcltsGrp/USAddress/CityNm 

#######
#
# IRS990ScheduleH - SkdHSpplmntlInfrmtnDtl - Part VI contents
# A repeating structure from skedh_part_vi
#
#######

class SkdHSpplmntlInfrmtnDtl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FrmAndLnRfrncDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part VI  Description:  Form, part and line number reference  most recent xpath: /IRS990ScheduleH/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = models.TextField(null=True, blank=True)
    # Line number: Part VI  Description:  Form, part and line number explanation  most recent xpath: /IRS990ScheduleH/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleI - ScheduleI Part I General Information on Grants and Assistance 
#
#######

class skedi_part_i(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    GrntRcrdsMntndInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 1  Description: Does the organization maintain records to substantiate the amount of the grants or assistance, the grantees' eligibility for the grants or assistance, and the selection criteria used to award the grants or assistance?  most recent xpath: /IRS990ScheduleI/GrantRecordsMaintainedInd 

#######
#
# IRS990ScheduleI - ScheduleI Part II Grants and Other Assistance to Governments and Organizations in the United States 
#
#######

class skedi_part_ii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    TtlOthrOrgCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 3  Description: Enter total number of other organizations  most recent xpath: /IRS990ScheduleI/TotalOtherOrgCnt 

    Ttl501c3OrgCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Line 2  Description: Enter total number of 501(c)(3) and government organizations  most recent xpath: /IRS990ScheduleI/Total501c3OrgCnt 

#######
#
# IRS990ScheduleI - SkdIGrntsOthrAsstTIndvInUS - Part III content
# A repeating structure from skedi_part_iii
#
#######

class SkdIGrntsOthrAsstTIndvInUS(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    CshGrntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Column (c)  Description:  Amount of cash grant  most recent xpath: /IRS990ScheduleI/GrantsOtherAsstToIndivInUSGrp/CashGrantAmt 

    NnCshAssstncDsc = models.TextField(null=True, blank=True)
    # Line number: Part III Column (f)  Description:  Description of non-cash assistance  most recent xpath: /IRS990ScheduleI/GrantsOtherAsstToIndivInUSGrp/NonCashAssistanceDesc 

    GrntTxt = models.TextField(null=True, blank=True)
    # Line number: Part III Column (a)  Description:  Type of grant or assistance  most recent xpath: /IRS990ScheduleI/GrantsOtherAsstToIndivInUSGrp/GrantTypeTxt 

    NnCshAssstncAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Column (d)  Description:  Amount of non-cash assistance  most recent xpath: /IRS990ScheduleI/GrantsOtherAsstToIndivInUSGrp/NonCashAssistanceAmt 

    RcpntCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Column (b)  Description:  Number of recipients  most recent xpath: /IRS990ScheduleI/GrantsOtherAsstToIndivInUSGrp/RecipientCnt 

    VltnMthdUsdDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part III Column (e)  Description:  Method of valuation (book, FMV, appraisal, other)  most recent xpath: /IRS990ScheduleI/GrantsOtherAsstToIndivInUSGrp/ValuationMethodUsedDesc 

#######
#
# IRS990ScheduleI - SkdISpplmntlInfrmtnDtl - Part IV content
# A repeating structure from skedi_part_iv
#
#######

class SkdISpplmntlInfrmtnDtl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FrmAndLnRfrncDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part IV  Description:  Form, part and line number reference  most recent xpath: /IRS990ScheduleI/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = models.TextField(null=True, blank=True)
    # Line number: Part IV  Description:  Form, part and line number reference explanation  most recent xpath: /IRS990ScheduleI/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleI - SkdIRcpntTbl - Complete if the organization reported more than $5,000 on Form 990, Part IX, line 1 for any recipient that received more than $5,000
# A repeating structure from skedi_part_ii
#
#######

class SkdIRcpntTbl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    RcpntTbl_IRCSctnDsc = models.CharField(null=True, blank=True, max_length=20)
    # Line number:  Part II Line  1 Column (c)  Description:  IRC code section if applicable  most recent xpath: /IRS990ScheduleI/RecipientTable/IRCSectionDesc 

    RcpntTbl_NnCshAssstncAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Line  1 Column (e)  Description:  Amount of non-cash assistance  most recent xpath: /IRS990ScheduleI/RecipientTable/NonCashAssistanceAmt 

    FrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number:  Part II Line  1 Column (a)  Description:  Postal code  most recent xpath: /IRS990ScheduleI/RecipientTable/ForeignAddress/ForeignPostalCd 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part II Line  1 Column (a)  Description:  State  most recent xpath: /IRS990ScheduleI/RecipientTable/USAddress/StateAbbreviationCd 

    FrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number:  Part II Line  1 Column (a)  Description:  City  most recent xpath: /IRS990ScheduleI/RecipientTable/ForeignAddress/CityNm 

    RcpntBsnssNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part II Line 1 Column (a)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleI/RecipientTable/RecipientBusinessName/BusinessNameLine1Txt 

    FrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part II Line  1 Column (a)  Description:  Address line 1  most recent xpath: /IRS990ScheduleI/RecipientTable/ForeignAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part II Line  1 Column (a)  Description:  Address line 2  most recent xpath: /IRS990ScheduleI/RecipientTable/USAddress/AddressLine2Txt 

    FrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part II Line  1 Column (a)  Description:  Address line 2  most recent xpath: /IRS990ScheduleI/RecipientTable/ForeignAddress/AddressLine2Txt 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part II Line  1 Column (a)  Description:  Address line 1  most recent xpath: /IRS990ScheduleI/RecipientTable/USAddress/AddressLine1Txt 

    RcpntTbl_RcpntEIN = models.CharField(null=True, blank=True, max_length=9)
    # Line number:  Part II Line  1 Column (b)  Description:  EIN of recipient  most recent xpath: /IRS990ScheduleI/RecipientTable/RecipientEIN 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number:  Part II Line  1 Column (a)  Description:  City  most recent xpath: /IRS990ScheduleI/RecipientTable/USAddress/CityNm 

    FrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Part II Line  1 Column (a)  Description:  Country  most recent xpath: /IRS990ScheduleI/RecipientTable/ForeignAddress/CountryCd 

    RcpntTbl_PrpsOfGrntTxt = models.TextField(null=True, blank=True)
    # Line number:  Part II Line  1 Column (h)  Description:  Purpose of grant  most recent xpath: /IRS990ScheduleI/RecipientTable/PurposeOfGrantTxt 

    RcpntTbl_VltnMthdUsdDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part II Line  1 Column (f)  Description:  Method of valuation (book. FMV, appraisal, other)  most recent xpath: /IRS990ScheduleI/RecipientTable/ValuationMethodUsedDesc 

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number:  Part II Line  1 Column (a)  Description:  ZIP code  most recent xpath: /IRS990ScheduleI/RecipientTable/USAddress/ZIPCd 

    RcpntTbl_CshGrntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Line  1 Column (d)  Description:  Amount of cash grant  most recent xpath: /IRS990ScheduleI/RecipientTable/CashGrantAmt 

    FrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number:  Part II Line  1 Column (a)  Description:  Province or state  most recent xpath: /IRS990ScheduleI/RecipientTable/ForeignAddress/ProvinceOrStateNm 

    RcpntBsnssNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part II Line 1 Column (a)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleI/RecipientTable/RecipientBusinessName/BusinessNameLine2Txt 

    RcpntTbl_NnCshAssstncDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part II Line  1 Column (g)  Description:  Description of non-cash assistance  most recent xpath: /IRS990ScheduleI/RecipientTable/NonCashAssistanceDesc 

#######
#
# IRS990ScheduleJ - ScheduleJ Part I Questions Regarding Compensation
#
#######

class skedj_part_i(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    CmpBsdOnRvnOfFlngOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 5a  Description: Compensation based on revenue of filing org?  most recent xpath: /IRS990ScheduleJ/CompBasedOnRevenueOfFlngOrgInd 

    DscrtnrySpndngAcctInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 1a  Description: Discretionary spending account  most recent xpath: /IRS990ScheduleJ/DiscretionarySpendingAcctInd 

    HsngAllwncOrRsdncInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 1a  Description: Housing allowance or residence  most recent xpath: /IRS990ScheduleJ/HousingAllowanceOrResidenceInd 

    CmpBsdNtErnsRltdOrgsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 6b  Description: Compensation based on net earnings of related orgs?  most recent xpath: /IRS990ScheduleJ/CompBsdNetEarnsRltdOrgsInd 

    PymntsFrUsOfRsdncInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 1a  Description: Payments for use of residence  most recent xpath: /IRS990ScheduleJ/PaymentsForUseOfResidenceInd 

    IntlCntrctExcptnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 8  Description: Initial contract exception?  most recent xpath: /IRS990ScheduleJ/InitialContractExceptionInd 

    CmpnstnSrvyInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 3  Description: Compensation survey  most recent xpath: /IRS990ScheduleJ/CompensationSurveyInd 

    SpplmntlNnqlRtrPlnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 4b  Description: Supplemental nonqualified retirement plan?  most recent xpath: /IRS990ScheduleJ/SupplementalNonqualRtrPlanInd 

    AnyNnFxdPymntsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 7  Description: Any non-fixed payments?  most recent xpath: /IRS990ScheduleJ/AnyNonFixedPaymentsInd 

    FrstClssOrChrtrTrvlInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 1a  Description: First class or charter travel  most recent xpath: /IRS990ScheduleJ/FirstClassOrCharterTravelInd 

    SbstnttnRqrdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 2  Description: Substantiation required?  most recent xpath: /IRS990ScheduleJ/SubstantiationRequiredInd 

    CmpnstnCmmttInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 3  Description: Compensation committee  most recent xpath: /IRS990ScheduleJ/CompensationCommitteeInd 

    EqtyBsdCmpArrngmInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 4c  Description: Equity based compensation arrangement?  most recent xpath: /IRS990ScheduleJ/EquityBasedCompArrngmInd 

    BrdOrCmmttApprvlInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 3  Description: Board or committee approval  most recent xpath: /IRS990ScheduleJ/BoardOrCommitteeApprovalInd 

    CmpBsdNtErnsFlngOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 6a  Description: Compensation based on net earnings of filing org?  most recent xpath: /IRS990ScheduleJ/CompBsdNetEarnsFlngOrgInd 

    WrttnPlcyRfTAndEExpnssInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 1b  Description: Written policy reference T and E expenses?  most recent xpath: /IRS990ScheduleJ/WrittenPolicyRefTAndEExpnssInd 

    PrsnlSrvcsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 1a  Description: Personal services  most recent xpath: /IRS990ScheduleJ/PersonalServicesInd 

    IndpndntCnsltntInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 3  Description: Independent consultant  most recent xpath: /IRS990ScheduleJ/IndependentConsultantInd 

    IdmnfctnGrssUpPmtsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 1a  Description: Idemnification and gross-up payments  most recent xpath: /IRS990ScheduleJ/IdemnificationGrossUpPmtsInd 

    TrvlFrCmpnnsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 1a  Description: Travel for companions  most recent xpath: /IRS990ScheduleJ/TravelForCompanionsInd 

    Frm990OfOthrOrgnztnsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 3  Description: Form 990 of other organizations  most recent xpath: /IRS990ScheduleJ/Form990OfOtherOrganizationsInd 

    RbttblPrsmptnPrcInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 9  Description: Rebuttable presumption procedure?  most recent xpath: /IRS990ScheduleJ/RebuttablePresumptionProcInd 

    SvrncPymntInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 4a  Description: Severance payment?  most recent xpath: /IRS990ScheduleJ/SeverancePaymentInd 

    CmpBsdOnRvRltdOrgsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 5b  Description: Compensation based on revenue of related orgs?  most recent xpath: /IRS990ScheduleJ/CompBsdOnRevRelatedOrgsInd 

    ClbDsOrFsInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 1a  Description: Club dues or fees  most recent xpath: /IRS990ScheduleJ/ClubDuesOrFeesInd 

    WrttnEmplymntCntrctInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number: Part I Line 3  Description: Written employment contract  most recent xpath: /IRS990ScheduleJ/WrittenEmploymentContractInd 

#######
#
# IRS990ScheduleJ - SkdJRltdOrgOffcrTrstKyEmpl - Part II contents
# A repeating structure from skedj_part_ii
#
#######

class SkdJRltdOrgOffcrTrstKyEmpl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    OthrCmpnstnFlngOrgAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Column (B)(iii)  Description:  Other compensation ($) from filing organization  most recent xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/OtherCompensationFilingOrgAmt 

    BnsFlngOrgnztnAmnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Column (B)(ii)  Description:  Bonus and incentive compensation ($) from filing organization  most recent xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/BonusFilingOrganizationAmount 

    BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part II Column (A)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/BusinessName/BusinessNameLine2Txt 

    CmpnstnBsdOnRltdOrgsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Column (B)(i)  Description:  Compensation based on related organizations?  most recent xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/CompensationBasedOnRltdOrgsAmt 

    NntxblBnftsFlngOrgAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Column (D)  Description:  Nontaxable benefits ($) from filing organization  most recent xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/NontaxableBenefitsFilingOrgAmt 

    NntxblBnftsRltdOrgsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Column (D)  Description:  Nontaxable benefits ($) from related organizations  most recent xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/NontaxableBenefitsRltdOrgsAmt 

    TtlTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part II Column (A)  Description:  Title of Officer  most recent xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/TitleTxt 

    OthrCmpnstnRltdOrgsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Column (B)(iii)  Description:  Other compensation ($) from related organizations  most recent xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/OtherCompensationRltdOrgsAmt 

    TtlCmpnstnFlngOrgAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Column (E)  Description:  Total of (B)(i) - (D), from filing org  most recent xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/TotalCompensationFilingOrgAmt 

    DfrrdCmpRltdOrgsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Column (C)  Description:  Deferred compensation ($) from related organizations  most recent xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/DeferredCompRltdOrgsAmt 

    BsCmpnstnFlngOrgAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Column (B)(i)  Description:  Base compensation ($) from filing organization  most recent xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/BaseCompensationFilingOrgAmt 

    CmpRprtPrr990RltdOrgsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Column (F)  Description:  Comp reported prior 990 - from related orgs  most recent xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/CompReportPrior990RltdOrgsAmt 

    CmpRprtPrr990FlngOrgAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Column (F)  Description:  Comp reported prior 990 - from filing org  most recent xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/CompReportPrior990FilingOrgAmt 

    TtlCmpnstnRltdOrgsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Column (E)  Description:  Total of (B)(i) - (D), from related orgs  most recent xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/TotalCompensationRltdOrgsAmt 

    BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part II Column (A)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/BusinessName/BusinessNameLine1Txt 

    DfrrdCmpnstnFlngOrgAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Column (C)  Description:  Deferred compensation ($) from filing organization  most recent xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/DeferredCompensationFlngOrgAmt 

    PrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part II Column (A)  Description:  Name of officer - person  most recent xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/PersonNm 

    BnsRltdOrgnztnsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Column (B)(ii)  Description:  Bonus and incentive compensation ($) from related organizations  most recent xpath: /IRS990ScheduleJ/RltdOrgOfficerTrstKeyEmplGrp/BonusRelatedOrganizationsAmt 

#######
#
# IRS990ScheduleJ - SkdJSpplmntlInfrmtnDtl - Part III contents
# A repeating structure from skedj_part_iii
#
#######

class SkdJSpplmntlInfrmtnDtl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FrmAndLnRfrncDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part III  Description:  Form, Part and line number reference  most recent xpath: /IRS990ScheduleJ/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = models.TextField(null=True, blank=True)
    # Line number: Part III  Description:  Form, Part and line number reference explanation  most recent xpath: /IRS990ScheduleJ/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleK - SkdKTxExmptBndsIsss
# A repeating structure from skedk_part_i
#
#######

class SkdKTxExmptBndsIsss(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")
    documentId = models.TextField(blank=True, null=True, help_text="documentID attribute")
    OnBhlfOfIssrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part I Column (h)  Description:  On behalf of issuer?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/OnBehalfOfIssuerInd 

    DfsdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part I Column (g)  Description:  Defeased?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/DefeasedInd 

    CUSIPNm = models.CharField(null=True, blank=True, max_length=9)
    # Line number:  Part I Column (c)  Description:  CUSIP number  most recent xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/CUSIPNum 

    PrpsDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part I Column (f)  Description:  Description of purpose  most recent xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/PurposeDesc 

    BndRfrncCd = models.TextField(null=True, blank=True)
    # Line number:  Part I  Description:  Bond issue reference number (A-D)  most recent xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/BondReferenceCd 

    IssPrcAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part I Column (e)  Description:  Issue price  most recent xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/IssuePriceAmt 

    BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part I Column (a)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/IssuerName/BusinessNameLine2Txt 

    BndIssdDt = models.CharField(null=True, blank=True, max_length=31)
    # Line number:  Part I Column (d)  Description:  Date issued  most recent xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/BondIssuedDt 

    BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part I Column (a)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/IssuerName/BusinessNameLine1Txt 

    BndIssrEIN = models.CharField(null=True, blank=True, max_length=9)
    # Line number:  Part I Column (b)  Description:  Issuer EIN  most recent xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/BondIssuerEIN 

    PlFnncngInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part I Column (i)  Description:  Pool financing?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsIssuesGrp/PoolFinancingInd 

#######
#
# IRS990ScheduleK - SkdKTxExmptBndsPrcds
# A repeating structure from skedk_part_ii
#
#######

class SkdKTxExmptBndsPrcds(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")
    documentId = models.TextField(blank=True, null=True, help_text="documentID attribute")
    UnspntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Line 12  Description:  Amount unspent  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/UnspentAmt 

    CrdtEnhncmntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Line 8  Description:  Credit enhancement from proceeds  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/CreditEnhancementAmt 

    TtlPrcdsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Line 3  Description:  Total proceeds of issue  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/TotalProceedsAmt 

    FnlAllctnMdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part II Line 16  Description:  Final allocation made?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/FinalAllocationMadeInd 

    InRsrvFndAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Line 4  Description:  Gross proceeds in reserve funds  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/InReserveFundAmt 

    RfndngEscrwAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Line 6  Description:  Proceeds in refunding escrow  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/RefundingEscrowAmt 

    OthrSpntPrcdsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Line 11  Description:  Other spent proceeds  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/OtherSpentProceedsAmt 

    AdqtBksAndRcMntInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part II Line 17  Description:  Adequate books and records maintained?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/AdequateBooksAndRecMaintInd 

    CptlExpndtrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Line 10  Description:  Capital expenditures from proceeds  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/CapitalExpendituresAmt 

    RtrdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Line 1  Description:  Amount of bonds retired  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/RetiredAmt 

    BndDfsdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Line 2  Description:  Amount of bonds defeased  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/BondDefeasedAmt 

    BndRfrncCd = models.TextField(null=True, blank=True)
    # Line number:  Part II  Description:  Bond issue reference number (A-D)  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/BondReferenceCd 

    SbstntlCmpltnYr = models.IntegerField(null=True, blank=True)
    # Line number:  Part II Line 13  Description:  Year of substantial completion  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/SubstantialCompletionYr 

    WrkngCptlExpndtrsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Line 9  Description:  Working capital expenditures from proceeds  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/WorkingCapitalExpendituresAmt 

    RfndngTxExmptBndsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part II Line 14  Description:  Refunding tax-exempt bonds?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/RefundingTaxExemptBondsInd 

    CrrntRfndngInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part II Line 14  Description:  Current refunding?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/CurrentRefundingInd 

    AdvncRfndngInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part II Line 15  Description:  Advance refunding?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/AdvanceRefundingInd 

    CptlzdIntrstAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Line 5  Description:  Capitalized interest from proceeds  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/CapitalizedInterestAmt 

    RfndngTxblBndsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part II Line 15  Description:  Refunding taxable bonds?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/RefundingTaxableBondsInd 

    IssncCstsFrmPrcdsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Line 7  Description:  Issuance costs from proceeds  most recent xpath: /IRS990ScheduleK/TaxExemptBondsProceedsGrp/IssuanceCostsFromProceedsAmt 

#######
#
# IRS990ScheduleK - SkdKTxExmptBndsPrvtBsUs
# A repeating structure from skedk_part_iii
#
#######

class SkdKTxExmptBndsPrvtBsUs(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")
    documentId = models.TextField(blank=True, null=True, help_text="documentID attribute")
    AnyLsArrngmntsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part III Line 2  Description:  Any lease arrangements?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/AnyLeaseArrangementsInd 

    OwnngBndFnncdPrprtyInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part III Line 1  Description:  Partnership or LLC owning bond financed property?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/OwningBondFinancedPropertyInd 

    AnyRsrchAgrmntsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part III Line 3c  Description:  Any research agreements?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/AnyResearchAgreementsInd 

    RmdlActnTknInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part III Line 8c  Description:  Remedial action taken?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/RemedialActionTakenInd 

    PrvtBsUsByOthrsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Part III Line 4  Description:  Percentage of private business use by others  most recent xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/PrivateBusUseByOthersPct 

    EnggBndCnslRsrchInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part III Line 3d  Description:  Bond Counsel routinely engaged to review management or service contracts?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/EngageBondCounselResearchInd 

    MgmtCntrctBndFncdPrpInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part III Line 3a  Description:  Management contract for bond financed property?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/MgmtContractBondFincdPropInd 

    PrcsNnqlfdBndRmdtdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part III Line 9  Description:  Nonqualified bonds remediated procedures?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/ProcsNonqualifiedBondRemdtdInd 

    BndIssMtPrvtScPymtTstInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part III Line 7  Description:  Bond issue meets private security or payment test?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/BondIssMeetPrvtSecPymtTestInd 

    EnggBndCnslCntrctsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part III Line 3b  Description:  Bond Counsel routinely engaged to review management or service contracts?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/EngageBondCounselContractsInd 

    PrvtBsCncrnngUBIPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Part III Line 5  Description:  Percentage of private business concerning UBI  most recent xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/PrivateBusConcerningUBIPct 

    ChngInUsBndFnncdPrpInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part III Line 8a  Description:  Change in use of bond financed property?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/ChangeInUseBondFinancedPropInd 

    ChngInUsBndFnncdPrpPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Part III Line 8b  Description:  Percentage change in use of bond financed property  most recent xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/ChangeInUseBondFinancedPropPct 

    BndRfrncCd = models.TextField(null=True, blank=True)
    # Line number:  Part III  Description:  Bond issue reference number (A-D)  most recent xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/BondReferenceCd 

    TtlPrvtBsnssUsPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number:  Part III Line 6  Description:  Total of lines 4 and 5  most recent xpath: /IRS990ScheduleK/TaxExemptBondsPrivateBusUseGrp/TotalPrivateBusinessUsePct 

#######
#
# IRS990ScheduleK - SkdKTxExmptBndsArbtrg
# A repeating structure from skedk_part_iv
#
#######

class SkdKTxExmptBndsArbtrg(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")
    documentId = models.TextField(blank=True, null=True, help_text="documentID attribute")
    TxExmptBndsArbtrg_HdgIdntfdInBksAndRcInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Line 4a  Description:  Hedge identified in books and records?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/HedgeIdentifiedInBksAndRecInd 

    TxExmptBndsArbtrg_BndRfrncCd = models.TextField(null=True, blank=True)
    # Line number:  Part IV  Description:  Bond issue reference number (A-D)  most recent xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/BondReferenceCd 

    TxExmptBndsArbtrg_RbtNtDYtInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Line 2a  Description:  Rebate not due yet?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/RebateNotDueYetInd 

    TxExmptBndsArbtrg_WrttnPrcTMntrRqsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Line 7  Description:  Written procedures to monitor requirements?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/WrittenProcToMonitorReqsInd 

    TxExmptBndsArbtrg_RgltrySfHrbrStsfdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Line 5d  Description:  Regulatory safe harbor satisfied?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/RegulatorySafeHarborStsfdInd 

    HdgPrvdrNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part IV Line 4b  Description:  Business name line 1  most recent xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/HedgeProviderName/BusinessNameLine1Txt 

    TxExmptBndsArbtrg_GrssPrcdsInvstdInGICInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Line 5a  Description:  Gross proceeds invested in GIC?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/GrossProceedsInvestedInGICInd 

    TxExmptBndsArbtrg_ExcptnTRbtInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Line 2b  Description:  Exception to rebate?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/ExceptionToRebateInd 

    TxExmptBndsArbtrg_NRbtDInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Line 2c  Description:  No rebate due?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/NoRebateDueInd 

    TxExmptBndsArbtrg_HdgTrmntdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Line 4e  Description:  Was the hedge terminated?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/HedgeTerminatedInd 

    TxExmptBndsArbtrg_Frm8038TFldInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Line 1  Description:  Form 8038-T filed?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/Form8038TFiledInd 

    GICPrvdrNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part IV Line 5b  Description:  Business name line 2  most recent xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/GICProviderName/BusinessNameLine2Txt 

    GICPrvdrNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part IV Line 5b  Description:  Business name line 1  most recent xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/GICProviderName/BusinessNameLine1Txt 

    TxExmptBndsArbtrg_TrmOfGICPct = models.DecimalField(null=True, blank=True, max_digits=22, decimal_places=12)
    # Line number:  Part IV Line 5c  Description:  Term of GIC  most recent xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/TermOfGICPct 

    TxExmptBndsArbtrg_SprntgrtdHdgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Line 4d  Description:  Was the hedge superintegrated?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/SuperintegratedHedgeInd 

    TxExmptBndsArbtrg_VrblRtIssInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Line 3  Description:  Variable rate issue?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/VariableRateIssueInd 

    HdgPrvdrNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part IV Line 4b  Description:  Business name line 2  most recent xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/HedgeProviderName/BusinessNameLine2Txt 

    TxExmptBndsArbtrg_TrmOfHdgPct = models.DecimalField(null=True, blank=True, max_digits=22, decimal_places=12)
    # Line number:  Part IV Line 4c  Description:  Term of hedge  most recent xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/TermOfHedgePct 

    TxExmptBndsArbtrg_GrssPrcdsInvstdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part IV Line 6  Description:  Gross proceeds invested?  most recent xpath: /IRS990ScheduleK/TaxExemptBondsArbitrageGrp/GrossProceedsInvestedInd 

#######
#
# IRS990ScheduleK - SkdKPrcdrsCrrctvActn
# A repeating structure from skedk_part_v
#
#######

class SkdKPrcdrsCrrctvActn(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")
    documentId = models.TextField(blank=True, null=True, help_text="documentID attribute")
    BndRfrncCd = models.TextField(null=True, blank=True)
    # Line number:  Part V  Description:  Bond issue reference number (A-D)  most recent xpath: /IRS990ScheduleK/ProceduresCorrectiveActionGrp/BondReferenceCd 

    PrcdrsCrrctvActnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part V  Description:  Procedures to ensure violations identified and corrected?  most recent xpath: /IRS990ScheduleK/ProceduresCorrectiveActionGrp/ProceduresCorrectiveActionInd 

#######
#
# IRS990ScheduleK - SkdKSpplmntlInfrmtnDtl - Part VI contents
# A repeating structure from skedk_part_vi
#
#######

class SkdKSpplmntlInfrmtnDtl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")
    documentId = models.TextField(blank=True, null=True, help_text="documentID attribute")
    ExplntnTxt = models.TextField(null=True, blank=True)
    # Line number: Part VI  Description:  Form, part and line number reference explanation  most recent xpath: /IRS990ScheduleK/SupplementalInformationDetail/ExplanationTxt 

    FrmAndLnRfrncDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part VI  Description:  Form, part and line number reference  most recent xpath: /IRS990ScheduleK/SupplementalInformationDetail/FormAndLineReferenceDesc 

#######
#
# IRS990ScheduleL - ScheduleL Part I Excess Benefit Transactions 
#
#######

class skedl_part_i(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    TxImpsdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 2  Description: Amount of tax imposed  most recent xpath: /IRS990ScheduleL/TaxImposedAmt 

    TxRmbrsdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 3  Description: Amount of tax reimbursed  most recent xpath: /IRS990ScheduleL/TaxReimbursedAmt 

#######
#
# IRS990ScheduleL - ScheduleL Part II Loans to and/or From Interested Persons 
#
#######

class skedl_part_ii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    TtlBlncDAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part II Column d  Description: Total balance due  most recent xpath: /IRS990ScheduleL/TotalBalanceDueAmt 

#######
#
# IRS990ScheduleL - SkdLDsqlfdPrsnExBnftTr
# A repeating structure from skedl_part_i
#
#######

class SkdLDsqlfdPrsnExBnftTr(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    RlnDsqlfdPrsnOrgTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part I Column (1b)  Description:  Relationship between disqualified person and organization  most recent xpath: /IRS990ScheduleL/DisqualifiedPersonExBnftTrGrp/RlnDisqualifiedPersonOrgTxt 

    PrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part I Column (1a)  Description:  Name - Person  most recent xpath: /IRS990ScheduleL/DisqualifiedPersonExBnftTrGrp/PersonNm 

    TrnsctnCrrctdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part I Column (1d)  Description:  Transaction corrected?  most recent xpath: /IRS990ScheduleL/DisqualifiedPersonExBnftTrGrp/TransactionCorrectedInd 

    BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part I Column (1a)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleL/DisqualifiedPersonExBnftTrGrp/BusinessName/BusinessNameLine2Txt 

    TrnsctnDsc = models.TextField(null=True, blank=True)
    # Line number:  Part I Column (1c)  Description:  Description of transaction  most recent xpath: /IRS990ScheduleL/DisqualifiedPersonExBnftTrGrp/TransactionDesc 

    BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part I Column (1a)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleL/DisqualifiedPersonExBnftTrGrp/BusinessName/BusinessNameLine1Txt 

#######
#
# IRS990ScheduleL - SkdLLnsBtwnOrgIntrstdPrsn
# A repeating structure from skedl_part_ii
#
#######

class SkdLLnsBtwnOrgIntrstdPrsn(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    LnFrmOrgnztnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Part II Column (d)  Description:  Loan from organization?  most recent xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/LoanFromOrganizationInd 

    BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part II Column (a)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/BusinessName/BusinessNameLine1Txt 

    BrdOrCmmttApprvlInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part II Column (h)  Description:  Approved by board?  most recent xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/BoardOrCommitteeApprovalInd 

    LnTOrgnztnInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Part II Column (d)  Description:  Loan to organization?  most recent xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/LoanToOrganizationInd 

    BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part II Column (a)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/BusinessName/BusinessNameLine2Txt 

    OrgnlPrncplAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Column (e)  Description:  Original principal amount  most recent xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/OriginalPrincipalAmt 

    WrttnAgrmntInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part II Column (i)  Description:  Written agreement?  most recent xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/WrittenAgreementInd 

    LnPrpsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part II Column (c)  Description:  Purpose of loan  most recent xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/LoanPurposeTxt 

    DfltInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number:  Part II Column (g)  Description:  Default?  most recent xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/DefaultInd 

    PrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Part II Column (a)  Description:  Name - Person  most recent xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/PersonNm 

    RltnshpWthOrgTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part II Column (b)  Description:  Relationship with organization  most recent xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/RelationshipWithOrgTxt 

    BlncDAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part II Column (f)  Description:  Balance due  most recent xpath: /IRS990ScheduleL/LoansBtwnOrgInterestedPrsnGrp/BalanceDueAmt 

#######
#
# IRS990ScheduleL - SkdLGrntAsstBnftIntrstdPrsn - Part III content
# A repeating structure from skedl_part_iii
#
#######

class SkdLGrntAsstBnftIntrstdPrsn(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    RltnshpWthOrgTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part III Column (b)  Description:  Relationship with organization  most recent xpath: /IRS990ScheduleL/GrntAsstBnftInterestedPrsnGrp/RelationshipWithOrgTxt 

    PrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part III Column (a)  Description:  Name of interested person - Person  most recent xpath: /IRS990ScheduleL/GrntAsstBnftInterestedPrsnGrp/PersonNm 

    BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part III Column (a)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleL/GrntAsstBnftInterestedPrsnGrp/BusinessName/BusinessNameLine1Txt 

    CshGrntAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Column (c)  Description:  Amount of grant  most recent xpath: /IRS990ScheduleL/GrntAsstBnftInterestedPrsnGrp/CashGrantAmt 

    BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part III Column (a)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleL/GrntAsstBnftInterestedPrsnGrp/BusinessName/BusinessNameLine2Txt 

    OfAssstncTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part III Column (d)  Description:  Type of assistance  most recent xpath: /IRS990ScheduleL/GrntAsstBnftInterestedPrsnGrp/TypeOfAssistanceTxt 

    AssstncPrpsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part III Column (e)  Description:  Purpose of assistance  most recent xpath: /IRS990ScheduleL/GrntAsstBnftInterestedPrsnGrp/AssistancePurposeTxt 

#######
#
# IRS990ScheduleL - SkdLBsTrInvlvIntrstdPrsn - Part IV content
# A repeating structure from skedl_part_iv
#
#######

class SkdLBsTrInvlvIntrstdPrsn(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part IV Column (a)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleL/BusTrInvolveInterestedPrsnGrp/NameOfInterested/BusinessName/BusinessNameLine1Txt 

    TrnsctnAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IV Column (c)  Description:  Amount of transaction  most recent xpath: /IRS990ScheduleL/BusTrInvolveInterestedPrsnGrp/TransactionAmt 

    TrnsctnDsc = models.TextField(null=True, blank=True)
    # Line number: Part IV Column (d)  Description:  Description of transaction  most recent xpath: /IRS990ScheduleL/BusTrInvolveInterestedPrsnGrp/TransactionDesc 

    ShrngOfRvnsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part IV Column (e)  Description:  Sharing of revenues?  most recent xpath: /IRS990ScheduleL/BusTrInvolveInterestedPrsnGrp/SharingOfRevenuesInd 

    PrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part IV Column (a)  Description:  Name - Person  most recent xpath: /IRS990ScheduleL/BusTrInvolveInterestedPrsnGrp/NameOfInterested/PersonNm 

    RltnshpDscrptnTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part IV Column (b)  Description:  Relationship with organization  most recent xpath: /IRS990ScheduleL/BusTrInvolveInterestedPrsnGrp/RelationshipDescriptionTxt 

    BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part IV Column (a)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleL/BusTrInvolveInterestedPrsnGrp/NameOfInterested/BusinessName/BusinessNameLine2Txt 

#######
#
# IRS990ScheduleL - SkdLSpplmntlInfrmtnDtl - Part V contents
# A repeating structure from skedl_part_v
#
#######

class SkdLSpplmntlInfrmtnDtl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FrmAndLnRfrncDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part V  Description:  Form, part and line number reference  most recent xpath: /IRS990ScheduleL/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = models.TextField(null=True, blank=True)
    # Line number: Part V  Description:  Form, part and line number reference explanation  most recent xpath: /IRS990ScheduleL/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleM - ScheduleM Part I Types of Property 
#
#######

class skedm_part_i(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    ScrtsMsc_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/SecuritiesMiscellaneousGrp/NonCashCheckboxInd 

    Txdrmy_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/TaxidermyGrp/MethodOfDeterminingRevenuesTxt 

    IntllctlPrprty_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/IntellectualPropertyGrp/ContributionCnt 

    ScrtsMsc_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/SecuritiesMiscellaneousGrp/MethodOfDeterminingRevenuesTxt 

    BtsAndPlns_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/BoatsAndPlanesGrp/NoncashContributionsRptF990Amt 

    QlfdCntrbHstStrct_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/QualifiedContribHistStructGrp/ContributionCnt 

    ArtFrctnlIntrst_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/ArtFractionalInterestGrp/NoncashContributionsRptF990Amt 

    RlEsttRsdntl_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/RealEstateResidentialGrp/NonCashCheckboxInd 

    ArtHstrclTrsrs_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/ArtHistoricalTreasuresGrp/ContributionCnt 

    DrgsAndMdclSppls_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/DrugsAndMedicalSuppliesGrp/NonCashCheckboxInd 

    IntllctlPrprty_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/IntellectualPropertyGrp/NoncashContributionsRptF990Amt 

    RlEsttRsdntl_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/RealEstateResidentialGrp/NoncashContributionsRptF990Amt 

    HstrclArtfcts_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/HistoricalArtifactsGrp/NoncashContributionsRptF990Amt 

    CrsAndOthrVhcls_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/CarsAndOtherVehiclesGrp/ContributionCnt 

    HstrclArtfcts_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/HistoricalArtifactsGrp/MethodOfDeterminingRevenuesTxt 

    ArtFrctnlIntrst_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/ArtFractionalInterestGrp/NonCashCheckboxInd 

    RlEsttCmmrcl_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/RealEstateCommercialGrp/ContributionCnt 

    ScrtsMsc_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/SecuritiesMiscellaneousGrp/NoncashContributionsRptF990Amt 

    BksAndPblctns_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/BooksAndPublicationsGrp/NonCashCheckboxInd 

    SkdM_RvwPrcssUnslNCGftsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 31  Description: Review process reference unusual noncash gifts?  most recent xpath: /IRS990ScheduleM/ReviewProcessUnusualNCGiftsInd 

    HstrclArtfcts_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/HistoricalArtifactsGrp/NonCashCheckboxInd 

    DrgsAndMdclSppls_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/DrugsAndMedicalSuppliesGrp/ContributionCnt 

    ScrtsPblclyTrdd_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/SecuritiesPubliclyTradedGrp/NonCashCheckboxInd 

    QlfdCntrbOthr_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/QualifiedContribOtherGrp/NoncashContributionsRptF990Amt 

    SkdM_Frm8283RcvdCnt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Line 29  Description: Number of 8283s received  most recent xpath: /IRS990ScheduleM/Form8283ReceivedCnt 

    ScrPrtnrshpTrstIntrsts_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/SecurPrtnrshpTrustIntrstsGrp/NonCashCheckboxInd 

    ClthngAndHshldGds_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/ClothingAndHouseholdGoodsGrp/ContributionCnt 

    ScrPrtnrshpTrstIntrsts_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/SecurPrtnrshpTrustIntrstsGrp/NoncashContributionsRptF990Amt 

    BksAndPblctns_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/BooksAndPublicationsGrp/MethodOfDeterminingRevenuesTxt 

    IntllctlPrprty_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/IntellectualPropertyGrp/MethodOfDeterminingRevenuesTxt 

    QlfdCntrbHstStrct_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/QualifiedContribHistStructGrp/NonCashCheckboxInd 

    ScrtsPblclyTrdd_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/SecuritiesPubliclyTradedGrp/ContributionCnt 

    ScntfcSpcmns_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/ScientificSpecimensGrp/NonCashCheckboxInd 

    DrgsAndMdclSppls_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/DrugsAndMedicalSuppliesGrp/MethodOfDeterminingRevenuesTxt 

    WrksOfArt_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/WorksOfArtGrp/MethodOfDeterminingRevenuesTxt 

    QlfdCntrbHstStrct_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/QualifiedContribHistStructGrp/NoncashContributionsRptF990Amt 

    RlEsttCmmrcl_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/RealEstateCommercialGrp/MethodOfDeterminingRevenuesTxt 

    RlEsttOthr_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/RealEstateOtherGrp/NonCashCheckboxInd 

    Txdrmy_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/TaxidermyGrp/ContributionCnt 

    RlEsttRsdntl_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/RealEstateResidentialGrp/ContributionCnt 

    BtsAndPlns_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/BoatsAndPlanesGrp/MethodOfDeterminingRevenuesTxt 

    ScrtsPblclyTrdd_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/SecuritiesPubliclyTradedGrp/NoncashContributionsRptF990Amt 

    ArchlgclArtfcts_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/ArchaeologicalArtifactsGrp/NoncashContributionsRptF990Amt 

    BtsAndPlns_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/BoatsAndPlanesGrp/ContributionCnt 

    Cllctbls_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/CollectiblesGrp/NoncashContributionsRptF990Amt 

    ArchlgclArtfcts_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/ArchaeologicalArtifactsGrp/NonCashCheckboxInd 

    CrsAndOthrVhcls_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/CarsAndOtherVehiclesGrp/NonCashCheckboxInd 

    FdInvntry_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/FoodInventoryGrp/NonCashCheckboxInd 

    RlEsttRsdntl_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/RealEstateResidentialGrp/MethodOfDeterminingRevenuesTxt 

    QlfdCntrbOthr_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/QualifiedContribOtherGrp/MethodOfDeterminingRevenuesTxt 

    ScrtsPblclyTrdd_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/SecuritiesPubliclyTradedGrp/MethodOfDeterminingRevenuesTxt 

    QlfdCntrbHstStrct_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/QualifiedContribHistStructGrp/MethodOfDeterminingRevenuesTxt 

    ArtHstrclTrsrs_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/ArtHistoricalTreasuresGrp/NonCashCheckboxInd 

    HstrclArtfcts_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/HistoricalArtifactsGrp/ContributionCnt 

    ClthngAndHshldGds_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/ClothingAndHouseholdGoodsGrp/NoncashContributionsRptF990Amt 

    Cllctbls_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/CollectiblesGrp/NonCashCheckboxInd 

    ScntfcSpcmns_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/ScientificSpecimensGrp/MethodOfDeterminingRevenuesTxt 

    ScrtsClslyHldStck_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/SecuritiesCloselyHeldStockGrp/ContributionCnt 

    RlEsttCmmrcl_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/RealEstateCommercialGrp/NoncashContributionsRptF990Amt 

    RlEsttOthr_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/RealEstateOtherGrp/NoncashContributionsRptF990Amt 

    RlEsttOthr_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/RealEstateOtherGrp/MethodOfDeterminingRevenuesTxt 

    ArtHstrclTrsrs_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/ArtHistoricalTreasuresGrp/NoncashContributionsRptF990Amt 

    ScrPrtnrshpTrstIntrsts_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/SecurPrtnrshpTrustIntrstsGrp/MethodOfDeterminingRevenuesTxt 

    WrksOfArt_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/WorksOfArtGrp/ContributionCnt 

    SkdM_AnyPrprtyThtMstBHldInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 30a  Description: Any property that must be held?  most recent xpath: /IRS990ScheduleM/AnyPropertyThatMustBeHeldInd 

    DrgsAndMdclSppls_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/DrugsAndMedicalSuppliesGrp/NoncashContributionsRptF990Amt 

    ArchlgclArtfcts_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/ArchaeologicalArtifactsGrp/ContributionCnt 

    FdInvntry_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/FoodInventoryGrp/ContributionCnt 

    ScrtsClslyHldStck_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/SecuritiesCloselyHeldStockGrp/MethodOfDeterminingRevenuesTxt 

    QlfdCntrbOthr_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/QualifiedContribOtherGrp/NonCashCheckboxInd 

    BtsAndPlns_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/BoatsAndPlanesGrp/NonCashCheckboxInd 

    QlfdCntrbOthr_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/QualifiedContribOtherGrp/ContributionCnt 

    SkdM_ThrdPrtsUsdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 32a  Description: Third parties used?  most recent xpath: /IRS990ScheduleM/ThirdPartiesUsedInd 

    ScntfcSpcmns_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/ScientificSpecimensGrp/NoncashContributionsRptF990Amt 

    WrksOfArt_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/WorksOfArtGrp/NoncashContributionsRptF990Amt 

    FdInvntry_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/FoodInventoryGrp/NoncashContributionsRptF990Amt 

    Cllctbls_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/CollectiblesGrp/MethodOfDeterminingRevenuesTxt 

    ArchlgclArtfcts_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/ArchaeologicalArtifactsGrp/MethodOfDeterminingRevenuesTxt 

    ArtFrctnlIntrst_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/ArtFractionalInterestGrp/MethodOfDeterminingRevenuesTxt 

    ArtFrctnlIntrst_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/ArtFractionalInterestGrp/ContributionCnt 

    Cllctbls_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/CollectiblesGrp/ContributionCnt 

    ScrPrtnrshpTrstIntrsts_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/SecurPrtnrshpTrustIntrstsGrp/ContributionCnt 

    Txdrmy_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/TaxidermyGrp/NonCashCheckboxInd 

    ScrtsMsc_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/SecuritiesMiscellaneousGrp/ContributionCnt 

    RlEsttCmmrcl_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/RealEstateCommercialGrp/NonCashCheckboxInd 

    IntllctlPrprty_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/IntellectualPropertyGrp/NonCashCheckboxInd 

    BksAndPblctns_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/BooksAndPublicationsGrp/ContributionCnt 

    BksAndPblctns_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/BooksAndPublicationsGrp/NoncashContributionsRptF990Amt 

    Txdrmy_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/TaxidermyGrp/NoncashContributionsRptF990Amt 

    ClthngAndHshldGds_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/ClothingAndHouseholdGoodsGrp/NonCashCheckboxInd 

    CrsAndOthrVhcls_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/CarsAndOtherVehiclesGrp/MethodOfDeterminingRevenuesTxt 

    ClthngAndHshldGds_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/ClothingAndHouseholdGoodsGrp/MethodOfDeterminingRevenuesTxt 

    CrsAndOthrVhcls_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/CarsAndOtherVehiclesGrp/NoncashContributionsRptF990Amt 

    FdInvntry_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/FoodInventoryGrp/MethodOfDeterminingRevenuesTxt 

    RlEsttOthr_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/RealEstateOtherGrp/ContributionCnt 

    ScrtsClslyHldStck_NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/SecuritiesCloselyHeldStockGrp/NoncashContributionsRptF990Amt 

    ArtHstrclTrsrs_MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/ArtHistoricalTreasuresGrp/MethodOfDeterminingRevenuesTxt 

    ScrtsClslyHldStck_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/SecuritiesCloselyHeldStockGrp/NonCashCheckboxInd 

    WrksOfArt_NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/WorksOfArtGrp/NonCashCheckboxInd 

    ScntfcSpcmns_CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/ScientificSpecimensGrp/ContributionCnt 

#######
#
# IRS990ScheduleM - SkdMOthrNnCshCntrTbl
# A repeating structure from skedm_part_i
#
#######

class SkdMOthrNnCshCntrTbl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    Dsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Lines 25 - 28  Description:  Description  most recent xpath: /IRS990ScheduleM/OtherNonCashContriTableGrp/Desc 

    NncshCntrbtnsRptF990Amt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Revenues reported on F990, Pt VIII, line 1g  most recent xpath: /IRS990ScheduleM/OtherNonCashContriTableGrp/NoncashContributionsRptF990Amt 

    NnCshChckbxInd = models.CharField(null=True, blank=True, max_length=1)
    # Line number:  Column (a)  Description:  Checkbox for lines on Part I  most recent xpath: /IRS990ScheduleM/OtherNonCashContriTableGrp/NonCashCheckboxInd 

    CntrbtnCnt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (b)  Description:  Number of contributions  most recent xpath: /IRS990ScheduleM/OtherNonCashContriTableGrp/ContributionCnt 

    MthdOfDtrmnngRvnsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (d)  Description:  Method of determining revenues  most recent xpath: /IRS990ScheduleM/OtherNonCashContriTableGrp/MethodOfDeterminingRevenuesTxt 

#######
#
# IRS990ScheduleM - SkdMSpplmntlInfrmtnDtl - Explanation repeating group
# A repeating structure from skedm_part_ii
#
#######

class SkdMSpplmntlInfrmtnDtl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FrmAndLnRfrncDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Part II  Description:  Form, part and line number reference  most recent xpath: /IRS990ScheduleM/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = models.TextField(null=True, blank=True)
    # Line number:  Part II  Description:  Form, part and line number reference explanation  most recent xpath: /IRS990ScheduleM/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleN - ScheduleN Part I Liquidation, Termination or Dissolution 
#
#######

class skedn_part_i(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    EmplyOfSccssrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 2b  Description: Become an employee of, or independent contractor for, a successor or transferee organization?  most recent xpath: /IRS990ScheduleN/EmployeeOfSuccessorInd 

    LbltsPdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 5  Description: Did the organization discharge or pay all liabilities in accordance with state laws?  most recent xpath: /IRS990ScheduleN/LiabilitiesPaidInd 

    DrctrOfSccssrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 2a  Description: Become a director or trustee of a successor or transferee organization?  most recent xpath: /IRS990ScheduleN/DirectorOfSuccessorInd 

    AttrnyGnrlNtfdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 4b  Description: If "Yes," did the organization provide such notice?  most recent xpath: /IRS990ScheduleN/AttorneyGeneralNotifiedInd 

    RqrdTNtfyAGInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 4a  Description: Is the organization required to notify the attorney general or other appropriate state official of its intent to dissolve?  most recent xpath: /IRS990ScheduleN/RequiredToNotifyAGInd 

    RcvCmpnstnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 2d  Description: Receive, or become entitled to, compensation or other similar payments as a result of the organization's liquidation, termination, or dissolution?  most recent xpath: /IRS990ScheduleN/ReceiveCompensationInd 

    OwnrOfSccssrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 2c  Description: Become a direct or indirect owner of a successor or transferee organization?  most recent xpath: /IRS990ScheduleN/OwnerOfSuccessorInd 

    BndLbltsDschrgdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 6b  Description: Did the organization discharge or defease tax-exempt bond liabilities in accordance with the Internal Revenue Code and state laws?  most recent xpath: /IRS990ScheduleN/BondLiabilitiesDischargedInd 

    AsstsDstrbtdInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 3  Description: Did the organization distribute its assets in accordance with its governing instruments?  most recent xpath: /IRS990ScheduleN/AssetsDistributedInd 

    BndsOtstndngInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part I Line 6a  Description: Did the organization have any tax-exempt bonds outstanding during the year?  most recent xpath: /IRS990ScheduleN/BondsOutstandingInd 

#######
#
# IRS990ScheduleN - ScheduleN Part II Sale, Exchange, Disposition or Other Transfer of more than 25% of the Organization's Assets 
#
#######

class skedn_part_ii(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    EmplyOfSccssr2Ind = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part II Line 2b  Description: Become an employee of, or independent contractor for, a successor or transferee organization?  most recent xpath: /IRS990ScheduleN/EmployeeOfSuccessor2Ind 

    RcvCmpnstn2Ind = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part II Line 2d  Description: Receive, or become entitled to, compensation or other similar payments as a result of the organization's significant disposition of assets?  most recent xpath: /IRS990ScheduleN/ReceiveCompensation2Ind 

    DrctrOfSccssr2Ind = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part II Line 2a  Description: Become a director or trustee of a successor or transferee organization?  most recent xpath: /IRS990ScheduleN/DirectorOfSuccessor2Ind 

    OwnrOfSccssr2Ind = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part II Line 2c  Description: Become a direct or indirect owner of a successor or transferee organization?  most recent xpath: /IRS990ScheduleN/OwnerOfSuccessor2Ind 

#######
#
# IRS990ScheduleN - SkdNLqdtnOfAsstsDtl
# A repeating structure from skedn_part_i
#
#######

class SkdNLqdtnOfAsstsDtl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    LqdtnOfAsstsDtl_MthdOfFMVDtrmntnTxt = models.TextField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Method of determining FMV for asset(s) distributed or transactional expenses  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/MethodOfFMVDeterminationTxt 

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number:  Column (f)  Description:  ZIP code  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/USAddress/ZIPCd 

    FrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number:  Column (f)  Description:  Postal code  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/ForeignAddress/ForeignPostalCd 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Column (f)  Description:  Address line 1  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/USAddress/AddressLine1Txt 

    FrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Column (f)  Description:  Country  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/ForeignAddress/CountryCd 

    FrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number:  Column (f)  Description:  Province or state  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number:  Column (f)  Description:  City  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/ForeignAddress/CityNm 

    LqdtnOfAsstsDtl_EIN = models.CharField(null=True, blank=True, max_length=9)
    # Line number:  Column (e)  Description:  EIN of recipient (if tax-exempt)  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/EIN 

    BsnssNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Column (f)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/BusinessName/BusinessNameLine2Txt 

    BsnssNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Column (f)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/BusinessName/BusinessNameLine1Txt 

    LqdtnOfAsstsDtl_IRCSctnTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (g)  Description:  IRC code section of recipient(s) (if tax-exempt) or type of entity  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/IRCSectionTxt 

    LqdtnOfAsstsDtl_PrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Column (f)  Description:  Name - Person  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/PersonNm 

    LqdtnOfAsstsDtl_FrMrktVlOfAsstAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Fair market value of asset(s) distributed or amount of transactional expenses  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/FairMarketValueOfAssetAmt 

    FrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Column (f)  Description:  Address line 2  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/ForeignAddress/AddressLine2Txt 

    LqdtnOfAsstsDtl_DstrbtnDt = models.CharField(null=True, blank=True, max_length=31)
    # Line number:  Column (b)  Description:  Date of distribution  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/DistributionDt 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Column (f)  Description:  Address line 2  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/USAddress/AddressLine2Txt 

    FrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Column (f)  Description:  Address line 1  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/ForeignAddress/AddressLine1Txt 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number:  Column (f)  Description:  City  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/USAddress/CityNm 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Column (f)  Description:  State  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/USAddress/StateAbbreviationCd 

    LqdtnOfAsstsDtl_AsstsDstrOrExpnssPdDsc = models.TextField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Description of asset(s) distributed or transactional expenses paid  most recent xpath: /IRS990ScheduleN/LiquidationOfAssetsTableGrp/LiquidationOfAssetsDetail/AssetsDistriOrExpnssPaidDesc 

#######
#
# IRS990ScheduleN - SkdNDspstnOfAsstsDtl
# A repeating structure from skedn_part_ii
#
#######

class SkdNDspstnOfAsstsDtl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Column (f)  Description:  Address line 1  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/ForeignAddress/AddressLine1Txt 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Column (f)  Description:  State  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/USAddress/StateAbbreviationCd 

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number:  Column (f)  Description:  ZIP code  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/USAddress/ZIPCd 

    DspstnOfAsstsDtl_FrMrktVlOfAsstAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Column (c)  Description:  Fair market value of asset(s) distributed or amount of transactional expenses  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/FairMarketValueOfAssetAmt 

    FrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number:  Column (f)  Description:  City  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/ForeignAddress/CityNm 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Column (f)  Description:  Address line 2  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/USAddress/AddressLine2Txt 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Column (f)  Description:  Address line 1  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/USAddress/AddressLine1Txt 

    DspstnOfAsstsDtl_PrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Column (f)  Description:  Name - Person  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/PersonNm 

    BsnssNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Column (f)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/BusinessName/BusinessNameLine2Txt 

    BsnssNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Column (f)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/BusinessName/BusinessNameLine1Txt 

    DspstnOfAsstsDtl_MthdOfFMVDtrmntnTxt = models.TextField(null=True, blank=True)
    # Line number:  Column (d)  Description:  Method of determining FMV for asset(s) distributed or transactional expenses  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/MethodOfFMVDeterminationTxt 

    FrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number:  Column (f)  Description:  Postal code  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/ForeignAddress/ForeignPostalCd 

    FrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number:  Column (f)  Description:  Country  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/ForeignAddress/CountryCd 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number:  Column (f)  Description:  City  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/USAddress/CityNm 

    DspstnOfAsstsDtl_DstrbtnDt = models.CharField(null=True, blank=True, max_length=31)
    # Line number:  Column (b)  Description:  Date of distribution  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/DistributionDt 

    DspstnOfAsstsDtl_AsstsDstrOrExpnssPdDsc = models.TextField(null=True, blank=True)
    # Line number:  Column (a)  Description:  Description of asset(s) distributed or transactional expenses paid  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/AssetsDistriOrExpnssPaidDesc 

    DspstnOfAsstsDtl_EIN = models.CharField(null=True, blank=True, max_length=9)
    # Line number:  Column (e)  Description:  EIN of recipient (if tax-exempt)  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/EIN 

    FrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number:  Column (f)  Description:  Address line 2  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number:  Column (f)  Description:  Province or state  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/ForeignAddress/ProvinceOrStateNm 

    DspstnOfAsstsDtl_IRCSctnTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number:  Column (g)  Description:  IRC code section of recipient(s) (if tax-exempt) or type of entity  most recent xpath: /IRS990ScheduleN/DispositionOfAssetsDetail/IRCSectionTxt 

#######
#
# IRS990ScheduleN - SkdNSpplmntlInfrmtnDtl - Part III contents
# A repeating structure from skedn_part_iii
#
#######

class SkdNSpplmntlInfrmtnDtl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    ExplntnTxt = models.TextField(null=True, blank=True)
    # Line number: Part III  Description:  Form, part and line number reference explanation  most recent xpath: /IRS990ScheduleN/SupplementalInformationDetail/ExplanationTxt 

    FrmAndLnRfrncDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part III  Description:  Form, part and line number reference  most recent xpath: /IRS990ScheduleN/SupplementalInformationDetail/FormAndLineReferenceDesc 

#######
#
# IRS990ScheduleO - SkdOSpplmntlInfrmtnDtl
# A repeating structure from skedo_part_i
#
#######

class SkdOSpplmntlInfrmtnDtl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    FrmAndLnRfrncDsc = models.CharField(null=True, blank=True, max_length=100)
    # Description: Form, part and line number reference  most recent xpath: /IRS990ScheduleO/SupplementalInformationDetail/FormAndLineReferenceDesc 

    ExplntnTxt = models.TextField(null=True, blank=True)
    # Description: Form, part and line number reference explanation  most recent xpath: /IRS990ScheduleO/SupplementalInformationDetail/ExplanationTxt 

#######
#
# IRS990ScheduleR - ScheduleR Part V - Transactions with Related Organizations and Noncharitable Exempt Organizations 
#
#######

class skedr_part_v(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    AsstPrchsFrmOthrOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1h  Description: Purchase of assets from other organization?  most recent xpath: /IRS990ScheduleR/AssetPurchaseFromOtherOrgInd 

    GftGrntOrCpCntrTOthOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1b  Description: Gift, grant, or capital contribution to other organization?  most recent xpath: /IRS990ScheduleR/GiftGrntOrCapContriToOthOrgInd 

    DvRltdOrgnztnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1f  Description: Dividends from related organization(s)? (Y-N)  most recent xpath: /IRS990ScheduleR/DivRelatedOrganizationInd 

    PrfrmOfSrvcsByOthrOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1m  Description: Performance of services or membership or fundraising solicitations by other organizations?  most recent xpath: /IRS990ScheduleR/PerformOfServicesByOtherOrgInd 

    RntlOfFcltsFrmOthOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1k  Description: Lease of facilities, equipment, or other assets from other organizations?  most recent xpath: /IRS990ScheduleR/RentalOfFcltsFromOthOrgInd 

    LnsOrGrntsFrmOthOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1e  Description: Loans or loan guarantees by other organization?  most recent xpath: /IRS990ScheduleR/LoansOrGuaranteesFromOthOrgInd 

    PrfrmOfSrvcsFrOthOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1l  Description: Performance of services or membership or fundraising solicitations for other organizations?  most recent xpath: /IRS990ScheduleR/PerformOfServicesForOthOrgInd 

    TrnsfrTOthrOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1r  Description: Other transfer of cash or property to other organization?  most recent xpath: /IRS990ScheduleR/TransferToOtherOrgInd 

    RmbrsmntPdByOthrOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1q  Description: Reimbursement paid by other organization for expenses?  most recent xpath: /IRS990ScheduleR/ReimbursementPaidByOtherOrgInd 

    RntlOfFcltsTOthOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1j  Description: Lease of facilities, equipment, or other assets to other organizations?  most recent xpath: /IRS990ScheduleR/RentalOfFacilitiesToOthOrgInd 

    AsstSlTOthrOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1g  Description: Sale of assets to other organization?  most recent xpath: /IRS990ScheduleR/AssetSaleToOtherOrgInd 

    AsstExchngInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1i  Description: Exchange of assets?  most recent xpath: /IRS990ScheduleR/AssetExchangeInd 

    RcptOfIntAnntsRntsRyltsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1a  Description: Receipt of interest, annuities, rents, royalties?  most recent xpath: /IRS990ScheduleR/ReceiptOfIntAnntsRntsRyltsInd 

    PdEmplysShrngInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1o  Description: Sharing of paid employees?  most recent xpath: /IRS990ScheduleR/PaidEmployeesSharingInd 

    TrnsfrFrmOthrOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1s  Description: Other transfer of cash or property from other organization?  most recent xpath: /IRS990ScheduleR/TransferFromOtherOrgInd 

    RmbrsmntPdTOthrOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1p  Description: Reimbursement paid to other organization for expenses?  most recent xpath: /IRS990ScheduleR/ReimbursementPaidToOtherOrgInd 

    ShrngOfFcltsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1n  Description: Sharing of facilities, equipment, mailing lists, other assets, or employees?  most recent xpath: /IRS990ScheduleR/SharingOfFacilitiesInd 

    GftGrntCpCntrFrmOthOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1c  Description: Gift, grant, or capital contribution from other organization?  most recent xpath: /IRS990ScheduleR/GiftGrntCapContriFromOthOrgInd 

    LnsOrGrntsTOthrOrgInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part V Line 1d  Description: Loans or loan guarantees to or for other organization?  most recent xpath: /IRS990ScheduleR/LoansOrGuaranteesToOtherOrgInd 

#######
#
# IRS990ScheduleR - SkdRIdDsrgrddEntts - Part I content - Identification of disregarded entities
# A repeating structure from skedr_part_i
#
#######

class SkdRIdDsrgrddEntts(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    DsrgrddEnttyNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part I Column (a)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/DisregardedEntityName/BusinessNameLine1Txt 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part I Column (a)  Description:  State  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/USAddress/StateAbbreviationCd 

    IdDsrgrddEntts_EndOfYrAsstsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Column (e)  Description:  End-of-year assets ($)  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/EndOfYearAssetsAmt 

    DrctCntrllngEnttyNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part I Column (f)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/DirectControllingEntityName/BusinessNameLine2Txt 

    DrctCntrllngEnttyNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part I Column (f)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/DirectControllingEntityName/BusinessNameLine1Txt 

    IdDsrgrddEntts_PrmryActvtsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part I Column (b)  Description:  Nature of activities  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/PrimaryActivitiesTxt 

    IdDsrgrddEntts_EIN = models.CharField(null=True, blank=True, max_length=9)
    # Line number: Part I Column (a)  Description:  EIN  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/EIN 

    FrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number: Part I Column (a)  Description:  Postal code  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/ForeignAddress/ForeignPostalCd 

    FrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part I Column (a)  Description:  Country  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/ForeignAddress/CountryCd 

    DsrgrddEnttyNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part I Column (a)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/DisregardedEntityName/BusinessNameLine2Txt 

    FrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part I Column (a)  Description:  Address line 2  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part I Column (a)  Description:  Address line 1  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/ForeignAddress/AddressLine1Txt 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part I Column (a)  Description:  Address line 2  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/USAddress/AddressLine2Txt 

    IdDsrgrddEntts_TtlIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part I Column (d)  Description:  Total income ($)  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/TotalIncomeAmt 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number: Part I Column (a)  Description:  City  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/USAddress/CityNm 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part I Column (a)  Description:  Address line 1  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/USAddress/AddressLine1Txt 

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number: Part I Column (a)  Description:  ZIP code  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/USAddress/ZIPCd 

    IdDsrgrddEntts_DrctCntrllngNACd = models.TextField(null=True, blank=True)
    # Line number: Part I Column (f)  Description:  Direct controlling entity - Literal for not applicable  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/DirectControllingNACd 

    FrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number: Part I Column (a)  Description:  Province or state  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/ForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number: Part I Column (a)  Description:  City  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/ForeignAddress/CityNm 

    IdDsrgrddEntts_LglDmclFrgnCntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part I Column (c)  Description:  Legal domicile - Foreign Country  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/LegalDomicileForeignCountryCd 

    IdDsrgrddEntts_LglDmclSttCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part I Column (c)  Description:  Legal domicile - State  most recent xpath: /IRS990ScheduleR/IdDisregardedEntitiesGrp/LegalDomicileStateCd 

#######
#
# IRS990ScheduleR - SkdRIdRltdTxExmptOrg - Part II content - Identification of related tax-exempt organizations
# A repeating structure from skedr_part_ii
#
#######

class SkdRIdRltdTxExmptOrg(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number: Part II Column (a)  Description:  ZIP code  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/USAddress/ZIPCd 

    IdRltdTxExmptOrg_EIN = models.CharField(null=True, blank=True, max_length=9)
    # Line number: Part II Column (a)  Description:  EIN  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/EIN 

    FrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part II Column (a)  Description:  Address line 1  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/ForeignAddress/AddressLine1Txt 

    IdRltdTxExmptOrg_ExmptCdSctnTxt = models.CharField(null=True, blank=True, max_length=20)
    # Line number: Part II Column (d)  Description:  Exempt code section  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/ExemptCodeSectionTxt 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part II Column (a)  Description:  State  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/USAddress/StateAbbreviationCd 

    FrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number: Part II Column (a)  Description:  City  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/ForeignAddress/CityNm 

    IdRltdTxExmptOrg_LglDmclSttCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part II Column (c)  Description:  Legal domicile - State  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/LegalDomicileStateCd 

    FrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part II Column (a)  Description:  Address line 2  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/ForeignAddress/AddressLine2Txt 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part II Column (a)  Description:  Address line 2  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/USAddress/AddressLine2Txt 

    DsrgrddEnttyNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part II Column (a)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/DisregardedEntityName/BusinessNameLine1Txt 

    IdRltdTxExmptOrg_CntrlldOrgnztnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part II Column (g)  Description:  512(b)(13) controlled organization? (Y-N)  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/ControlledOrganizationInd 

    FrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number: Part II Column (a)  Description:  Postal code  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/ForeignAddress/ForeignPostalCd 

    DrctCntrllngEnttyNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part II Column (f)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/DirectControllingEntityName/BusinessNameLine1Txt 

    DsrgrddEnttyNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part II Column (a)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/DisregardedEntityName/BusinessNameLine2Txt 

    FrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number: Part II Column (a)  Description:  Province or state  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/ForeignAddress/ProvinceOrStateNm 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number: Part II Column (a)  Description:  City  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/USAddress/CityNm 

    IdRltdTxExmptOrg_LglDmclFrgnCntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part II Column (c)  Description:  Legal domicile - Foreign Country  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/LegalDomicileForeignCountryCd 

    FrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part II Column (a)  Description:  Country  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/ForeignAddress/CountryCd 

    IdRltdTxExmptOrg_PrmryActvtsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part II Column (b)  Description:  Primary activities  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/PrimaryActivitiesTxt 

    IdRltdTxExmptOrg_DrctCntrllngNACd = models.TextField(null=True, blank=True)
    # Line number: Part II Column (f)  Description:  Direct controlling entity - Literal for not applicable  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/DirectControllingNACd 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part II Column (a)  Description:  Address line 1  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/USAddress/AddressLine1Txt 

    DrctCntrllngEnttyNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part II Column (f)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/DirectControllingEntityName/BusinessNameLine2Txt 

    IdRltdTxExmptOrg_PblcChrtySttsTxt = models.CharField(null=True, blank=True, max_length=20)
    # Line number: Part II Column (e)  Description:  Public charity status (if 501(c)(3))  most recent xpath: /IRS990ScheduleR/IdRelatedTaxExemptOrgGrp/PublicCharityStatusTxt 

#######
#
# IRS990ScheduleR - SkdRIdRltdOrgTxblPrtnrshp - Part III content - Identification of related organizations taxable as a partnership
# A repeating structure from skedr_part_iii
#
#######

class SkdRIdRltdOrgTxblPrtnrshp(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    IdRltdOrgTxblPrtnrshp_PrdmnntIncmTxt = models.CharField(null=True, blank=True, max_length=20)
    # Line number: Part III Column (e)  Description:  Predominant income (related, investment, unrelated)  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/PredominantIncomeTypeTxt 

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number: Part III Column (a)  Description:  ZIP code  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/USAddress/ZIPCd 

    IdRltdOrgTxblPrtnrshp_EIN = models.CharField(null=True, blank=True, max_length=9)
    # Line number: Part III Column (a)  Description:  EIN  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/EIN 

    DrctCntrllngEnttyNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part III Column (d)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/DirectControllingEntityName/BusinessNameLine1Txt 

    IdRltdOrgTxblPrtnrshp_PrmryActvtsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part III Column (b)  Description:  Primary business activity, product or service  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/PrimaryActivitiesTxt 

    IdRltdOrgTxblPrtnrshp_DrctCntrllngNACd = models.TextField(null=True, blank=True)
    # Line number: Part III Column (d)  Description:  Direct controlling entity - Literal for not applicable  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/DirectControllingNACd 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part III Column (a)  Description:  Address line 1  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/USAddress/AddressLine1Txt 

    RltdOrgnztnNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part III Column (a)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/RelatedOrganizationName/BusinessNameLine2Txt 

    IdRltdOrgTxblPrtnrshp_LglDmclSttCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part III Column (c)  Description:  Legal domicile - State  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/LegalDomicileStateCd 

    FrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number: Part III Column (a)  Description:  Postal code  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/ForeignAddress/ForeignPostalCd 

    IdRltdOrgTxblPrtnrshp_ShrOfEOYAsstsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Column (g)  Description:  Share of end-of-year assets ($)  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/ShareOfEOYAssetsAmt 

    FrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part III Column (a)  Description:  Address line 1  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/ForeignAddress/AddressLine1Txt 

    IdRltdOrgTxblPrtnrshp_OwnrshpPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number: Part III Column (k)  Description:  Percentage ownership  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/OwnershipPct 

    IdRltdOrgTxblPrtnrshp_ShrOfTtlIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Column (f)  Description:  Share of total income ($)  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/ShareOfTotalIncomeAmt 

    RltdOrgnztnNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part III Column (a)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/RelatedOrganizationName/BusinessNameLine1Txt 

    IdRltdOrgTxblPrtnrshp_DsprprtntAllctnsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part III Column (h)  Description:  Disproportionate allocations? (Y-N)  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/DisproportionateAllocationsInd 

    IdRltdOrgTxblPrtnrshp_LglDmclFrgnCntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part III Column (c)  Description:  Legal domicile - Foreign Country  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/LegalDomicileForeignCountryCd 

    IdRltdOrgTxblPrtnrshp_GnrlOrMngngPrtnrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part III Column (j)  Description:  General or managing partner? (Y-N)  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/GeneralOrManagingPartnerInd 

    IdRltdOrgTxblPrtnrshp_UBICdVAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part III Column (i)  Description:  Code V-UBI amount on Box 20 of K-1 ($)  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/UBICodeVAmt 

    FrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part III Column (a)  Description:  Country  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/ForeignAddress/CountryCd 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part III Column (a)  Description:  State  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/USAddress/StateAbbreviationCd 

    FrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number: Part III Column (a)  Description:  Province or state  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/ForeignAddress/ProvinceOrStateNm 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number: Part III Column (a)  Description:  City  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/USAddress/CityNm 

    FrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part III Column (a)  Description:  Address line 2  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/ForeignAddress/AddressLine2Txt 

    FrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number: Part III Column (a)  Description:  City  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/ForeignAddress/CityNm 

    DrctCntrllngEnttyNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part III Column (d)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/DirectControllingEntityName/BusinessNameLine2Txt 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part III Column (a)  Description:  Address line 2  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblPartnershipGrp/USAddress/AddressLine2Txt 

#######
#
# IRS990ScheduleR - SkdRIdRltdOrgTxblCrpTr - Part IV content - Identification of related organizations taxable as a corporation or trust
# A repeating structure from skedr_part_iv
#
#######

class SkdRIdRltdOrgTxblCrpTr(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    IdRltdOrgTxblCrpTr_OwnrshpPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number: Part IV Column (h)  Description:  Percentage ownership  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/OwnershipPct 

    DrctCntrllngEnttyNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part IV Column (d)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/DirectControllingEntityName/BusinessNameLine2Txt 

    FrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number: Part IV Column (a)  Description:  City  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/ForeignAddress/CityNm 

    FrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part IV Column (a)  Description:  Address line 2  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/ForeignAddress/AddressLine2Txt 

    IdRltdOrgTxblCrpTr_EIN = models.CharField(null=True, blank=True, max_length=9)
    # Line number: Part IV Column (a)  Description:  EIN  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/EIN 

    IdRltdOrgTxblCrpTr_LglDmclFrgnCntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part IV Column (c)  Description:  Legal domicile - Foreign Country  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/LegalDomicileForeignCountryCd 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part IV Column (a)  Description:  Address line 1  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/USAddress/AddressLine1Txt 

    IdRltdOrgTxblCrpTr_CntrlldOrgnztnInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part IV Column (i)  Description:  512(b)(13) controlled organization? (Y-N)  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/ControlledOrganizationInd 

    FrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part IV Column (a)  Description:  Country  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/ForeignAddress/CountryCd 

    DrctCntrllngEnttyNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part IV Column (d)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/DirectControllingEntityName/BusinessNameLine1Txt 

    IdRltdOrgTxblCrpTr_ShrOfTtlIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IV Column (f)  Description:  Share of total income ($)  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/ShareOfTotalIncomeAmt 

    IdRltdOrgTxblCrpTr_DrctCntrllngNACd = models.TextField(null=True, blank=True)
    # Line number: Part IV Column (d)  Description:  Direct controlling entity - Literal for not applicable  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/DirectControllingNACd 

    IdRltdOrgTxblCrpTr_PrmryActvtsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part IV Column (b)  Description:  Primary activity, product or service  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/PrimaryActivitiesTxt 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number: Part IV Column (a)  Description:  City  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/USAddress/CityNm 

    FrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part IV Column (a)  Description:  Address line 1  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/ForeignAddress/AddressLine1Txt 

    IdRltdOrgTxblCrpTr_LglDmclSttCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part IV Column (c)  Description:  Legal domicile - State  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/LegalDomicileStateCd 

    IdRltdOrgTxblCrpTr_EnttyTxt = models.CharField(null=True, blank=True, max_length=20)
    # Line number: Part IV Column (e)  Description:  Type of entity (C corp, S corp, or trust)  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/EntityTypeTxt 

    FrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number: Part IV Column (a)  Description:  Postal code  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/ForeignAddress/ForeignPostalCd 

    IdRltdOrgTxblCrpTr_ShrOfEOYAsstsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part IV Column (g)  Description:  Share of end-of-year assets ($)  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/ShareOfEOYAssetsAmt 

    RltdOrgnztnNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part IV Column (a)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/RelatedOrganizationName/BusinessNameLine1Txt 

    FrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number: Part IV Column (a)  Description:  Province or state  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/ForeignAddress/ProvinceOrStateNm 

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number: Part IV Column (a)  Description:  ZIP code  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/USAddress/ZIPCd 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part IV Column (a)  Description:  Address line 2  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/USAddress/AddressLine2Txt 

    RltdOrgnztnNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part IV Column (a)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/RelatedOrganizationName/BusinessNameLine2Txt 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part IV Column (a)  Description:  State  most recent xpath: /IRS990ScheduleR/IdRelatedOrgTxblCorpTrGrp/USAddress/StateAbbreviationCd 

#######
#
# IRS990ScheduleR - SkdRTrnsctnsRltdOrg
# A repeating structure from skedr_part_v
#
#######

class SkdRTrnsctnsRltdOrg(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part V Line 2 Column (a)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleR/TransactionsRelatedOrgGrp/OtherOrganizationName/BusinessNameLine1Txt 

    TrnsctnTxt = models.TextField(null=True, blank=True)
    # Line number:  Part V Line 2 Column (b)  Description:  Transaction type, enter up to five characters  most recent xpath: /IRS990ScheduleR/TransactionsRelatedOrgGrp/TransactionTypeTxt 

    InvlvdAmt = models.BigIntegerField(null=True, blank=True)
    # Line number:  Part V Line 2 Column (c)  Description:  Amount involved ($)  most recent xpath: /IRS990ScheduleR/TransactionsRelatedOrgGrp/InvolvedAmt 

    BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number:  Part V Line 2 Column (a)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleR/TransactionsRelatedOrgGrp/OtherOrganizationName/BusinessNameLine2Txt 

    MthdOfAmntDtrmntnTxt = models.TextField(null=True, blank=True)
    # Line number:  Part V Line 2 Column (d)  Description:  Method of determining amount involved  most recent xpath: /IRS990ScheduleR/TransactionsRelatedOrgGrp/MethodOfAmountDeterminationTxt 

#######
#
# IRS990ScheduleR - SkdRUnrltdOrgTxblPrtnrshp - Part VI content
# A repeating structure from skedr_part_vi
#
#######

class SkdRUnrltdOrgTxblPrtnrshp(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    UnrltdOrgTxblPrtnrshp_EIN = models.CharField(null=True, blank=True, max_length=9)
    # Line number: Part VI Column (a)  Description:  EIN  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/EIN 

    UnrltdOrgTxblPrtnrshp_LglDmclSttCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part VI Column (c)  Description:  Legal domicile - State  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/LegalDomicileStateCd 

    UnrltdOrgTxblPrtnrshp_AllPrtnrsC3SInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Column (e)  Description:  All partners c3s?  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/AllPartnersC3SInd 

    UnrltdOrgTxblPrtnrshp_DsprprtntAllctnsInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Column (h)  Description:  Disproportionate allocations?  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/DisproportionateAllocationsInd 

    BsnssNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part VI Column (a)  Description:  Business name line 1  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/BusinessName/BusinessNameLine1Txt 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part VI Column (a)  Description:  Address line 2  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/USAddress/AddressLine2Txt 

    UnrltdOrgTxblPrtnrshp_UBICdVAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Column (i)  Description:  Code V amount  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/UBICodeVAmt 

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Line number: Part VI Column (a)  Description:  ZIP code  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/USAddress/ZIPCd 

    FrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part VI Column (a)  Description:  Address line 1  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part VI Column (a)  Description:  Address line 2  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/ForeignAddress/AddressLine2Txt 

    UnrltdOrgTxblPrtnrshp_ShrOfEOYAsstsAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Column (g)  Description:  Share of end-of-year assets ($)  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/ShareOfEOYAssetsAmt 

    UnrltdOrgTxblPrtnrshp_OwnrshpPct = models.DecimalField(null=True, blank=True, max_digits=6, decimal_places=5)
    # Line number: Part VI Column (k)  Description:  Percentage ownership  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/OwnershipPct 

    UnrltdOrgTxblPrtnrshp_LglDmclFrgnCntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part VI Column (c)  Description:  Legal domicile - Foreign Country  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/LegalDomicileForeignCountryCd 

    FrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Line number: Part VI Column (a)  Description:  Postal code  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/ForeignAddress/ForeignPostalCd 

    FrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part VI Column (a)  Description:  Country  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/ForeignAddress/CountryCd 

    FrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Line number: Part VI Column (a)  Description:  City  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/ForeignAddress/CityNm 

    UnrltdOrgTxblPrtnrshp_PrmryActvtsTxt = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part VI Column (b)  Description:  Primary activity  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/PrimaryActivitiesTxt 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Line number: Part VI Column (a)  Description:  Address line 1  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/USAddress/AddressLine1Txt 

    UnrltdOrgTxblPrtnrshp_GnrlOrMngngPrtnrInd = models.CharField(null=True, blank=True, max_length=5)
    # Line number: Part VI Column (j)  Description:  General or managing partner?  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/GeneralOrManagingPartnerInd 

    UnrltdOrgTxblPrtnrshp_PrdmntIncmDsc = models.TextField(null=True, blank=True)
    # Line number: Part VI Column (d)  Description:  Predominate income (related, investment, unrelated)  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/PredominateIncomeDesc 

    BsnssNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Line number: Part VI Column (a)  Description:  Business name line 2  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/BusinessName/BusinessNameLine2Txt 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Line number: Part VI Column (a)  Description:  City  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/USAddress/CityNm 

    UnrltdOrgTxblPrtnrshp_ShrOfTtlIncmAmt = models.BigIntegerField(null=True, blank=True)
    # Line number: Part VI Column (f)  Description:  Share of total income ($)  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/ShareOfTotalIncomeAmt 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Line number: Part VI Column (a)  Description:  State  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/USAddress/StateAbbreviationCd 

    FrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Line number: Part VI Column (a)  Description:  Province or state  most recent xpath: /IRS990ScheduleR/UnrelatedOrgTxblPartnershipGrp/ForeignAddress/ProvinceOrStateNm 

#######
#
# IRS990ScheduleR - SkdRSpplmntlInfrmtnDtl - Part VII contents
# A repeating structure from skedr_part_vii
#
#######

class SkdRSpplmntlInfrmtnDtl(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    ExplntnTxt = models.TextField(null=True, blank=True)
    # Line number: Part VII  Description:  Form, part and line number reference explanation  most recent xpath: /IRS990ScheduleR/SupplementalInformationDetail/ExplanationTxt 

    FrmAndLnRfrncDsc = models.CharField(null=True, blank=True, max_length=100)
    # Line number: Part VII  Description:  Form, part and line number reference  most recent xpath: /IRS990ScheduleR/SupplementalInformationDetail/FormAndLineReferenceDesc 

#######
#
# ReturnHeader990x - ReturnHeader990x Part I Return Header Data 
#
#######

class returnheader990x_part_i(models.Model):
    object_id = models.CharField(max_length=31, blank=True, null=True, help_text="unique xml return id")
    ein = models.CharField(max_length=15, blank=True, null=True, help_text="filer EIN")

    PrprrPrsn_EmlAddrssTxt = models.CharField(null=True, blank=True, max_length=75)
    # Description:  Email address  most recent xpath: /ReturnHeader/PreparerPersonGrp/EmailAddressTxt 

    Flr_BsnssNmCntrlTxt = models.CharField(null=True, blank=True, max_length=7)
    # Description:  Business name control text  most recent xpath: /ReturnHeader/Filer/BusinessNameControlTxt 

    RtrnHdr_TxYr = models.IntegerField(null=True, blank=True)
    # Description: Tax year  most recent xpath: /ReturnHeader/TaxYr 

    FlngScrtyInfrmtn_FdrlOrgnlSbmssnIdDt = models.CharField(null=True, blank=True, max_length=31)
    # Description:  Federal original submission ID date  most recent xpath: /ReturnHeader/FilingSecurityInformation/FederalOriginalSubmissionIdDt 

    PrprrPrsn_FrgnPhnNm = models.TextField(null=True, blank=True)
    # Description:  Telephone number  most recent xpath: /ReturnHeader/PreparerPersonGrp/ForeignPhoneNum 

    FlngScrtyInfrmtn_IPDt = models.CharField(null=True, blank=True, max_length=31)
    # Description:  IP date  most recent xpath: /ReturnHeader/FilingSecurityInformation/IPDt 

    RtrnHdr_DsstrRlfTxt = models.CharField(null=True, blank=True, max_length=100)
    # most recent xpath: /ReturnHeader/DisasterReliefTxt 

    PrcttnrPIN_EFIN = models.CharField(null=True, blank=True, max_length=6)
    # Description:  Electronic Filing Identification Number  most recent xpath: /ReturnHeader/OriginatorGrp/PractitionerPINGrp/EFIN 

    PrprrPrsn_PhnNm = models.CharField(null=True, blank=True, max_length=10)
    # Description:  Telephone number  most recent xpath: /ReturnHeader/PreparerPersonGrp/PhoneNum 

    PrprrUSAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Description:  Address line 2  most recent xpath: /ReturnHeader/PreparerFirmGrp/PreparerUSAddress/AddressLine2Txt 

    USAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Description: State  most recent xpath: /ReturnHeader/Filer/USAddress/StateAbbreviationCd 

    PrprrUSAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Description:  Address line 1  most recent xpath: /ReturnHeader/PreparerFirmGrp/PreparerUSAddress/AddressLine1Txt 

    BsnssNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Description:  Business name line 2  most recent xpath: /ReturnHeader/Filer/BusinessName/BusinessNameLine2Txt 

    RtrnHdr_MltSftwrPckgsUsdInd = models.CharField(null=True, blank=True, max_length=5)
    # Description: Multiple software packages used  most recent xpath: /ReturnHeader/MultSoftwarePackagesUsedInd 

    PrprrFrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Description:  Country  most recent xpath: /ReturnHeader/PreparerFirmGrp/PreparerForeignAddress/CountryCd 

    PrprrPrsn_SlfEmplydInd = models.CharField(null=True, blank=True, max_length=1)
    # Description:  Self-employed?  most recent xpath: /ReturnHeader/PreparerPersonGrp/SelfEmployedInd 

    PrcttnrPIN_PIN = models.CharField(null=True, blank=True, max_length=5)
    # Description:  PIN  most recent xpath: /ReturnHeader/OriginatorGrp/PractitionerPINGrp/PIN 

    PrprrPrsn_SSN = models.CharField(null=True, blank=True, max_length=12)
    # Description:  SSN  most recent xpath: /ReturnHeader/PreparerPersonGrp/SSN 

    Orgntr_OrgntrCd = models.CharField(null=True, blank=True, max_length=15)
    # Description:  Type  most recent xpath: /ReturnHeader/OriginatorGrp/OriginatorTypeCd 

    BsnssNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Description:  Business name line 1  most recent xpath: /ReturnHeader/Filer/BusinessName/BusinessNameLine1Txt 

    USAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Description: City  most recent xpath: /ReturnHeader/Filer/USAddress/CityNm 

    BsnssOffcr_PhnNm = models.CharField(null=True, blank=True, max_length=10)
    # Description:  Telephone number  most recent xpath: /ReturnHeader/BusinessOfficerGrp/PhoneNum 

    FrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Description: Province or state  most recent xpath: /ReturnHeader/Filer/ForeignAddress/ProvinceOrStateNm 

    BsnssOffcr_TxpyrPIN = models.CharField(null=True, blank=True, max_length=5)
    # Description:  Taxpayer PIN  most recent xpath: /ReturnHeader/BusinessOfficerGrp/TaxpayerPIN 

    RtrnHdr_TxPrdBgnDt = models.CharField(null=True, blank=True, max_length=31)
    # Line number: A  Description: Tax period begin date  most recent xpath: /ReturnHeader/TaxPeriodBeginDt 

    Flr_EIN = models.CharField(null=True, blank=True, max_length=9)
    # Description:  EIN  most recent xpath: /ReturnHeader/Filer/EIN 

    Flr_FrgnPhnNm = models.TextField(null=True, blank=True)
    # Description:  Telephone number  most recent xpath: /ReturnHeader/Filer/ForeignPhoneNum 

    USAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Description: Address line 1  most recent xpath: /ReturnHeader/Filer/USAddress/AddressLine1Txt 

    RtrnHdr_RtrnCd = models.TextField(null=True, blank=True)
    # Description: Return type  most recent xpath: /ReturnHeader/ReturnTypeCd 

    USAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Description: Address line 2  most recent xpath: /ReturnHeader/Filer/USAddress/AddressLine2Txt 

    FrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Description: City  most recent xpath: /ReturnHeader/Filer/ForeignAddress/CityNm 

    FlngScrtyInfrmtn_AtSbmssnCrtnDvcId = models.CharField(null=True, blank=True, max_length=40)
    # Description:  Creation device ID  most recent xpath: /ReturnHeader/FilingSecurityInformation/AtSubmissionCreationDeviceId 

    PrprrFrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Description:  Postal code  most recent xpath: /ReturnHeader/PreparerFirmGrp/PreparerForeignAddress/ForeignPostalCd 

    FlngScrtyInfrmtn_FlngLcnsCd = models.TextField(null=True, blank=True)
    # Description:  Filing license type  most recent xpath: /ReturnHeader/FilingSecurityInformation/FilingLicenseTypeCd 

    RtrnHdr_TxPrdEndDt = models.CharField(null=True, blank=True, max_length=31)
    # Line number: A  Description: Tax period end date  most recent xpath: /ReturnHeader/TaxPeriodEndDt 

    PrprrFrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Description:  Address line 2  most recent xpath: /ReturnHeader/PreparerFirmGrp/PreparerForeignAddress/AddressLine2Txt 

    PrprrFrm_PrprrFrmEIN = models.CharField(null=True, blank=True, max_length=9)
    # Description:  EIN  most recent xpath: /ReturnHeader/PreparerFirmGrp/PreparerFirmEIN 

    PrprrFrmNm_BsnssNmLn2Txt = models.CharField(null=True, blank=True, max_length=75)
    # Description:  Business name line 2  most recent xpath: /ReturnHeader/PreparerFirmGrp/PreparerFirmName/BusinessNameLine2Txt 

    RtrnHdr_RtrnTs = models.CharField(null=True, blank=True, max_length=63)
    # Description: The date and time when the return was created  most recent xpath: /ReturnHeader/ReturnTs 

    BsnssOffcr_PrsnTtlTxt = models.CharField(null=True, blank=True, max_length=35)
    # Description:  Title  most recent xpath: /ReturnHeader/BusinessOfficerGrp/PersonTitleTxt 

    RtrnHdr_ISPNm = models.CharField(null=True, blank=True, max_length=6)
    # Description:  ISP  most recent xpath: /ReturnHeader/ISPNum 

    PrprrPrsn_PTIN = models.CharField(null=True, blank=True, max_length=9)
    # Description: Preparer Tax Identification Number  most recent xpath: /ReturnHeader/PreparerPersonGrp/PTIN 

    PrprrFrmNm_BsnssNmLn1Txt = models.CharField(null=True, blank=True, max_length=75)
    # Description:  Business name line 1  most recent xpath: /ReturnHeader/PreparerFirmGrp/PreparerFirmName/BusinessNameLine1Txt 

    PrprrUSAddrss_CtyNm = models.CharField(null=True, blank=True, max_length=22)
    # Description:  City  most recent xpath: /ReturnHeader/PreparerFirmGrp/PreparerUSAddress/CityNm 

    PrprrFrgnAddrss_CtyNm = models.TextField(null=True, blank=True)
    # Description:  City  most recent xpath: /ReturnHeader/PreparerFirmGrp/PreparerForeignAddress/CityNm 

    FlngScrtyInfrmtn_AtSbmssnFlngDvcId = models.CharField(null=True, blank=True, max_length=40)
    # Description:  Filing device ID  most recent xpath: /ReturnHeader/FilingSecurityInformation/AtSubmissionFilingDeviceId 

    PrprrFrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Description:  Address line 1  most recent xpath: /ReturnHeader/PreparerFirmGrp/PreparerForeignAddress/AddressLine1Txt 

    PrprrUSAddrss_SttAbbrvtnCd = models.CharField(null=True, blank=True, max_length=2)
    # Description:  State  most recent xpath: /ReturnHeader/PreparerFirmGrp/PreparerUSAddress/StateAbbreviationCd 

    PrprrPrsn_PrprtnDt = models.CharField(null=True, blank=True, max_length=31)
    # Description:  Preparation date  most recent xpath: /ReturnHeader/PreparerPersonGrp/PreparationDt 

    PrprrFrgnAddrss_PrvncOrSttNm = models.TextField(null=True, blank=True)
    # Description:  Province or state  most recent xpath: /ReturnHeader/PreparerFirmGrp/PreparerForeignAddress/ProvinceOrStateNm 

    FrgnAddrss_AddrssLn1Txt = models.CharField(null=True, blank=True, max_length=35)
    # Description:  Address line 1  most recent xpath: /ReturnHeader/Filer/ForeignAddress/AddressLine1Txt 

    FrgnAddrss_FrgnPstlCd = models.TextField(null=True, blank=True)
    # Description: Postal code  most recent xpath: /ReturnHeader/Filer/ForeignAddress/ForeignPostalCd 

    PrprrPrsn_PrprrPrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Description:  Name - Person  most recent xpath: /ReturnHeader/PreparerPersonGrp/PreparerPersonNm 

    Orgntr_EFIN = models.CharField(null=True, blank=True, max_length=6)
    # Description:  EFIN  most recent xpath: /ReturnHeader/OriginatorGrp/EFIN 

    Flr_InCrOfNm = models.CharField(null=True, blank=True, max_length=35)
    # Description:  In care of name  most recent xpath: /ReturnHeader/Filer/InCareOfNm 

    RtrnHdr_SftwrVrsnNm = models.CharField(null=True, blank=True, max_length=20)
    # Description: Software version number  most recent xpath: /ReturnHeader/SoftwareVersionNum 

    IPAddrss_IPv4AddrssTxt = models.CharField(null=True, blank=True, max_length=31)
    # Description:  IP address  most recent xpath: /ReturnHeader/FilingSecurityInformation/IPAddress/IPv4AddressTxt 

    FlngScrtyInfrmtn_IPTmznCd = models.CharField(null=True, blank=True, max_length=31)
    # Description:  IP timezone  most recent xpath: /ReturnHeader/FilingSecurityInformation/IPTimezoneCd 

    RtrnHdr_SgntrOptnCd = models.TextField(null=True, blank=True)
    # Description: Signature Option  most recent xpath: /ReturnHeader/SignatureOptionCd 

    PrprrUSAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Description:  ZIP code  most recent xpath: /ReturnHeader/PreparerFirmGrp/PreparerUSAddress/ZIPCd 

    BsnssOffcr_FrgnPhnNm = models.TextField(null=True, blank=True)
    # Description:  Telephone number  most recent xpath: /ReturnHeader/BusinessOfficerGrp/ForeignPhoneNum 

    FlngScrtyInfrmtn_IPTm = models.CharField(null=True, blank=True, max_length=15)
    # Description:  IP time  most recent xpath: /ReturnHeader/FilingSecurityInformation/IPTm 

    USAddrss_ZIPCd = models.CharField(null=True, blank=True, max_length=15)
    # Description: ZIP code  most recent xpath: /ReturnHeader/Filer/USAddress/ZIPCd 

    BsnssOffcr_EmlAddrssTxt = models.CharField(null=True, blank=True, max_length=75)
    # Description:  Email address  most recent xpath: /ReturnHeader/BusinessOfficerGrp/EmailAddressTxt 

    BsnssOffcr_PrsnNm = models.CharField(null=True, blank=True, max_length=35)
    # Description:  Name  most recent xpath: /ReturnHeader/BusinessOfficerGrp/PersonNm 

    RtrnHdr_PINEntrdByCd = models.TextField(null=True, blank=True)
    # Description: PIN Entered By  most recent xpath: /ReturnHeader/PINEnteredByCd 

    IPAddrss_IPv6AddrssTxt = models.CharField(null=True, blank=True, max_length=31)
    # Description:  IP address  most recent xpath: /ReturnHeader/FilingSecurityInformation/IPAddress/IPv6AddressTxt 

    FrgnAddrss_AddrssLn2Txt = models.CharField(null=True, blank=True, max_length=35)
    # Description:  Address line 2  most recent xpath: /ReturnHeader/Filer/ForeignAddress/AddressLine2Txt 

    Flr_PhnNm = models.CharField(null=True, blank=True, max_length=10)
    # Description:  Telephone number  most recent xpath: /ReturnHeader/Filer/PhoneNum 

    RtrnHdr_SftwrId = models.CharField(null=True, blank=True, max_length=8)
    # Description: Software ID  most recent xpath: /ReturnHeader/SoftwareId 

    FlngScrtyInfrmtn_FdrlOrgnlSbmssnId = models.TextField(null=True, blank=True)
    # Description:  Federal original submission ID  most recent xpath: /ReturnHeader/FilingSecurityInformation/FederalOriginalSubmissionId 

    BsnssOffcr_SgntrDt = models.CharField(null=True, blank=True, max_length=31)
    # Description:  Signature date  most recent xpath: /ReturnHeader/BusinessOfficerGrp/SignatureDt 

    FrgnAddrss_CntryCd = models.CharField(null=True, blank=True, max_length=2)
    # Description: Country  most recent xpath: /ReturnHeader/Filer/ForeignAddress/CountryCd 

    BsnssOffcr_DscssWthPdPrprrInd = models.CharField(null=True, blank=True, max_length=5)
    # Description: May the IRS discuss this return with the preparer shown above?  most recent xpath: /ReturnHeader/BusinessOfficerGrp/DiscussWithPaidPreparerInd 
