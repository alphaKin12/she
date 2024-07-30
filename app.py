import streamlit as st
from PIL import Image
# Define functions for each page
def first_page():
    st.title("Holy day, thank you for being the biggest blessing. 01/08/2023")
    
    # Corrected image URL
    image_url = "https://drive.google.com/uc?export=view&id=1FBQb0dAUPUBHgYSTLc8DHvE8g48LZnHd"
    
    # Display the image
    st.image(image_url, use_column_width=True)
    
    # Display the text
    st.write("""
    ### Shinjini and Anurag <3
    **The start of us**

    From what was just an instant connection between the headboy and the prefect, we have come a long way. 
    From asking you if everything was alright in class IV, to asking you if everything was alright at home... 
    a bond strong enough for a lifetime was formed.

    I take a moment to thank you for bearing with me. I am not the easiest guy. I am grateful I have you. 
    I am grateful I have a girl with whom even a day of fights is nothing short of an anniversary. 
    And with whom, every single day is a summer in the hills or a winter by the beach. Relaxing, soothing, 
    comforting, a feeling worth letting go the world for. The feeling of true love, as rare as it is, 
    is basically an umbrella word for so many feelings together. Companionship, friendship, partnership, 
    a guide, a soul to look up to and so much more :).
    """)

    # Add the surprise button
    if st.button("Surprise"):
        st.write("[Click here to see the surprise!](#upload link here)")


