from django.shortcuts import render
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Bidirectional, LSTM, Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.sequence import pad_sequences

from django.shortcuts import render, redirect


def input_page(request):
    if request.method == 'POST':
        number = int(request.POST['number'])
        number1 = int(request.POST['number1'])
        number2 = int(request.POST['number2'])
        text = request.POST['text']
        square = number ** 2


        # Machine Learning Code
        if number2==1:
            text1='''
            Vignan is the trust of 1 lakh student many will think in such way.Chairperson name
            is Lavu Rathaiah and many are working under vignan college
            many faculties including hod's work under vignan college.many students study in vignan for
            good education and good future goals many parents believe vignan institute of
            technology and science as one of the best college in telangana state vignan intitute
            of technology and sciece collge also performs very well in study to get good
            It will satisfy all students in terms of academics and studies
            VGNT is an exemplary institution of higher learning with a mission of pursuing excellence in education and research. The institution, with its diverse and dynamic community of about 2500 students offers a distinctive combination of some of the finest facilities for MCA, MBA and M.Tech. with 5 different graduate and undergraduate programs CIVIL, MECH, EEE, ECE, CSE, CSE(AI & ML, CSE(Data Science), IT, EIE accomplished faculty, world-class facilities with hostel set on a sprawling 350 acres of sylvan surroundings of valleys and watersheds, mango groves and greenery.
            While students at VGNT immerse themselves in academics, the college has a lot in store for them outside the classroom. Student life includes participation in sports, recreational & co-curricular and cultural activities. In short, at VGNT, students will find an academic and social environment where everyone from faculty members to peers helps them shape their future.
            VGNT is home to aesthetically designed buildings with its state-of-the-art computer and internet facilities, modern laboratories, workshops, seminar halls, auditoriums and well-stocked libraries, sports and games fields.
            The Institution boasts of a strong alumni network with alumni events held every year serving as a platform for past students to give back to VGNT and share their experiences with its present fellow students.
            With so much to offer, it is only natural that students of VGNT get a unique opportunity to carve a niche for themselves in their chosen field of study that enables them to become well-rounded and discerning citizens, fully qualified for their chosen professions in the workplace.
            To evolve into a center of excellence in Science & Technology through creative and innovative practices in teaching-learning, promoting academic achievement & research excellence to produce internationally accepted competitive and world class professionals who are psychologically strong and emotionally balanced imbued with social consciousness and ethical values.
            To provide high quality academic programmes, training activities, research facilities and opportunities supported by continuous industry – institute interaction aimed at employability, entrepreneurship, leadership and research aptitude among students and contribute to the economic and technological development of the region, state and nation.
            Well Thought-out Reforms In Technical Education Is The Need Of The Hour We, in India today, are living in a transitional era. On one hand, we are swamped by the global financial meltdown while on the other; we are witnessing a slow but sure revival of the manufacturing and agricultural sectors.
            Vignan, a trusted name for quality education in Andhra Pradesh, has always been figuring among the top due to its commitment to student centric initiatives through out its existence of more than three decades even in the unprecedented proliferation of professional institutions in AP during the last decade.
            Vignan with its inherent capability to capture the pulse of youth has grasped their aspirations, speed and intellectual capabilities and tuned its curriculum to fulfill their needs.
            Vignan provides world class training in transferring subject knowledge, communication and team working skills in learning centered fashion and enables its students to face the global arena with confidence.
            With its excellent infrastructure, committed and qualified faculty, strong teaching-learning processes and more importantly a meticulously designed student counseling system, Vignan is indeed the right choice to pursue engineering education and secure placements in top notch companies or admissions in reputed international universities for higher studies..Besides academics, at Vignan, we strive for the integrated development of the students through several internal student professional bodies designed to bring out the best from them.
            '''



        elif number2==2:
            text1='''Once upon a time in the ancient city of Ayodhya, there lived a noble king named Dasharatha. He had a son named Rama, who was loved by everyone for his kind heart and strong principles. Rama was known for his righteousness and bravery.
As Rama grew older, the time came for him to marry. King Dasharatha decided to hold a grand ceremony called a swayamvara, where princesses from different kingdoms would compete to marry Rama. Among the princesses was Sita, the daughter of King Janaka.
During the swayamvara, Rama displayed his strength and skill by breaking Lord Shiva's bow, a feat no one else could accomplish. Sita, impressed by Rama's bravery, garlanded him, choosing him as her husband.
However, their happiness was short-lived. Dasharatha's second wife, Kaikeyi, was manipulated by her maid Manthara into demanding that Rama be banished from Ayodhya for fourteen years, and that her own son Bharata be crowned instead.
Despite protests from Dasharatha and Rama's mother, Queen Kausalya, Rama chose to honor his father's word and willingly left Ayodhya along with his devoted wife Sita and loyal brother Lakshmana.
During their exile in the forest, tragedy struck when the demon king Ravana kidnapped Sita and took her to his kingdom of Lanka. Rama and Lakshmana, aided by the monkey warrior Hanuman and an army of monkeys, embarked on a perilous journey to rescue her.
After many trials and battles, Rama defeated Ravana and rescued Sita. However, their troubles were far from over. Doubts about Sita's chastity arose among the people of Ayodhya, and to prove her purity, she underwent a trial by fire, emerging unscathed and vindicated.
Despite Sita's innocence, Rama, bound by his duty as a king, reluctantly exiled her to the forest. Heartbroken, Sita chose to return to the earth from where she had come, leaving behind her twin sons, Lava and Kusha, whom she had borne during her exile.
Rama ruled Ayodhya for many years with wisdom and justice, but his heart never truly healed from the loss of Sita. Eventually, when his time on earth came to an end, he returned to the divine realm, leaving behind a legacy of righteousness and devotion that would be remembered for generations to come.'''

        elif number2==3:
            text1='''The Mahabharata is an ancient Indian epic that tells the story of the great Kurukshetra War and the events leading up to it. It is a tale of family, honor, duty, and the eternal battle between righteousness and evil. Here's a summary of the Mahabharata story:
            The story begins with the kingdom of Hastinapura, ruled by King Shantanu. He falls in love with and marries the beautiful Ganga, who later reveals herself to be the goddess of the river. They have a son named Devavrata, who becomes known as Bhishma.
            As the story unfolds, Bhishma takes a vow of celibacy to ensure the stability of the kingdom. Over time, the throne passes to King Shantanu's son, Vichitravirya. However, Vichitravirya dies without an heir, leaving behind two widows, Ambika and Ambalika.
            To continue the royal lineage, Bhishma seeks a suitable husband for the widows. He arranges for a practice called Niyoga, where a sage named Vyasa fathers children with Ambika and Ambalika. Ambika gives birth to Dhritarashtra, who is blind, and Ambalika gives birth to Pandu, who is cursed to be unable to father children.
            Dhritarashtra becomes the king of Hastinapura, but due to his blindness, his younger brother, Pandu, rules as regent. Pandu marries Kunti and Madri. Kunti possesses a divine boon that allows her to summon gods and bear their children. With this boon, she gives birth to Yudhishthira, Bhima, and Arjuna. Madri, on the other hand, seeks Kunti's help and has twin sons, Nakula and Sahadeva, with the Ashwini Kumaras, the divine physicians.
            The five Pandava brothers grow up under the guidance of their uncle, Bhishma, and their mother, Kunti. They receive education and training in various arts and weaponry, becoming skilled warriors.
            Meanwhile, Dhritarashtra's hundred sons, known as the Kauravas, including Duryodhana, Dushasana, and Shakuni, grow jealous of the Pandavas' popularity and their claim to the throne. The Kauravas conspire against the Pandavas, leading to a series of events that ultimately result in the infamous game of dice.
            In the game of dice, the cunning Shakuni manipulates Yudhishthira into gambling away his kingdom, wealth, and even his brothers and wife, Draupadi. As a result, the Pandavas are exiled to the forest for thirteen years, including one year of incognito exile.
            During their exile, the Pandavas face numerous challenges and have many adventures. They acquire powerful weapons, receive divine blessings, and gain allies such as Lord Krishna, who becomes their trusted advisor and guide.
            Upon completing their exile, the Pandavas return to claim their kingdom, but the Kauravas refuse to honor their rights. All attempts at peace fail, leading to the inevitable Kurukshetra War.
            The Kurukshetra War is a massive conflict between the Pandavas and the Kauravas. It involves numerous warriors, including Bhishma, Dronacharya, Karna, and others. The war lasts for eighteen days, filled with fierce battles, heroic deeds, and tragic losses.
            Lord Krishna imparts divine knowledge and guidance to Arjuna in the form of the Bhagavad Gita, a spiritual discourse that addresses moral dilemmas, duty, and the path to liberation.
            The war culminates in the defeat of the Kauravas, but it comes at a great cost. Many warriors, including Bhishma, Dronacharya, and Karna, meet their demise. The war leaves a trail of destruction and loss, testing the moral fabric of society.
            Eventually, Yudhishthira ascends the throne as the king of Hastinapura, supported by his brothers and Krishna. They establish a reign of righteousness, justice, and prosperity.
            The Mahabharata also includes various subplots, philosophical discourses, and lessons on life, morality, and dharma. It explores complex characters, their strengths, weaknesses, and inner conflicts.
            The epic concludes with the departure of the Pandavas and other survivors from this mortal realm, symbolizing the end of an era and the beginning of a new cycle.'''


        text1=text1.lower()
        sentences=text1.split('\n')

        tokenizer = Tokenizer(oov_token='<UNK>')
        tokenizer.fit_on_texts(sentences)
        vocab_size = len(tokenizer.word_index) + 1

        sequences = tokenizer.texts_to_sequences(sentences)

        input_sequences = []
        for sequence in sequences:
            for i in range(1, len(sequence)):
                n_gram_sequence = sequence[:i + 1]
                input_sequences.append(n_gram_sequence)

        max_seq_len = max([len(seq) for seq in input_sequences])

        padded_sequences = pad_sequences(input_sequences, maxlen=max_seq_len)

        padded_sequences = np.array(padded_sequences)

        x = padded_sequences[:, :-1]
        labels = padded_sequences[:, -1]

        y = to_categorical(labels)

        model = Sequential()
        model.add(Embedding(vocab_size, 100, input_length=max_seq_len - 1))
        model.add(Bidirectional(LSTM(256)))
        model.add(Dense(vocab_size, activation='softmax'))
        adam = Adam(learning_rate=0.01)
        model.compile(loss='categorical_crossentropy', optimizer=adam, metrics=['acc'])
        epo = number1

        history = model.fit(x, y, epochs=epo, verbose=1, batch_size=512)

        text = text.lower()

        next_words = number
        for _ in range(next_words):
            sequence = tokenizer.texts_to_sequences([text])
            padded = pad_sequences(sequence, maxlen=max_seq_len - 1)
            predicted_probs = model.predict(padded, verbose=0)
            predicted = np.argmax(predicted_probs, axis=1)

            output_word = ''
            for word, index in tokenizer.word_index.items():
                if index == predicted:
                    output_word = word
                    break
            text += ' ' + output_word

        print("The generated Text:", text)
        # End of Machine Learning Code
        return redirect('output', number=number, text=text, square=square)
        #return render(request, 'input.html', {'number': number, 'text': text, 'square': square})
    return render(request, 'input.html')

def output_page(request, number, text, square):
    result = 'Extra Words you asked: {}                        Text Generated: {}'.format(number, text)
    return render(request, 'output.html', {'result': result, 'square': square})

'''
def output_page(request):
    if request.method == 'POST':
        num = int(request.POST['number'])
        text = request.POST['text']
        result = 'Number: {}, Text: {}'.format(num, text)
        return render(request, 'output.html', {'result': result})
    else:
        return render(request, 'output.html')
'''
