# REF: README.md
# For individual sentences
from nltk.translate.bleu_score import sentence_bleu
# For whole paragraphs/texts
from nltk.translate.bleu_score import corpus_bleu
from nltk.tokenize import sent_tokenize
from nltk.translate.bleu_score import SmoothingFunction

'''
Compare 2 Wikipedia articles to find sentences present in one but not the other
'''
def compare(ref, hypothesis, similarity=0.1):
    # Tokenize paragraphs so they can be traversed as an array
    ref_list = sent_tokenize(ref)
    hyp_list = sent_tokenize(hypothesis)

    no_pairs = []
    pairs = []

    # Itteration over both paragraphs
    for ref in ref_list:
        for hyp in hyp_list:
            #Determine if the current sentence has a match or not
            if sentence_bleu([ref.split()], hyp.split(), smoothing_function=SmoothingFunction().method7) >= similarity:
                # Check for duplicates
                if ref not in pairs:
                    pairs.append(ref)
                # Check to see if sentence was determined to have no pair in previous itteration
                if ref in no_pairs:
                    no_pairs.remove(ref)   
            else:
                # If the setence hasn't been added to either array yet
                if ref not in no_pairs and ref not in pairs:
                    no_pairs.append(ref)
    # Print results
    print("--Similar sentences--")
    for pair in pairs:
        print(pair)
    print("")
    print("--Different sentences--")
    for single in no_pairs:
        print(single)






ref_par = "The Beatles were an English rock band, formed in Liverpool in 1960, that comprised John Lennon, Paul McCartney, George Harrison and Ringo Starr. They are regarded as the most influential band of all time and were integral to the development of 1960s counterculture and popular music's recognition as an art form. Rooted in skiffle, beat and 1950s rock 'n' roll, their sound incorporated elements of classical music and traditional pop in innovative ways; the band later explored music styles ranging from ballads and Indian music to psychedelia and hard rock. As pioneers in recording, songwriting and artistic presentation, the Beatles revolutionised many aspects of the music industry and were often publicised as leaders of the era's youth and sociocultural movements. Led by primary songwriters Lennon and McCartney, the Beatles evolved from Lennon's previous group, the Quarrymen, and built their reputation playing clubs in Liverpool and Hamburg over three years from 1960, initially with Stuart Sutcliffe playing bass. The core trio of Lennon, McCartney and Harrison, together since 1958, went through a succession of drummers, including Pete Best, before asking Starr to join them in 1962. Manager Brian Epstein moulded them into a professional act, and producer George Martin guided and developed their recordings, greatly expanding their domestic success after signing to EMI Records and achieving their first hit, 'Love Me Do', in late 1962. As their popularity grew into the intense fan frenzy dubbed 'Beatlemania', the band acquired the nickname 'the Fab Four', with Epstein, Martin and other members of the band's entourage sometimes given the informal title of 'fifth Beatle'. By early 1964, the Beatles were international stars and had achieved unprecedented levels of critical and commercial success. They became a leading force in Britain's cultural resurgence, ushering in the British Invasion of the United States pop market, and soon made their film debut with A Hard Day's Night (1964). A growing desire to refine their studio efforts, coupled with the untenable nature of their concert tours, led to the band's retirement from live performances in 1966. At this time, they produced records of greater sophistication, including the albums Rubber Soul (1965), Revolver (1966) and Sgt. Pepper's Lonely Hearts Club Band (1967), and enjoyed further commercial success with The Beatles (also known as 'the White Album', 1968) and Abbey Road (1969). Heralding the album era, their success elevated the album to be the dominant form of record consumption over singles; they also inspired a greater public interest in psychedelic drugs and Eastern spirituality, and furthered advancements in electronic music, album art and music videos. In 1968, they founded Apple Corps, a multi-armed multimedia corporation that continues to oversee projects related to the band's legacy. After the group's break-up in 1970, all principal members enjoyed success as solo artists and some partial reunions have occurred. Lennon was murdered in 1980 and Harrison died of lung cancer in 2001. McCartney and Starr remain musically active. The Beatles are the best-selling music act of all time, with estimated sales of 600 million units worldwide. They hold the record for most number-one albums on the UK Albums Chart (15), most number-one hits on the Billboard Hot 100 chart (20), and most singles sold in the UK (21.9 million). The band received many accolades, including seven Grammy Awards, four Brit Awards, an Academy Award (for Best Original Song Score for the 1970 documentary film Let It Be) and fifteen Ivor Novello Awards. They were inducted into the Rock and Roll Hall of Fame in 1988, and each principal member was inducted individually between 1994 and 2015. In 2004 and 2011, the group topped Rolling Stone's lists of the greatest artists in history. Time magazine named them among the 20th century's 100 most important people."
hyp_par = "The Beatles, also known in the Hispanic world as the Beatles, was a British rock band formed in Liverpool during the 1960s, being integrated from 1962 to its separation in 1970 by John Lennon, Paul McCartney, George Harrison and Ringo Starr. It is widely considered the most influential band of all time, being instrumental in the development of the countercultural movement of the 1960s and the recognition of popular music as an art form. Rooted in skiffle, beat music, and 1950s rock and roll, their sound would often incorporate elements of classical and traditional pop music, among others, in innovative ways in their songs; the band would later go on to work with a wide range of musical styles, ranging from ballads and Indian music, to psychedelia and hard rock. As pioneers in the forms of recording, composition and artistic presentation; The nature of his enormous popularity, which had first emerged with the 'Beatlemania' craze, transformed as his compositions became more sophisticated, revolutionizing various aspects of the music industry and coming to be perceived as embodying the ideals of Beatlemania. progressives of the youth of the time and their social and cultural movements. Led by the Lennon-McCartney duo, they would build their reputation in the Liverpool and Hamburg underground scenes over a three-year period beginning in 1960, initially with Stuart Sutcliffe on bass. The core trio of Lennon, McCartney and Harrison, together since 1958 as part of The Quarry Men, would play alongside multiple drummers (including Pete Best) before asking Richard Starkey, better known as Ringo Starr, to join them in 1962. Established As a professional group after being offered management by Brian Epstein, and with their musical potential enhanced by the creativity of producer George Martin, they would achieve commercial success in the UK in late 1962 with their first single, 'Love Me Do'. ». From there, they would acquire international popularity over the following years, in which they would tour extensively until 1966, the year in which they ceased live activity to dedicate themselves solely to recording in the studio until their official dissolution. in 1970. Afterwards, all of its members embarked on successful independent careers of varying lengths. Lennon would be assassinated, by Mark David Chapman, outside his New York home in 1980, and Harrison would die of cancer in 2001. McCartney and Starr, the two surviving members, are still musically active. During their years of study they created some of their best material, including the album Sgt. Pepper's Lonely Hearts Club Band (1967), considered by experts to be a masterpiece. Five decades after their split, the music they created continues to be popular. They remain the group with the most number ones on the British charts, placing more albums in this position than any other musical group. According to RIAA certifications, they have sold more albums in the United States than any other artist. They were awarded seven Grammy Awards, and received a total of fifteen Ivor Novello Awards from the British Academy of Songwriters, Composers and Authors. In 2004, Rolling Stone magazine ranked them number one on its list of the '100 greatest artists of all time'. According to the same publication, the innovative music of The Beatles and their impact helped define both popular culture and counterculture. In 2010, the channel Music specialist television firm VH1 ranked them at number one on its list of the '100 Greatest Artists of All Time'. 'The Top 1000 Artists of All Time'. They also appear in the first position as the greatest artists of all time on the Hot 100 and Billboard 200 lists in the 2015 Billboard ranking."
compare(ref_par, hyp_par)