def second_page():
    st.title("Shinjini")

    # Create a list of sections
    sections = [
        ("S - Surreality", "For what I have learnt and realised about you and from what I have learnt about myself, finding you has been more about rediscovering myself. It has been about growing up. It has been about believing in myself and being like fuck the world, this woman makes me believe that I can reach for the moon. Can I in reality? most likely no. But this spirit, the rush at the thought of it. This is surreal. The idea that a girl and a boy can be so much in love and yet hold each other together like a newborn that hangs onto his mother. You are dreamlike. You are my dream come true. Just that you know shinu...mujhe sab mil jata hai. Jo jo main chahta hoon...God just makes me work for it. Once I do, he ensures I get it. The distance between us is that test of time. What lies ahead is a beautiful time. A paradise. Where our souls will live in peace together whether it be a single room apartment, or an entire mansion, it will be all of us :)\n\nMy life, my darling, my sweetheart, the apple of my eyes, I love you, I don't cherish anything as much :)"),
        ("H - Happiness", "My girl. The sense of your name is nothing short of happiness to me. One idiot understands the other. One dumb guy who melts in most situations is well understood by this girl who is quick to remind him of the good in the world. And how every situation is treatable positively, without anger, without frustration and most importantly, without CURSING. The first time in life when I have realised that even the sight of someone can bring joy to your heart. The mere voice coming out of someone's throat is enough to bring a wide smile to one's face especially after a day full of suffering and unlucky events. When things go wrong, I see your photographs to console myself and remind myself of how many things i have to look forward to. If this is not happiness, what is, shinu? Life happens. World goes down. I still have this bubbly face to look at whenever I want to. My capsule of happiness, thank you for existing for your idiot."),
        ("I - Indebted", "I am deeply indebted to God for you, for your family, and for everything that you bring with yourself. Every day, I find myself in awe of the love and joy you bring into my life. You are my confidant, my muse, and the light that guides me through the darkest of times.\n\n'My bounty is as boundless as the sea, My love as deep; the more I give to thee, The more I have, for both are infinite.' — William Shakespeare\n\nThese words from Shakespeare perfectly capture the infinite depth of my love for you. Just as the sea is boundless, so too is my gratitude for having you by my side. You are my everything, and I am eternally thankful to God for blessing me with your presence.\n\n'When I saw you I fell in love, and you smiled because you knew.' — William Shakespeare\n\nFrom the moment our paths crossed, I knew you were the one I had been searching for. Your smile, your laughter, and your loving presence have made every day a precious gift. I am forever grateful to God for bringing you into my life.\n\nAs we celebrate our anniversary, I want you to know how deeply I cherish you. You are my past, my present, and my future. Together, we have built a love that is strong and enduring, and I look forward to all the adventures that await us. Thank you for loving me. I have nothing but eyes filled with happy tears as I write all this today.\n\nWith all my love and gratitude,\n\nAadi."),
        ("N - Nympholepsy", "The word means excessive longingness or very high sexual attraction. Could this ever not be in the series of things that I feel for you? Never. My heart pounds, I have goosebumps on my arms everytime I touch you. The urge to bury my face in between your chest is a never dying feeling. The desire to insert myself into your world of warmth and love with fluids like water is heavenly. You happen to have the best body shinu. Your insecurities bug me. I would not change a thing about you. I mean it when I say it. You have a little fat around your tummy? No worries. That is a place I can pinch you and runaway. You have bigger breasts than most around, and that sag down? No worries. Our babies will love them.(Just as much as their dad craves the same :3). You have body hair that makes you feel weird in public? Why worry for something that grows normally out of your body? It isn't so much that it makes you look bad. I like them. They're homely. Makes my wife feel more of a normal human being than an artifical creature. You have intense acne? You still look way too good for a girl. I will love you enough to ensure that you have the best glow. Less worries your plate will mean more clear the skin hai na?\n\nDying. Dying. Dying to make love to you. Miss you shinu."),
        ("J - Juno", "My dearest, you embody the grace and majesty of Juno, the queen of the gods. As Virgil wrote in the Aeneid, Juno is 'regina deum' (queen of the gods), and to me, you are the queen of my heart.\n\nIn the words of William Shakespeare, 'She walks in beauty, like the night / Of cloudless climes and starry skies' (Byron). Your beauty, both inside and out, is timeless and enchanting, much like the goddess Juno's enduring influence.\n\nYour presence in my life is nothing short of divine, a blessing that I cherish every day. As the poet John Keats once said, 'A thing of beauty is a joy forever,' and your love has been an everlasting source of joy and strength for me.\n\nIn the mythology, Juno is not only a protector but also a symbol of marital harmony and fidelity. Just as Juno stood by Jupiter, you have stood by me, a steadfast partner in every sense. As Homer wrote in the Iliad, 'There is nothing alive more agonized than man of all that breathe and crawl across the earth,' yet with you by my side, I feel invincible, able to face any challenge.\n\nYour wisdom, kindness, and strength are unparalleled. Much like Juno, who was known for her counsel and support, you are my guide and my rock. The poet Robert Browning once said, 'Grow old along with me! The best is yet to be,' and with you, I believe in a future filled with endless possibilities and unending love."),
        ("I - Insula", "My dearest love,\n\nYou are my insula, my home, my sanctuary. Just as an insula stands as a place of refuge and comfort, you are the center of my world, where my heart finds peace and belonging.\n\nMy love for you knows no bounds, and it grows with each passing day. You have become my insula, a place where my soul finds rest and my heart feels at home.\n\nShakespeare also wrote, 'I wish you all the joy that you can wish' (The Merchant of Venice). My joy is complete in your presence, and my greatest wish is to always be by your side, to cherish and love you as you deserve.\n\n'You are my heaven on earth' (Othello), my insula where every moment is filled with the warmth of your love and the comfort of your embrace. With you, I have found my true home, and I am endlessly grateful for the blessing that you are in my life.\n\nAs Shakespeare beautifully penned, 'From the moment we met, I knew you were my insula, the place where I belong.' Your love has transformed my world, filling it with light and love beyond measure.\n\nYou are my insula, my home, my love, my everything.\n\nForever yours dearie...\n\nAadi."),
        ("N - Naive", "Your innocence and naivety are among the many things I adore about you. They paint you with a purity that is rare and beautiful in this world. Your heart, untouched by the cynicism of life, remains a beacon of light, guiding me with its gentle glow.\n\nYou have made silly decisions, as we all do, but it is in those moments that your true beauty shines through. Your willingness to learn, to grow, and to submit yourself to me, your Aadi, is a testament to your trust and love. As Shakespeare once wrote, 'Love looks not with the eyes, but with the mind, and therefore is winged Cupid painted blind' (A Midsummer Night's Dream). Your love, unseeing and unassuming, is the truest form of affection.\n\nI love you more than words can ever express. My heart aches with longing for you, and my soul craves your presence. 'Hear my soul speak: The very instant that I saw you, did my heart fly to your service' (The Tempest). From the moment our paths crossed, my heart knew it belonged to you, and I have been devoted to you ever since.\n\nI would cross the seas, scale the highest mountains, and traverse the widestand traverse the widest deserts just to be with you. As Shakespeare beautifully penned, 'The course of true love never did run smooth' (A Midsummer Night's Dream), but I am willing to face any obstacle, endure any hardship, to be by your side.Your naivety, your innocence, your silly decisions—they all make you the extraordinary person I have fallen deeply in love with. You are my muse, my insula, my Juno, and my heart's true desire.The world's definitely a harsh place. But will it be any sort of a paradise with you? Nope.With all my love,Aadi"),
        ("I - Idol"," You have been my goddess, my Juno, ever since you entered my life. Your presence has illuminated my world, and through you, I have learned the most profound and important lessons in life.In your eyes, I have discovered the true meaning of love and devotion. You have shown me that love is not just a feeling, but a commitment, a journey we embark on together. Your unwavering support and boundless affection have taught me the value of loyalty and partnership. As Shakespeare said, 'Love is not love which alters when it alteration finds, or bends with the remover to remove: O no! it is an ever-fixed mark that looks on tempests and is never shaken' (Sonnet 116). Your love has been that ever-fixed mark in my life, guiding me through every storm.Through your innocence and naivety, I have learned the beauty of seeing the world with fresh eyes, of embracing life with an open heart. You have reminded me that it is okay to make mistakes, to stumble and fall, as long as we rise again and learn from our experiences. Your gentle spirit has shown me the importance of kindness and compassion.Your silly decisions, your laughter, and your tears have all been part of our shared journey. They have taught me patience and understanding, and through them, I have come to appreciate the depth of our connection. Shakespeare once wrote, 'My heart is ever at your service' (Timon of Athens). My heart is indeed at your service, ready to support you in every way, just as you have supported me.Through your love, I have learned the most important lesson of all: that true happiness comes from sharing our lives with someone who truly understands and accepts us. You have been my guide, my teacher, and my inspiration. You are my goddess, my Juno, and I am forever grateful for the lessons you have imparted to me.\n With all my love,\nAadi.") 
          ]
          
    for title, content in sections:
        with st.expander(title, expanded=False):
            st.write(content)

