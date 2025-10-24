from flask import Flask, render_template, url_for

app = Flask(__name__)

# Data dummy untuk contoh
campus_info = {
    'name': 'Politeknik Baja Tegal',
    'tagline': 'Mencetak Generasi Unggul di Bidang Industri Baja',
    'address': 'Jl. Raya Barat Dukuhwaru, km 7, Dukuhwaru, Kab. Tegal, Jawa Tengah',
    'phone': '+62 823-2558-0008',
    'email': 'poltekbaja@gmail.com',
    'instagram': 'https://www.instagram.com/poltekbajategal?igsh=MXhmMDVnZGJlM2R5NQ==',
    'about': 'POLITEKNIK BAJA TEGAL adalah institusi pendidikan tinggi vokasi yang berfokus pada pengembangan sumber daya manusia di sektor industri baja dan manufaktur. Kami berkomitmen untuk menghasilkan lulusan yang kompeten dan siap kerja di berbagai lini industri.',
    'vision': 'Menjadi politeknik unggulan yang menghasilkan tenaga ahli profesional dan inovatif di bidang industri baja dan manufaktur, serta berkontribusi pada pembangunan ekonomi nasional.',
    'mission': [
        'Menyelenggarakan pendidikan vokasi yang berbasis industri dan relevan dengan kebutuhan pasar kerja, melalui kurikulum yang adaptif dan fasilitas praktik yang modern.',
        'Melakukan penelitian terapan untuk mendukung pengembangan ilmu pengetahuan dan teknologi di industri baja, serta memfasilitasi inovasi yang bermanfaat bagi masyarakat dan industri.',
        'Melaksanakan pengabdian kepada masyarakat melalui penerapan ilmu pengetahuan dan teknologi, pelatihan, dan pendampingan untuk peningkatan kualitas sumber daya manusia dan daya saing industri lokal.'
    ]
}

courses_list = [
    {
        'id': 'd3-teknik-informatika', # ID unik untuk URL
        'name': 'D3 Teknik Informatika',
        'short_description': 'Disiplin ilmu yang menginduk pada ilmu komputer, fokus pada transformasi data dengan teknologi komputer.',
        'full_description': """
            <p>Teknik informatika merupakan disiplin ilmu yang menginduk pada ilmu komputer, yang pada dasarnya merupakan kumpulan disiplin ilmu dan teknik yang secara khusus menangani masalah transformasi atau pengolahan fakta-fakta simbolik (data) dengan memanfaatkan seoptimal mungkin teknologi komputer.</p>
            <p>Transformasi itu berupa proses-proses logika dan sistematika untuk mendapatkan solusi dalam menyelesaikan berbagai masalah, sehingga dengan memilih program studi Teknik Informatika, kita menjadi terlatih berpikir secara logis dan sistematis untuk dapat dengan mudah menyesuaikan diri dengan pekerjaan apapun.</p>
            <p>Program Studi Teknik Informatika di Politeknik Baja Tegal dirancang untuk membekali mahasiswa dengan pengetahuan dan keterampilan dalam bidang teknologi informasi dan komunikasi. Kurikulum mencakup teori dasar komputer, pemrograman, jaringan, keamanan siber, pengembangan perangkat lunak, serta teknologi terbaru seperti kecerdasan buatan dan data science.</p>

            <h3>Prospek Kerja</h3>
            <p>Bidang yang dapat ditekuni seorang lulusan Teknik Informatika cukup beragam, antara lain:</p>
            <ul>
                <li><strong>Programmer</strong><br>
                Baik sebagai system programmer atau application developer, sarjana informatika sangat dibutuhkan di berbagai bidang, misalnya bidang perbankan, telekomunikasi, industri IT, media, instansi pemerintah, dan lain-lain.</li>
                <!-- Anda bisa menambahkan lebih banyak prospek kerja di sini jika ada -->
            </ul>
        """
    },
    {
        'id': 'd3-teknik-otomotif',
        'name': 'D3 Teknik Otomotif',
        'short_description': 'Menghasilkan tenaga ahli madya kompeten di bidang otomotif, konvensional maupun modern (listrik/hybrid).',
        'full_description': """
            <p>Program Studi Teknik Otomotif dirancang untuk menghasilkan tenaga ahli madya yang kompeten di bidang otomotif, baik dalam teknologi kendaraan konvensional maupun kendaraan modern berbasis listrik dan hybrid. Kurikulum dirancang secara komprehensif, mencakup aspek teori dan praktik, sehingga mahasiswa memiliki keterampilan teknis, analitis, serta kemampuan manajerial untuk berkontribusi di dunia industri otomotif.</p>
            <p>Mahasiswa akan dibekali dengan kemampuan menganalisis dan memecahkan masalah terkait mesin, sistem kelistrikan kendaraan, sistem manajemen kendaraan, serta teknologi otomotif terkini seperti IoT pada kendaraan dan teknologi ramah lingkungan.</p>
        """
    },
    {
        'id': 'd3-teknik-mesin',
        'name': 'D3 Teknik Mesin',
        'short_description': 'Lulusan ahli di bidang teknologi manufaktur dan permesinan, siap menghadapi teknologi modern.',
        'full_description': """
            <p>Program Studi D3 Teknik Mesin di Politeknik Baja Tegal dirancang untuk menghasilkan lulusan yang ahli di bidang teknologi manufaktur dan permesinan. Program studi ini mempersiapkan mahasiswa untuk memiliki kemampuan teknis, analisis, dan aplikatif dalam berbagai teknologi modern, seperti mesin CNC, otomasi, CAD/CAM, dan manufaktur canggih. Dengan pendekatan pendidikan vokasi berbasis kompetensi, mahasiswa akan dibekali dengan keterampilan yang relevan dengan kebutuhan industri.</p>
            <p>Teknik Mesin adalah bidang ilmu yang sangat luas, mencakup desain, produksi, operasi, dan pemeliharaan mesin atau alat-alat mekanik. Di era modern, teknik mesin juga berhubungan dengan teknologi inovatif seperti robotika, otomasi, dan energi terbarukan, sehingga lulusan memiliki peluang besar di pasar kerja nasional maupun global.</p>
        """
    },
    {
        'id': 'd3-teknik-elektronika-industri',
        'name': 'D3 Teknik Elektronika Industri',
        'short_description': 'Fokus pada penerapan teknologi elektronika dalam dunia industri modern.',
        'full_description': """
            <p>Teknik Elektronika Industri adalah cabang dari disiplin teknik yang berfokus pada penerapan teknologi elektronika dalam dunia industri. Program Studi Teknik Elektronika Industri di Politeknik Baja Tegal dirancang untuk membekali mahasiswa dengan keahlian praktis dan teoritis dalam merancang, mengembangkan, serta mengelola sistem elektronika yang digunakan di sektor industri modern.</p>
        """
    }
]

@app.route('/')
def index():
    return render_template('index.html', campus=campus_info)

@app.route('/about')
def about():
    return render_template('about.html', campus=campus_info)

@app.route('/courses')
def courses():
    return render_template('courses.html', courses=courses_list)

# Route baru untuk detail program studi
@app.route('/courses/<string:course_id>')
def course_detail(course_id):
    course = next((c for c in courses_list if c['id'] == course_id), None)
    if course:
        return render_template('course_detail.html', course=course)
    return "Program Studi tidak ditemukan", 404 # Atau render halaman 404 custom

if __name__ == '__main__':
    app.run(debug=True)