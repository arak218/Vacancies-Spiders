from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from zorgned_project.spiders import activite, adhd, altrecht, amsta, arlijne, aza_bijtzorg, bethelzorg
from zorgned_project.spiders import breedonk, burgemeester_zorgplein, buurtzorgt, carintreg, cederhof, coloriet
from zorgned_project.spiders import de_vijverhof, dsv, edt_maastricht, empathon, eykenburg, ggz_centraal
from zorgned_project.spiders import ggz_friesland, gkracht, havenpol, het_zand, isala, kalorama, kk_l
from zorgned_project.spiders import laprovidence, libertas, liemerije, lyvore, maasduinen, marente, meander
from zorgned_project.spiders import mmc, molendrift, ouderenzorg_annenborch, ouderenzorgzitinje, perspectief
from zorgned_project.spiders import raffyzorg, sensire, skb, st_antonius, stichtingniko, sutfene, talma, tsn, vumc
from zorgned_project.spiders import woonzorgbcm, zorgcentradebetuwe, zorgcirkel, zorggroeptellus, zorgstroom, nncz
settings = get_project_settings()

process = CrawlerProcess(settings=settings)
process.crawl(activite.FirstSpider)
process.crawl(adhd.SecondSpider)
process.crawl(altrecht.ThirdSpider)
process.crawl(amsta.FourthSpider)
process.crawl(arlijne.FifthSpider)
process.crawl(aza_bijtzorg.SixthSpider)
process.crawl(bethelzorg.SeventhSpider)
process.crawl(breedonk.EighthSpider)
process.crawl(burgemeester_zorgplein.NinthSpider)
process.crawl(buurtzorgt.TenthSpider)
process.crawl(carintreg.EleventhSpider)
process.crawl(cederhof.TwelfthSpider)
process.crawl(coloriet.ThirteenthSpider)
process.crawl(de_vijverhof.FourteenthSpider)
process.crawl(dsv.FifteenthSpider)
process.crawl(edt_maastricht.SixteenthSpider)
process.crawl(empathon.SeventeenthSpider)
process.crawl(eykenburg.EigteenthSpider)
process.crawl(ggz_centraal.NinteenthSpider)
process.crawl(ggz_friesland.TwentiethSpider)
process.crawl(gkracht.TwentyfirstSpider)
process.crawl(havenpol.TwentysecondSpider)
process.crawl(het_zand.TwentyThirdSpider)
process.crawl(isala.TwentyFourthSpider)
process.crawl(kalorama.TwentyFifthSpider)
process.crawl(kk_l.TwentySixthSpider)
process.crawl(laprovidence.TwentySeventhSpider)
process.crawl(libertas.TwentyEighthSpider)
process.crawl(liemerije.TwentyNinthSpider)
process.crawl(lyvore.ThirtythSpider)
process.crawl(maasduinen.ThirtyFirstSpider)
process.crawl(marente.ThirtySecondSpider)
process.crawl(meander.ThirtyThirdSpider)
process.crawl(mmc.ThirtyFourthSpider)
process.crawl(molendrift.ThirtyFifthSpider)
process.crawl(ouderenzorg_annenborch.ThirtySixthSpider)
process.crawl(ouderenzorgzitinje.ThirtySeventhSpider)
process.crawl(perspectief.ThirtyEigthSpider)
process.crawl(raffyzorg.ThirtyNinthSpider)
process.crawl(sensire.FortiethSpider)
process.crawl(skb.FortyFirstSpider)
process.crawl(st_antonius.FortySecondSpider)
process.crawl(stichtingniko.FortyThirdSpider)
process.crawl(sutfene.FortyFourthSpider)
process.crawl(talma.FortyFifthSpider)
process.crawl(tsn.FortySixthSpider)
process.crawl(vumc.FortySeventhSpider)
process.crawl(woonzorgbcm.FortyEighthSpider)
process.crawl(zorgcentradebetuwe.FortyNinthSpider)
process.crawl(zorgcirkel.FiftiethSpider)
process.crawl(zorggroeptellus.FiftyfirstSpider)
process.crawl(zorgstroom.FiftySecondSpider)
process.crawl(nncz.FiftyThirdSpider)
process.start()