def page_three():
    st.title("Lessons I've Learned From You")

    st.write(
        """
        My dearest Shinu,

        Over the time we've spent together, I've learned so many invaluable lessons from you. Here are some of the most cherished lessons that have profoundly impacted my life, when I say this, i truly mean the word profound. I was this sweet know it all arrogant guy who cared little about stuff around:
        """
    )

    # Define lessons with optional icons or images
    lessons = [
        {"title": "Gratefulness", "description": "You've taught me to find joy in the simple things and to appreciate the small moments in life.You have taught me what it means to love and to be loved. You have given me endless moments to cherish. You have told me how everything has something good to it. And how consideration and a little patience kind of sorts everything out. You aren't perfect in those yourself but you still ensure je Aadi know. Thank you Shinu :)"},
        {"title": "Family comes first", "description": "I did. I still do today a little maybe, but I genuinely have started valuing people with me so so much more.Knowingly, unknowingly you have taught me the way to work to keep my relationships and friendships healthy and safe. You have taught me how everything needs efforts. This is maybe the biggest change Anurag Thakur has undergone in the last one year, credits, his beautiful girl."},
        {"title": "To be more understanding", "description": "To understand people in situations before reacting. I am in general quite short tempered. You brought in peace. You brought in calm. Taught me how to not judge people as much. To be more considerate. In the process, I have become a much understanding lover, maybe shinu? "},
        {"title": "Leap of faith is all it takes", "description": "I have been a guy with trust issues(ektu). The amount of trust you put in me makes me believe in the good things of the world. How true love sees no logic. Believes in nothing but the good and how trusting someone despite what society says is still the best deal. You have taken that leap of faith to be with your Aadi despite him being a 1000 km away, ain't it jaanu? Thank you for this too, once again. I will be grateful to you 4ever."}
    ]

    # Create columns for lessons
    num_columns = 2
    cols = st.columns(num_columns)

    # Display lessons in boxes
    for i, lesson in enumerate(lessons):
        with cols[i % num_columns]:
            st.markdown(f"""
            <div style="background-color: #f0f8ff; padding: 20px; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); margin-bottom: 20px;">
                <h4 style="color: #333; font-family: Arial, sans-serif;">{lesson['title']}</h4>
                <p style="color: #555; font-family: Arial, sans-serif;">{lesson['description']}</p>
            </div>
            """, unsafe_allow_html=True)
        
    # Optional: Add an image or illustration
    image_url = "https://imgs.search.brave.com/XEc57uIwXAq4fWBOjlHTKFs36F7JrRIbXxNoHv85wMM/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9pbWcu/YS50cmFuc2Zlcm1h/cmt0LnRlY2hub2xv/Z3kvcG9ydHJhaXQv/YmlnLzgxOTgtMTY5/NDYwOTY3MC5qcGc_/bG09MQ"
    
    try:
        st.image(image_url, caption="Together we learn and grow", use_column_width=True)
    except Exception as e:
        st.write(f"Image could not be loaded: {e}")


    # Conclusion
    st.write(
        """
        Each of these lessons has enriched my life in countless ways. Thank you for being my guide, my inspiration, and my greatest teacher. I look forward to continuing this journey with you and learning even more together.

        With all my love,
        Aadi
        """
    )
# Page navigation
page = st.sidebar.selectbox("Choose a page", ["Home", "Second Page","Third Page"])
if page == "Home":
    first_page()
elif page == "Second Page":
    second_page()
elif page=="Third Page":
    page_three()
    
