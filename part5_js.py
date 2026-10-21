JS_HTML = '''<!-- ==================== LOGIC XỬ LÝ DỮ LIỆU & ALPINE.JS STORE TOÀN DIỆN ==================== -->
<script>
function superPetCareApp() {
    return {
        // Trạng thái xác thực & Điều hướng
        isLoggedIn: false, // Mặc định khi vào là Khách chưa đăng nhập
        currentRole: 'customer', // Mặc định hiển thị giao diện khách hàng
        activeCustomerTab: 'home', // 'home' | 'petshare' | 'shop' | 'booking' | 'orders' | 'profile' | 'faq' | 'legal'
        get currentTab() { return this.activeCustomerTab; },
        set currentTab(val) { this.activeCustomerTab = val; },

        activeAdminTab: 'dashboard', // 'dashboard' | 'appointments' | 'orders' | 'products' | 'pets' | 'analytics'
        get adminTab() { return this.activeAdminTab; },
        set adminTab(val) { this.activeAdminTab = val; },

        adminTimeFilter: 'all', // 'all' | 'today' | '7days' | 'month' | 'quarter'
        globalBranch: 'all', // 'all' | 'HN' | 'Q1' | 'Q7' | 'BT'
        currentOrderTypeTab: 'all',
        showLowStockOnly: false,
        sidebarOpen: false,

        // Thông báo hệ thống Admin
        showAdminNotifications: false,
        adminNotifications: [
            { id: 1, type: 'order', icon: 'fa-solid fa-receipt', title: 'Đơn hàng mới thanh toán', desc: 'Khách hàng Nguyễn Phương Thảo vừa thanh toán đơn ORD-8821 qua VietQR (700.000đ)', time: '2 phút trước', read: false },
            { id: 2, type: 'appointment', icon: 'fa-solid fa-calendar-check', title: 'Lịch hẹn mới được đặt', desc: 'Lịch Spa Cắt tỉa bé Bơ (Corgi) lúc 09:30 ngày 21/10 tại CN Quận 7 đã được ghi nhận', time: '15 phút trước', read: false },
            { id: 3, type: 'warning', icon: 'fa-solid fa-triangle-exclamation', title: 'Cảnh báo tồn kho an toàn', desc: 'Sản phẩm "Gel Dinh Dưỡng Virbac Nutri-plus" tại CN Quận 7 sắp hết hàng (còn 6 tuýp)', time: '35 phút trước', read: false },
            { id: 4, type: 'service', icon: 'fa-solid fa-stethoscope', title: 'Cập nhật trạng thái dịch vụ', desc: 'Lịch hẹn APT-1088 đã được Bác sĩ chuyển sang trạng thái: Đang tiếp khách', time: '1 giờ trước', read: false },
            { id: 5, type: 'system', icon: 'fa-solid fa-shield-cat', title: 'Hệ sinh thái PetCare360', desc: 'Hoàn tất chu kỳ tính điểm & cập nhật đặc quyền thành viên 6 tháng định kỳ Q4/2026', time: '2 giờ trước', read: false }
        ],

        // Bộ lọc & Tìm kiếm Khách hàng & Admin
        searchQuery: '',
        filterCategory: 'all', // 'all' | 'Thức ăn & Dinh dưỡng' | 'Phụ kiện & Vệ sinh' | 'Thuốc & Y tế'
        filterServiceCategory: 'all', // 'all' | 'Y Tế & Chăm Sóc Sức Khỏe' | 'Cấp Cứu & Điều Trị Chuyên Sâu' | 'Spa & Làm Đẹp' | 'Lưu Trú & Tiện Ích'
        serviceSearchQuery: '',
        filterArticleCat: 'all',
        searchArticleQuery: '',
        productSearchQuery: '',
        productCategoryFilter: 'all',
        appointmentSearchQuery: '',
        appointmentServiceFilter: 'all',
        orderSearchQuery: '',
        orderStatusFilter: 'all',
        petSearchQuery: '',
        customerSearchQuery: '',

        // Modals flags
        showLoginModal: false,
        loginModalOpen: false,
        showBookingDetailModal: false,
        bookingDetailModalOpen: false,
        showAddPetModal: false,
        addPetModalOpen: false,
        showEditProfileModal: false,
        editProfileModalOpen: false,
        showAddProductModal: false,
        addProductModalOpen: false,
        showRestockModal: false,
        restockModalOpen: false,
        showChatModal: false,
        chatModalOpen: false,
        showCartDrawer: false,
        cartOpen: false,
        showCheckoutModal: false,
        showLoyaltyDetailModal: false,
        loyaltyDetailModalOpen: false,
        showLegalModal: false,
        policyModalOpen: false,
        addAddressModalOpen: false,
        orderDrawerOpen: false,

        selectedServiceModal: null,
        selectedProductModal: null,
        selectedArticleModal: null,
        selectedPetHealthModal: null,
        selectedOrder: null,

        // Login form
        loginUsername: '',
        loginPassword: '',
        loginError: '',

        // Lỗi form thêm thú cưng
        petFormError: '',

        // Hồ sơ người dùng
        customerProfile: {
            name: 'Nguyễn Phương Thảo',
            phone: '0988 123 456',
            email: 'phuongthao.petcare@gmail.com',
            address: 'Căn hộ 12.04 Tòa Park 6, Vinhomes Central Park, Bình Thạnh, TP.HCM',
            avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=300&q=80',
            points: 3450,
            tier: 'Thành viên Vàng',
            nextTierPoints: 7000,
            petCount: 3,
            activeBookings: 2,
            totalSpent: 18500000
        },
        get userProfile() { return this.customerProfile; },
        set userProfile(val) { this.customerProfile = val; },

        // Danh sách địa chỉ nhận hàng
        addresses: [
            { id: 1, tag: 'Nhà riêng', fullAddress: 'Căn hộ 12.04 Tòa Park 6, Vinhomes Central Park, Bình Thạnh, TP.HCM', phone: '0988 123 456', isDefault: true },
            { id: 2, tag: 'Văn phòng', fullAddress: 'Tầng 18 Tòa nhà Bitexco, Số 2 Hải Triều, Bến Nghé, Quận 1, TP.HCM', phone: '0988 123 456', isDefault: false }
        ],

        // Đơn hàng của khách hàng
        customerOrders: [
            {
                id: 'ORD-8821',
                date: '2026-10-20',
                items: 'Royal Canin Mini Adult (1kg), Sữa tắm Davis 4%',
                total: 700000,
                status: 'Đã thanh toán',
                paymentMethod: 'Chuyển khoản VietQR'
            },
            {
                id: 'ORD-8710',
                date: '2026-09-15',
                items: 'Gói Spa & Grooming Cắt Tỉa Lông Toàn Diện (Bé Bơ)',
                total: 350000,
                status: 'Hoàn thành',
                paymentMethod: 'Ví MoMo'
            }
        ],

        // 3 Thú cưng chi tiết đầy đủ 4 nhóm thông tin
        pets: [
            {
                id: 1,
                name: 'Bơ (Butter)',
                type: 'Chó',
                species: 'Chó',
                breed: 'Corgi Pembroke Welsh',
                gender: 'Đực',
                age: '2 tuổi (15/04/2024)',
                weight: '11.5',
                chipId: '900118000452311',
                chip: '900118000452311',
                avatar: 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=400&q=80',
                image: 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=400&q=80',
                appearance: 'Lông vàng trắng ngắn mượt, tai to dựng đứng, đuôi cộc tròn, ngực trắng yếm đôi',
                health: 'Khỏe mạnh, vừa hoàn thành điều trị viêm kẽ móng chân',
                allergies: 'Không dị ứng thuốc, nhạy cảm với thức ăn chứa nhiều mỡ động vật',
                lastVaccine: 'Vắc-xin 7 bệnh chó Nobivac (15/01/2026)',
                nextVaccine: '15/01/2027 (Nhắc lại hàng năm)',
                diet: 'Hạt Royal Canin Mini Adult (80g/ngày), trộn 1/2 hộp Pate Monge gà tây, ăn 2 bữa/ngày',
                habits: 'Thích đi dạo công viên 17h chiều, thích bắt bóng tennis, rất quấn chủ',
                personality: 'Năng động, thân thiện, sủa cảnh giác người lạ gõ cửa, sợ tiếng máy sấy to',
                ownerName: 'Nguyễn Phương Thảo',
                ownerPhone: '0988 123 456',
                ownerAddress: 'Căn hộ 12.04 Tòa Park 6, Vinhomes Central Park, Bình Thạnh, TP.HCM',
                ownerEmergency: '0912 345 678 (Chồng - Anh Hoàng)',
                isDefault: true,
                vaccines: [
                    { name: 'Vắc-xin 7 bệnh chó (Nobivac DHPPi + L4)', date: '15/01/2026', doctor: 'ThS.BS Nguyễn Minh Quân', nextDate: '15/01/2027', status: 'Đã hoàn thành' },
                    { name: 'Phòng ngừa dại (Rabisin)', date: '15/01/2026', doctor: 'ThS.BS Nguyễn Minh Quân', nextDate: '15/01/2027', status: 'Đã hoàn thành' },
                    { name: 'Xổ giun định kỳ & Nhỏ gáy Advocate', date: '01/03/2026', doctor: 'BS Đỗ Hoàng Nam', nextDate: '01/06/2026', status: 'Sắp tới hạn' }
                ],
                medicalHistory: [
                    { date: '10/02/2026', diagnosis: 'Viêm da kẽ ngón chân do ẩm ướt', treatment: 'Vệ sinh Chlorhexidine 2%, bôi kem kháng viêm 5 ngày', notes: 'Giữ chân khô ráo sau khi đi dạo' },
                    { date: '05/11/2025', diagnosis: 'Khám sức khỏe tổng quát & Siêu âm ổ bụng', treatment: 'Chỉ số gan thận bình thường, thể trạng khỏe mạnh', notes: 'Bổ sung thêm glucosamine hỗ trợ cột sống ngắn' }
                ]
            },
            {
                id: 2,
                name: 'Mochi',
                type: 'Mèo',
                species: 'Mèo',
                breed: 'Anh Lông Ngắn (Silver Shaded)',
                gender: 'Cái',
                age: '1.5 tuổi (20/10/2024)',
                weight: '4.2',
                chipId: '900118000789123',
                chip: '900118000789123',
                avatar: 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=400&q=80',
                image: 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=400&q=80',
                appearance: 'Lông ánh bạc silver shaded dày mịn, mắt xanh lục bảo to tròn, mũi hồng',
                health: 'Đã triệt sản nội soi, vết mổ liền đẹp, cân nặng ổn định',
                allergies: 'Dị ứng phấn hoa nhẹ, nhạy cảm với thuốc gây mê nhóm ketamine',
                lastVaccine: 'Vắc-xin 4 bệnh mèo Purevax (20/12/2025)',
                nextVaccine: '20/12/2026',
                diet: 'Hạt Royal Canin Kitten & Sterilised (60g/ngày), thưởng 1 thanh Ciao Churu lúc 20h',
                habits: 'Thích nằm sưởi nắng ban công, cào móng trên trụ đay, ngủ cùng chủ buổi tối',
                personality: 'Điềm đạm, ít kêu, thích được gãi cằm, hay trốn dưới gầm giường khi nhà có khách lạ',
                ownerName: 'Nguyễn Phương Thảo',
                ownerPhone: '0988 123 456',
                ownerAddress: 'Căn hộ 12.04 Tòa Park 6, Vinhomes Central Park, Bình Thạnh, TP.HCM',
                ownerEmergency: '0912 345 678 (Chồng - Anh Hoàng)',
                isDefault: false,
                vaccines: [
                    { name: 'Vắc-xin 4 bệnh mèo (Purevax RCPCh)', date: '20/12/2025', doctor: 'BS Trần Thu Hà', nextDate: '20/12/2026', status: 'Đã hoàn thành' },
                    { name: 'Vắc-xin phòng dại (Rabisin)', date: '20/12/2025', doctor: 'BS Trần Thu Hà', nextDate: '20/12/2026', status: 'Đã hoàn thành' }
                ],
                medicalHistory: [
                    { date: '12/10/2025', diagnosis: 'Phẫu thuật triệt sản nội soi vi phẫu', treatment: 'Hồi phục hoàn toàn sau 48h, chỉ tự tiêu', notes: 'Đã lành sẹo đẹp, chế độ dinh dưỡng hạt Sterilised' }
                ]
            },
            {
                id: 3,
                name: 'Đậu Đậu',
                type: 'Chó',
                species: 'Chó',
                breed: 'Poodle Tiny',
                gender: 'Đực',
                age: '3 tuổi (08/06/2023)',
                weight: '3.6',
                chipId: '900118000994120',
                chip: '900118000994120',
                avatar: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=400&q=80',
                image: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=400&q=80',
                appearance: 'Lông nâu đỏ xoăn tít bồng bềnh, dáng nhỏ nhắn, chân ngắn đáng yêu',
                health: 'Răng miệng sạch mảng bám, mắt sáng không bị ố vàng khóe mắt',
                allergies: 'Tiền sử dị ứng đạm thịt bò (ngứa và đỏ tai)',
                lastVaccine: 'Vắc-xin 7 bệnh Nobivac (05/08/2025)',
                nextVaccine: '05/08/2026',
                diet: 'Hạt dinh dưỡng hữu cơ không thịt bò, bổ sung rau củ tươi luộc chín',
                habits: 'Thích được bế ẵm, thích mặc áo len mùa đông, thích đuổi laser',
                personality: 'Thông minh, hoạt bát, hay làm trò xin ăn, thích chơi đùa với trẻ nhỏ',
                ownerName: 'Nguyễn Phương Thảo',
                ownerPhone: '0988 123 456',
                ownerAddress: 'Căn hộ 12.04 Tòa Park 6, Vinhomes Central Park, Bình Thạnh, TP.HCM',
                ownerEmergency: '0912 345 678 (Chồng - Anh Hoàng)',
                isDefault: false,
                vaccines: [
                    { name: 'Vắc-xin 7 bệnh chó (Nobivac DHPPi)', date: '05/08/2025', doctor: 'ThS.BS Nguyễn Minh Quân', nextDate: '05/08/2026', status: 'Đã hoàn thành' },
                    { name: 'Phòng dại Rabisin', date: '05/08/2025', doctor: 'ThS.BS Nguyễn Minh Quân', nextDate: '05/08/2026', status: 'Đã hoàn thành' }
                ],
                medicalHistory: [
                    { date: '14/01/2026', diagnosis: 'Lấy cao răng siêu âm & đánh bóng răng', treatment: 'Vệ sinh vôi răng độ 2, xịt keo ong khử khuẩn', notes: 'Duy trì gặm thanh sạch răng hàng ngày' }
                ]
            }
        ],
        get allPets() { return this.pets; },
        set allPets(val) { this.pets = val; },
        get myPets() { return this.pets; },
        set myPets(val) { this.pets = val; },

        // 12 SẢN PHẨM PHÂN LOẠI CHÍNH XÁC THEO 3 DANH MỤC
        products: [
            // Danh mục 1: Thức ăn & Dinh dưỡng (6 sản phẩm)
            {
                id: 1,
                sku: 'PET-FD01',
                name: 'Thức Ăn Hạt Royal Canin Mini Adult (Chó Nhỏ)',
                brand: 'Royal Canin (Pháp)',
                price: 360000,
                rating: 4.9,
                reviews: 184,
                reviewsCount: 184,
                sold: 1420,
                stockQ1: 35,
                stockBT: 28,
                stockQ7: 42,
                q1: 35, bt: 28, q7: 42,
                category: 'Thức ăn & Dinh dưỡng',
                categoryAdmin: 'Thức ăn & Dinh dưỡng',
                img: 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=500&q=80',
                desc: 'Hạt dinh dưỡng cao cấp dành cho chó trưởng thành giống nhỏ từ 10 tháng đến 8 tuổi. Giúp duy trì cân nặng lý tưởng nhờ hàm lượng L-carnitine tối ưu và hỗ trợ sức khỏe răng miệng tối đa.',
                description: 'Hạt dinh dưỡng cao cấp dành cho chó trưởng thành giống nhỏ từ 10 tháng đến 8 tuổi.',
                ingredients: 'Protein gia cầm tách nước, bắp, bột bắp, chất béo động vật, gluten bắp, protein thực vật cô lập, lúa mì, khoáng chất, củ cải đường, dầu cá, men bia.',
                usage: 'Cho ăn theo trọng lượng: Chó 2-4kg: 40-70g/ngày; Chó 5-8kg: 80-120g/ngày.'
            },
            {
                id: 2,
                sku: 'PET-FD02',
                name: 'Hạt Royal Canin Kitten Dinh Dưỡng Toàn Diện Cho Mèo Con',
                brand: 'Royal Canin (Pháp)',
                price: 395000,
                rating: 5.0,
                reviews: 216,
                reviewsCount: 216,
                sold: 1890,
                stockQ1: 45,
                stockBT: 30,
                stockQ7: 50,
                q1: 45, bt: 30, q7: 50,
                category: 'Thức ăn & Dinh dưỡng',
                categoryAdmin: 'Thức ăn & Dinh dưỡng',
                img: 'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=500&q=80',
                desc: 'Công thức đặc chế cho mèo con từ 4 đến 12 tháng tuổi. Bổ sung hệ dưỡng chất tăng cường hệ miễn dịch tự nhiên, DHA phát triển não bộ và protein dễ tiêu hóa LIP.',
                description: 'Công thức đặc chế cho mèo con từ 4 đến 12 tháng tuổi.',
                ingredients: 'Protein gia cầm sấy khô, gạo, gluten lúa mì, mỡ động vật, bột ngô, men thủy phân, dầu đậu nành.',
                usage: 'Mèo con 4-6 tháng: 55-70g/ngày; Mèo con 7-12 tháng: 60-80g/ngày.'
            },
            {
                id: 3,
                sku: 'PET-FD03',
                name: 'Thức Ăn Hạt Orijen Original Biologically Appropriate',
                brand: 'Orijen (Canada)',
                price: 890000,
                rating: 4.9,
                reviews: 92,
                reviewsCount: 92,
                sold: 530,
                stockQ1: 18,
                stockBT: 12,
                stockQ7: 15,
                q1: 18, bt: 12, q7: 15,
                category: 'Thức ăn & Dinh dưỡng',
                categoryAdmin: 'Thức ăn & Dinh dưỡng',
                img: 'https://images.unsplash.com/photo-1568640347023-a616a30bc3bd?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1568640347023-a616a30bc3bd?auto=format&fit=crop&w=500&q=80',
                desc: 'Dòng thức ăn sinh học chuẩn tự nhiên cao cấp bậc nhất thế giới, chứa 85% thành phần từ gia cầm thả vườn, cá hoang dã và trứng tươi nguyên quả. Không ngũ cốc.',
                description: 'Dòng thức ăn sinh học chuẩn tự nhiên cao cấp bậc nhất thế giới.',
                ingredients: 'Thịt gà tươi 13%, thịt gà tây tươi 7%, trứng nguyên quả tươi 7%, gan gà tươi 6%, cá trích tươi 6%.',
                usage: 'Thức ăn dinh dưỡng đậm đặc, nên chuyển đổi thức ăn từ từ trong vòng 7 ngày.'
            },
            {
                id: 4,
                sku: 'PET-PT01',
                name: 'Combo 12 Lon Pate Monge Hạt Bổ Dưỡng Cho Chó (Ý)',
                brand: 'Monge (Italy)',
                price: 420000,
                rating: 4.8,
                reviews: 135,
                reviewsCount: 135,
                sold: 1120,
                stockQ1: 30,
                stockBT: 25,
                stockQ7: 35,
                q1: 30, bt: 25, q7: 35,
                category: 'Thức ăn & Dinh dưỡng',
                categoryAdmin: 'Thức ăn & Dinh dưỡng',
                img: 'https://images.unsplash.com/photo-1601758228041-f3b2795255f1?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1601758228041-f3b2795255f1?auto=format&fit=crop&w=500&q=80',
                desc: 'Pate thịt tươi nấu chậm từ nước Ý với các vị gà tây, cá hồi, thịt bò kết hợp rau củ tươi. Không phẩm màu, không chất bảo quản hóa học.',
                description: 'Pate thịt tươi nấu chậm từ nước Ý.',
                ingredients: 'Thịt tươi nguyên miếng 80%, khoáng chất, vitamin A, D3, E tự nhiên, thảo mộc địa trung hải.',
                usage: 'Dùng ăn trực tiếp hoặc trộn cùng hạt khô để kích thích vị giác.'
            },
            {
                id: 5,
                sku: 'PET-PT02',
                name: 'Pate Ciao Churu Cá Ngừ & Sò Điệp Bổ Sung Nước Cho Mèo (Gói 20 Thanh)',
                brand: 'Inaba Ciao (Nhật Bản)',
                price: 215000,
                rating: 5.0,
                reviews: 410,
                reviewsCount: 410,
                sold: 3400,
                stockQ1: 85,
                stockBT: 65,
                stockQ7: 95,
                q1: 85, bt: 65, q7: 95,
                category: 'Thức ăn & Dinh dưỡng',
                categoryAdmin: 'Thức ăn & Dinh dưỡng',
                img: 'https://images.unsplash.com/photo-1533738363-b7f9aef128ce?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1533738363-b7f9aef128ce?auto=format&fit=crop&w=500&q=80',
                desc: 'Treat dạng kem số 1 tại Nhật Bản, vị thơm ngon cuốn hút mọi chú mèo. Cung cấp nước dồi dào ngừa sỏi thận và chiết xuất trà xanh giảm mùi hôi chất thải.',
                description: 'Treat dạng kem số 1 tại Nhật Bản, vị thơm ngon cuốn hút.',
                ingredients: 'Thịt cá ngừ tươi Maguro, chiết xuất sò điệp, collagen biển, chiết xuất trà xanh.',
                usage: 'Cho ăn như món tráng miệng hoặc phần thưởng khi huấn luyện, 2-4 thanh mỗi ngày.'
            },
            {
                id: 6,
                sku: 'PET-MD03',
                name: 'Gel Dinh Dưỡng Bổ Sung Năng Lượng & Vitamin Nutri-plus Gel',
                brand: 'Virbac (Pháp)',
                price: 295000,
                rating: 5.0,
                reviews: 260,
                reviewsCount: 260,
                sold: 2150,
                stockQ1: 2,
                stockBT: 2,
                stockQ7: 2,
                q1: 2, bt: 2, q7: 2, // Tổng tồn kho = 6 (Dưới 10 để demo cảnh báo sắp hết hàng)
                category: 'Thức ăn & Dinh dưỡng',
                categoryAdmin: 'Thức ăn & Dinh dưỡng',
                img: 'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1548767797-d8c844163c4c?auto=format&fit=crop&w=500&q=80',
                desc: 'Thực phẩm bổ sung năng lượng cao cấp chứa đầy đủ vitamin nhóm B, A, D, E và các khoáng chất thiết yếu cho thú cưng đang dưỡng bệnh, sau phẫu thuật hoặc mẹ mang thai/cho con bú.',
                description: 'Thực phẩm bổ sung năng lượng cao cấp chứa đầy đủ vitamin.',
                ingredients: 'Vitamin A, D3, E, B1, B2, B6, B12, Nicotinamide, Canxi Pantothenate, Axit Folic, Sắt, Mangan, Magiê.',
                usage: 'Cho ăn trực tiếp hoặc trộn vào thức ăn. Liều lượng: 1-2 muỗng cà phê/5kg thể trọng.'
            },

            // Danh mục 2: Phụ kiện & Vệ sinh (4 sản phẩm)
            {
                id: 7,
                sku: 'PET-VS01',
                name: 'Cát Đậu Nành Tofu Cature Kháng Khuẩn Tự Nhiên (Hương Trà Xanh 6L)',
                brand: 'Cature (Mỹ)',
                price: 165000,
                rating: 4.8,
                reviews: 280,
                reviewsCount: 280,
                sold: 2890,
                stockQ1: 60,
                stockBT: 45,
                stockQ7: 75,
                q1: 60, bt: 45, q7: 75,
                category: 'Phụ kiện & Vệ sinh',
                categoryAdmin: 'Phụ kiện & Vệ sinh',
                img: 'https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=500&q=80',
                desc: '100% bã đậu nành tự nhiên vón cục siêu tốc trong 3 giây, kiểm soát mùi hôi vượt trội, tan hoàn toàn trong nước xả bồn cầu cực kỳ tiện lợi và thân thiện môi trường.',
                description: '100% bã đậu nành tự nhiên vón cục siêu tốc trong 3 giây.',
                ingredients: 'Sợi đậu nành hữu cơ, tinh bột ngô tự nhiên, chiết xuất lá trà xanh diệt khuẩn.',
                usage: 'Đổ cát vào khay vệ sinh độ dày khoảng 5-7cm. Dọn các cục vón hàng ngày.'
            },
            {
                id: 8,
                sku: 'PET-VS02',
                name: 'Sữa Tắm Trị Nấm & Khử Mùi Hôi Cho Thú Cưng Davis Chlorhexidine 4%',
                brand: 'Davis (Mỹ)',
                price: 340000,
                rating: 4.9,
                reviews: 145,
                reviewsCount: 145,
                sold: 980,
                stockQ1: 22,
                stockBT: 18,
                stockQ7: 25,
                q1: 22, bt: 18, q7: 25,
                category: 'Phụ kiện & Vệ sinh',
                categoryAdmin: 'Phụ kiện & Vệ sinh',
                img: 'https://images.unsplash.com/photo-1535294435445-d7249524ef2e?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1535294435445-d7249524ef2e?auto=format&fit=crop&w=500&q=80',
                desc: 'Sữa tắm dược liệu đặc trị viêm da, nấm da, vi khuẩn và mùi hôi khó chịu trên chó mèo. Chứa hoạt chất Chlorhexidine Gluconate 4% được các bác sĩ da liễu thú y khuyên dùng.',
                description: 'Sữa tắm dược liệu đặc trị viêm da, nấm da, vi khuẩn.',
                ingredients: 'Chlorhexidine Gluconate 4.0%, chất tạo bọt dịu nhẹ từ dừa, tinh dầu dưỡng ẩm da.',
                usage: 'Làm ướt lông, thoa dầu tắm tạo bọt và xoa bóp đều trong 5-10 phút rồi xả sạch với nước.'
            },
            {
                id: 9,
                sku: 'PET-PK01',
                name: 'Balo Phi Thuyền Vận Chuyển Thú Cưng Thông Khí Đa Chiều VIP',
                brand: 'PetCare Pro',
                price: 490000,
                rating: 4.7,
                reviews: 86,
                reviewsCount: 86,
                sold: 620,
                stockQ1: 15,
                stockBT: 10,
                stockQ7: 12,
                q1: 15, bt: 10, q7: 12,
                category: 'Phụ kiện & Vệ sinh',
                categoryAdmin: 'Phụ kiện & Vệ sinh',
                img: 'https://images.unsplash.com/photo-1522276498395-f4f68f7f8454?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1522276498395-f4f68f7f8454?auto=format&fit=crop&w=500&q=80',
                desc: 'Balo vận chuyển thú cưng cao cấp chất liệu nhựa ABS cứng cáp chống va đập, nắp trong suốt tầm nhìn rộng, hệ thống 9 lỗ thoáng khí và đệm lót êm ái cho bé dưới 8kg.',
                description: 'Balo vận chuyển thú cưng cao cấp chất liệu nhựa ABS cứng cáp.',
                ingredients: 'Nhựa ABS an toàn thực phẩm, vải Oxford 900D chống thấm, lưới thép không gỉ.',
                usage: 'Phù hợp khi chở bé đi tiêm phòng, du lịch hoặc dạo phố an toàn tuyệt đối.'
            },
            {
                id: 10,
                sku: 'PET-PK02',
                name: 'Trụ Cào Móng Cây Cat Tree 3 Tầng Kèm Nhà Cầu Ngủ Mèo',
                brand: 'CozyPet',
                price: 680000,
                rating: 4.9,
                reviews: 64,
                reviewsCount: 64,
                sold: 410,
                stockQ1: 10,
                stockBT: 8,
                stockQ7: 14,
                q1: 10, bt: 8, q7: 14,
                category: 'Phụ kiện & Vệ sinh',
                categoryAdmin: 'Phụ kiện & Vệ sinh',
                img: 'https://images.unsplash.com/photo-1545249390-6bdfa286032f?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1545249390-6bdfa286032f?auto=format&fit=crop&w=500&q=80',
                desc: 'Cây cào móng cao cấp quấn dây đay sisal tự nhiên bền chắc, khung gỗ ép công nghiệp chịu lực, bọc vải nhung mềm mịn giúp mèo xả stress và bảo vệ sofa nội thất gia đình.',
                description: 'Cây cào móng cao cấp quấn dây đay sisal tự nhiên bền chắc.',
                ingredients: 'Gỗ chịu lực MDF, dây thừng Sisal tự nhiên, vải nỉ lông cừu nhân tạo.',
                usage: 'Đặt tại góc phòng khách nơi mèo thường xuyên qua lại hoặc gần cửa sổ đón nắng.'
            },

            // Danh mục 3: Thuốc & Y tế (2 sản phẩm)
            {
                id: 11,
                sku: 'PET-MD01',
                name: 'Thuốc Trị Ve Rận & Tẩy Giun NexGard Spectra (Dạng Viên Nhai Thịt Bò)',
                brand: 'Boehringer Ingelheim (Pháp)',
                price: 460000,
                rating: 5.0,
                reviews: 320,
                reviewsCount: 320,
                sold: 2100,
                stockQ1: 30,
                stockBT: 25,
                stockQ7: 35,
                q1: 30, bt: 25, q7: 35,
                category: 'Thuốc & Y tế',
                categoryAdmin: 'Thuốc & Y tế',
                img: 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=500&q=80',
                desc: 'Viên nhai vị thịt bò thơm ngon bảo vệ toàn diện 1 tháng: tiêu diệt bọ chét, ve chó, ghẻ Demodex, phòng giun tim và tẩy sạch các loại giun đường ruột.',
                description: 'Viên nhai vị thịt bò thơm ngon bảo vệ toàn diện 1 tháng.',
                ingredients: 'Afoxolaner và Milbemycin Oxime tinh khiết chuẩn dược phẩm thú y quốc tế.',
                usage: 'Cho chó nhai trực tiếp như bánh thưởng. Dùng định kỳ 1 viên/tháng cho cún từ 8 tuần tuổi.'
            },
            {
                id: 12,
                sku: 'PET-MD02',
                name: 'Tuýp Nhỏ Gáy Phòng Trị Ký Sinh Trùng Toàn Diện Cho Mèo Revolution Plus',
                brand: 'Zoetis (Mỹ)',
                price: 385000,
                rating: 4.9,
                reviews: 198,
                reviewsCount: 198,
                sold: 1650,
                stockQ1: 38,
                stockBT: 28,
                stockQ7: 42,
                q1: 38, bt: 28, q7: 42,
                category: 'Thuốc & Y tế',
                categoryAdmin: 'Thuốc & Y tế',
                img: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=500&q=80',
                image: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=500&q=80',
                desc: 'Dược chất thế hệ mới tiêu diệt 6 loại ký sinh trùng gây hại trên mèo: bọ chét, ấu trùng bọ chét, ve, rận tai, giun tim, giun đũa và giun móc chỉ với 1 giọt nhỏ gáy.',
                description: 'Dược chất thế hệ mới tiêu diệt 6 loại ký sinh trùng trên mèo.',
                ingredients: 'Selamectin và Sarolaner nồng độ cao an toàn cho mèo từ 8 tuần tuổi.',
                usage: 'Vạch lông sau gáy mèo và bóp hết tuýp thuốc trực tiếp lên da.'
            }
        ],

        // 12 DỊCH VỤ PHÂN LOẠI CHÍNH XÁC THEO 4 DANH MỤC YÊU CẦU
        services: [
            // Nhóm 1: Y Tế & Chăm Sóc Sức Khỏe (5 dịch vụ)
            {
                id: 1,
                name: 'Khám Sức Khỏe Tổng Quát & Tầm Soát Bệnh Lý Thú Cưng',
                price: 250000,
                duration: '45 - 60 phút',
                expert: 'ThS. Bác sĩ Thú y chuyên khoa Nội',
                doctor: 'ThS. BS Nguyễn Minh Quân',
                category: 'Y Tế & Chăm Sóc Sức Khỏe',
                img: 'https://images.unsplash.com/photo-1628009368231-7bb7cfcb0def?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1628009368231-7bb7cfcb0def?auto=format&fit=crop&w=600&q=80',
                desc: 'Quy trình kiểm tra toàn diện 12 cơ quan trọng yếu: tim phổi, răng miệng, mắt tai, ổ bụng, xương khớp, huyết áp và kiểm tra ký sinh trùng da lông.',
                description: 'Quy trình kiểm tra toàn diện 12 cơ quan trọng yếu.',
                rating: 4.9,
                reviewsCount: 312,
                icon: 'fa-solid fa-stethoscope',
                tags: ['12 cơ quan', 'Khám lâm sàng', 'Sổ sức khỏe'],
                steps: [
                    { title: 'Thu thập tiền sử bệnh & cân đo chỉ số sinh tồn', desc: 'Đo thân nhiệt, huyết áp, cân nặng, nhịp tim và nghe phổi bằng ống nghe chuyên dụng.' },
                    { title: 'Khám lâm sàng chi tiết mắt - tai - miệng', desc: 'Nội soi ống tai, kiểm tra giác mạc và đánh giá mức độ vôi răng hay viêm nướu.' },
                    { title: 'Sờ nắn ổ bụng & kiểm tra hệ vận động khớp', desc: 'Đánh giá gan lách thận bàng quang và phản xạ các khớp xương chi.' },
                    { title: 'Soi tươi da lông kiểm tra nấm & ghẻ Demodex', desc: 'Lấy mẫu biểu bì kiểm tra dưới kính hiển vi quang học độ phóng đại lớn.' },
                    { title: 'Tư vấn phác đồ phòng bệnh & cấp sổ theo dõi', desc: 'Bác sĩ phân tích kết quả, lập phác đồ dinh dưỡng và chế độ tiêm phòng tối ưu.' }
                ]
            },
            {
                id: 2,
                name: 'Tiêm Chủng Vắc-xin Phòng Bệnh Đa Giá Nhập Khẩu (Chó & Mèo)',
                price: 220000,
                duration: '30 phút',
                expert: 'Bác sĩ Thú y chính quy',
                doctor: 'BS Trần Thu Hà',
                category: 'Y Tế & Chăm Sóc Sức Khỏe',
                img: 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=600&q=80',
                desc: 'Tiêm phòng vắc-xin chính hãng (Nobivac, Zoetis) phòng 7 bệnh nguy hiểm trên chó và 4 bệnh trên mèo. Được lưu trữ trong hệ thống tủ lạnh bảo quản chuẩn GSP y tế.',
                description: 'Tiêm phòng vắc-xin chính hãng lưu trữ chuẩn GSP y tế.',
                rating: 5.0,
                reviewsCount: 450,
                icon: 'fa-solid fa-syringe',
                tags: ['Chuẩn GSP', 'Khám sàng lọc', 'Bảo hiểm phản vệ'],
                steps: [
                    { title: 'Khám sàng lọc trước tiêm', desc: 'Đo thân nhiệt và xác nhận thể trạng hoàn toàn khỏe mạnh, không sốt, không ủ bệnh.' },
                    { title: 'Kiểm tra tem mã lô & hạn sử dụng vắc-xin', desc: 'Khách hàng trực tiếp đối chiếu tem niêm phong và hạn sử dụng của lọ thuốc.' },
                    { title: 'Thực hiện tiêm dưới da chuẩn kỹ thuật không đau', desc: 'Sát khuẩn kỹ càng, sử dụng kim tiêm siêu nhỏ hạn chế tối đa cảm giác nhói.' },
                    { title: 'Theo dõi phản ứng sốc phản vệ 15 phút tại chỗ', desc: 'Bé được nghỉ ngơi tại phòng chờ có điều hòa và bác sĩ túc trực quan sát.' },
                    { title: 'Dán tem vào sổ tiêm & cài đặt lịch nhắc hẹn', desc: 'Cấp chứng nhận tiêm phòng và gửi tin nhắn SMS nhắc lịch tái chủng tự động.' }
                ]
            },
            {
                id: 3,
                name: 'Xét Nghiệm Máu Tổng Quát 18 Chỉ Số & Test Nhanh Bệnh Truyền Nhiễm',
                price: 380000,
                duration: '30 - 45 phút lấy kết quả ngay',
                expert: 'Kỹ thuật viên Xét nghiệm Y khoa',
                doctor: 'KTV Xét nghiệm Thú y',
                category: 'Y Tế & Chăm Sóc Sức Khỏe',
                img: 'https://images.unsplash.com/photo-1579154204601-01588f351e67?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1579154204601-01588f351e67?auto=format&fit=crop&w=600&q=80',
                desc: 'Hệ thống máy xét nghiệm huyết học và sinh hóa tự động IDEXX (Mỹ) cho kết quả chính xác 99.9% chỉ trong 15 phút, phát hiện sớm suy thận, viêm tụy, Care, Parvo, FIP.',
                description: 'Máy xét nghiệm sinh hóa tự động IDEXX Mỹ lấy kết quả sau 15p.',
                rating: 4.9,
                reviewsCount: 188,
                icon: 'fa-solid fa-vial-virus',
                tags: ['Máy IDEXX Mỹ', '15 phút', 'Độ chính xác 99.9%'],
                steps: [
                    { title: 'Lấy mẫu máu tĩnh mạch êm ái', desc: 'Kỹ thuật viên thao tác chuẩn xác, lượng máu lấy rất nhỏ không gây mệt cho bé.' },
                    { title: 'Chạy máy huyết học tự động 18 chỉ số (CBC)', desc: 'Kiểm tra bạch cầu (nhiễm trùng), hồng cầu (thiếu máu), tiểu cầu.' },
                    { title: 'Đo sinh hóa chức năng gan, thận và đường huyết', desc: 'Đánh giá nồng độ men gan ALT, Creatinine, BUN, Glucose máu.' },
                    { title: 'Thực hiện test nhanh kháng nguyên bệnh truyền nhiễm', desc: 'Kit test chuyên biệt phát hiện virus Parvo, Care, Giảm bạch cầu (FPV).' },
                    { title: 'Bác sĩ giải thích tường tận từng chỉ số bất thường', desc: 'Đưa ra lời khuyên dinh dưỡng hoặc phác đồ can thiệp kịp thời.' }
                ]
            },
            {
                id: 4,
                name: 'Siêu Âm Màu 4D & Chụp X-Quang Kỹ Thuật Số (DR) Tận Nơi',
                price: 300000,
                duration: '40 phút',
                expert: 'Bác sĩ Chẩn đoán Hình ảnh Thú y',
                doctor: 'BS CĐHA Thú y',
                category: 'Y Tế & Chăm Sóc Sức Khỏe',
                img: 'https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1516549655169-df83a0774514?auto=format&fit=crop&w=600&q=80',
                desc: 'Máy siêu âm Doppler màu hiện đại chẩn đoán thai kỳ, sỏi bàng quang, khối u và máy X-quang kỹ thuật số liều phóng xạ thấp kiểm tra xương khớp.',
                description: 'Máy siêu âm Doppler màu hiện đại và X-quang kỹ thuật số.',
                rating: 4.8,
                reviewsCount: 142,
                icon: 'fa-solid fa-x-ray',
                tags: ['Doppler màu 4D', 'X-quang DR', 'Ảnh số qua App'],
                steps: [
                    { title: 'Chuẩn bị tư thế và cạo lông vùng kiểm tra', desc: 'Vệ sinh da và bôi gel siêu âm chuyên dụng không gây kích ứng.' },
                    { title: 'Quét siêu âm Doppler đánh giá chi tiết các tạng', desc: 'Đo kích thước tim thận, kiểm tra tuần hoàn máu và đếm số lượng thai nhi.' },
                    { title: 'Chụp phim X-quang các tư thế chuẩn', desc: 'Đánh giá dị vật đường tiêu hóa, gãy xương hoặc thoát vị đĩa đệm.' },
                    { title: 'Hội chẩn hình ảnh với bác sĩ chuyên khoa', desc: 'Phân tích bất thường và lập bản báo cáo chẩn đoán hình ảnh chuẩn xác.' },
                    { title: 'Trả file ảnh kỹ thuật số chất lượng cao qua App', desc: 'Khách hàng có thể lưu trữ và xem lại hình ảnh trên hồ sơ bệnh án điện tử.' }
                ]
            },
            {
                id: 5,
                name: 'Lấy Cao Răng Siêu Âm Không Đau & Đánh Bóng Men Răng',
                price: 320000,
                duration: '60 phút',
                expert: 'Bác sĩ Nha khoa Thú y',
                doctor: 'BS Nha khoa Thú y',
                category: 'Y Tế & Chăm Sóc Sức Khỏe',
                img: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=600&q=80',
                desc: 'Sử dụng đầu rung siêu âm tần số cao bóc tách nhẹ nhàng mảng bám vôi răng dưới nướu, chữa dứt điểm viêm lợi và mùi hôi miệng kéo dài.',
                description: 'Đầu rung siêu âm tần số cao bóc tách mảng bám không đau.',
                rating: 4.9,
                reviewsCount: 210,
                icon: 'fa-solid fa-tooth',
                tags: ['Sóng siêu âm', 'Đánh bóng men', 'Khử hôi miệng'],
                steps: [
                    { title: 'Thăm khám mức độ viêm nướu & tiền mê nhẹ', desc: 'Tiền mê an toàn bằng khí mê Isoflurane giúp bé nằm yên không lo sợ.' },
                    { title: 'Lấy mảng bám bằng máy siêu âm nước ấm', desc: 'Làm sạch triệt để từng kẽ răng và túi nha chu mà không mòn men răng.' },
                    { title: 'Đánh bóng bề mặt răng bằng paste nha khoa', desc: 'Tạo bề mặt nhẵn bóng ngăn ngừa thức ăn và vi khuẩn tái bám dính.' },
                    { title: 'Xịt gel kháng khuẩn sinh học thảo dược', desc: 'Làm dịu mô nướu, hỗ trợ tái tạo niêm mạc miệng tổn thương.' },
                    { title: 'Hướng dẫn chủ nuôi chăm sóc răng tại nhà', desc: 'Tư vấn loại gel đánh răng enzym và đồ gặm làm sạch mảng bám.' }
                ]
            },

            // Nhóm 2: Cấp Cứu & Điều Trị Chuyên Sâu (3 dịch vụ)
            {
                id: 6,
                name: 'Cấp Cứu Thú Y 24/7 & Hồi Sức Tích Cực (ICU)',
                price: 500000,
                duration: 'Phục vụ 24/24h',
                expert: 'Đội ngũ Bác sĩ Cấp cứu & Ngoại khoa thường trực',
                doctor: 'BS Đỗ Hoàng Nam (Đội trưởng ICU)',
                category: 'Cấp Cứu & Điều Trị Chuyên Sâu',
                img: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=600&q=80',
                desc: 'Phòng cấp cứu vô trùng trang bị máy thở oxy cao áp, máy sốc tim, monitor theo dõi huyết động học và đội xe cấp cứu cơ động đón tận nhà bất kể ngày đêm.',
                description: 'Phòng cấp cứu vô trùng trang bị máy thở oxy cao áp 24/7.',
                rating: 5.0,
                reviewsCount: 165,
                icon: 'fa-solid fa-truck-medical',
                tags: ['Trực 24/7', 'Thở oxy cao áp', 'Monitor ICU'],
                steps: [
                    { title: 'Tiếp nhận khẩn cấp & phân loại bệnh tình (Triage)', desc: 'Xác định nhanh tình trạng suy hô hấp, xuất huyết, ngộ độc hay đa chấn thương.' },
                    { title: 'Thiết lập đường truyền tĩnh mạch & hỗ trợ oxy', desc: 'Đặt catheter ven ngay lập tức, truyền dịch cân bằng điện giải và thở oxy buồng kín.' },
                    { title: 'Xét nghiệm cấp cứu tại giường & Chụp X-quang/Siêu âm', desc: 'Đọc kết quả khí máu và hình ảnh chẩn đoán trong vòng 5-10 phút.' },
                    { title: 'Phẫu thuật khẩn cấp hoặc điều trị nội trú ICU', desc: 'Chuyển thẳng vào phòng mổ áp lực dương hoặc lồng hồi sức kiểm soát nhiệt ẩm.' },
                    { title: 'Báo cáo diễn tiến sức khỏe liên tục cho gia đình', desc: 'Cập nhật tình trạng qua Zalo/Camera giám sát lồng bệnh 24/24.' }
                ]
            },
            {
                id: 7,
                name: 'Phẫu Thuật Triệt Sản Nội Soi An Toàn Vi Phẫu (Chó & Mèo)',
                price: 650000,
                duration: '120 phút',
                expert: 'Bác sĩ Ngoại khoa trưởng ca',
                doctor: 'BS Ngoại khoa Thú y',
                category: 'Cấp Cứu & Điều Trị Chuyên Sâu',
                img: 'https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1579684385127-1ef15d508118?auto=format&fit=crop&w=600&q=80',
                desc: 'Phương pháp vi phẫu đường mổ siêu nhỏ (dưới 1cm) hạn chế đau đớn, không chảy máu, khâu thẩm mỹ chỉ tự tiêu không cần quay lại cắt chỉ.',
                description: 'Phương pháp vi phẫu đường mổ siêu nhỏ chỉ tự tiêu.',
                rating: 5.0,
                reviewsCount: 280,
                icon: 'fa-solid fa-kit-medical',
                tags: ['Vi phẫu < 1cm', 'Chỉ tự tiêu', 'Gây mê Isoflurane'],
                steps: [
                    { title: 'Xét nghiệm máu kiểm tra đông máu & chức năng gan thận', desc: 'Đảm bảo bé đủ điều kiện chịu mê an toàn tuyệt đối 100%.' },
                    { title: 'Gây mê đa mô thức bằng máy thở Isoflurane hiện đại', desc: 'Theo dõi nhịp tim, nồng độ oxy trong máu liên tục suốt ca mổ.' },
                    { title: 'Tiến hành phẫu thuật trong phòng vô trùng tuyệt đối', desc: 'Dụng cụ tiệt trùng Autoclave, bác sĩ phẫu thuật mặc áo vô khuẩn.' },
                    { title: 'Khâu chỉ thẩm mỹ tự tiêu giấu vết mổ', desc: 'Không để lại vết sẹo lồi, thú cưng không cần đeo vòng chống liếm quá lâu.' },
                    { title: 'Hồi tỉnh tại phòng chăm sóc hậu phẫu êm dịu', desc: 'Tiêm thuốc giảm đau 24h và cấp thuốc uống chống viêm tại nhà.' }
                ]
            },
            {
                id: 8,
                name: 'Vật Lý Trị Liệu & Phục Hồi Chức Năng Cột Sống - Khớp',
                price: 300000,
                duration: '60 phút',
                expert: 'Bác sĩ Phục hồi Chức năng Thú y',
                doctor: 'BS PHCN Thú y',
                category: 'Cấp Cứu & Điều Trị Chuyên Sâu',
                img: 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=600&q=80',
                desc: 'Liệu trình vật lý trị liệu laser giảm đau sâu, thủy trị liệu bồn bơi nước ấm và châm cứu phục hồi phản xạ thần kinh cho các bé bị liệt 2 chân sau, thoái hóa khớp.',
                description: 'Laser giảm đau sâu, thủy trị liệu và châm cứu phục hồi khớp.',
                rating: 4.8,
                reviewsCount: 95,
                icon: 'fa-solid fa-bone',
                tags: ['Laser trị liệu', 'Thủy trị liệu', 'Phục hồi khớp'],
                steps: [
                    { title: 'Đánh giá thang điểm đau & mức độ vận động', desc: 'Kiểm tra phản xạ cơ bắp, độ co duỗi khớp và mức độ tổn thương thần kinh.' },
                    { title: 'Chiếu tia Laser cường độ thấp giảm viêm sâu', desc: 'Tăng cường tuần hoàn máu nuôi dưỡng mô sụn và cắt đứt cơn đau cơ.' },
                    { title: 'Thủy trị liệu (Hydrotherapy) trên máy chạy bộ dưới nước', desc: 'Nước nâng đỡ trọng lượng cơ thể giúp bé tập bước đi mà không áp lực lên xương.' },
                    { title: 'Xoa bóp nắn chỉnh cơ và kéo giãn nhẹ nhàng', desc: 'Chống teo cơ, duy trì độ dẻo dai của gân dây chằng.' },
                    { title: 'Bài tập phục hồi tại nhà cùng chủ nuôi', desc: 'Hướng dẫn các động tác mát-xa và dụng cụ hỗ trợ xe lăn nếu cần thiết.' }
                ]
            },

            // Nhóm 3: Spa & Làm Đẹp (2 dịch vụ)
            {
                id: 9,
                name: 'Gói Spa & Grooming Cắt Tỉa Lông Tạo Kiểu Toàn Diện',
                price: 350000,
                duration: '120 - 150 phút',
                expert: 'Master Groomer & Kỹ thuật viên cao cấp',
                doctor: 'Master Groomer & KTV cao cấp',
                category: 'Spa & Làm Đẹp',
                img: 'https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?auto=format&fit=crop&w=600&q=80',
                desc: 'Gói chăm sóc sắc đẹp đẳng cấp nhất cho bé cưng: tắm sục ozone thải độc da, sấy chải bông phồng, cắt móng mài góc tròn, vệ sinh nhổ lông tai và cắt tỉa lông tạo kiểu theo chuẩn dáng giống loài.',
                description: 'Gói chăm sóc sắc đẹp đẳng cấp nhất cho bé cưng.',
                rating: 5.0,
                reviewsCount: 520,
                icon: 'fa-solid fa-scissors',
                tags: ['Chuẩn 5 bước', 'Bồn sục Ozone', 'Tạo kiểu dáng chuẩn'],
                steps: [
                    { title: 'Kiểm tra da lông & tư vấn form dáng', desc: 'Kiểm tra tình trạng búi lông, ve rận, nấm và tư vấn dáng cắt tỉa phù hợp.' },
                    { title: 'Vệ sinh sơ bộ chuyên sâu', desc: 'Cắt mài móng không chảy máu, nhổ sạch lông tai, cạo lông đệm chân và vệ sinh hậu môn.' },
                    { title: 'Tắm bồn sục Ozone thư giãn 2 lần', desc: 'Dùng dầu gội hữu cơ nhập khẩu khử mùi, massage giải tỏa căng thẳng và ủ xả phục hồi lông.' },
                    { title: 'Sấy ion âm & chải tơi lông chuyên nghiệp', desc: 'Sấy gió ấm bảo vệ da, chải gỡ rối hoàn toàn và đánh bông lớp lông lót.' },
                    { title: 'Cắt tỉa tạo kiểu nghệ thuật & xịt tinh dầu', desc: 'Master Groomer tỉa thủ công từng góc cạnh sắc sảo và xịt tinh dầu dưỡng lông.' }
                ]
            },
            {
                id: 10,
                name: 'Tắm Trị Liệu Trị Nấm & Viêm Da Chuyên Sâu Bằng Dược Thảo',
                price: 280000,
                duration: '90 phút',
                expert: 'Kỹ thuật viên Da liễu Thú y',
                doctor: 'KTV Da liễu Thú y',
                category: 'Spa & Làm Đẹp',
                img: 'https://images.unsplash.com/photo-1535294435445-d7249524ef2e?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1535294435445-d7249524ef2e?auto=format&fit=crop&w=600&q=80',
                desc: 'Phác đồ điều trị dứt điểm các bệnh lý da liễu: nấm Microsporum, viêm da Demodex, viêm nang lông có mủ và vảy gàu ngứa ngáy dữ dội.',
                description: 'Phác đồ điều trị dứt điểm các bệnh lý da liễu và nấm ngứa.',
                rating: 4.9,
                reviewsCount: 175,
                icon: 'fa-solid fa-shower',
                tags: ['Davis 4%', 'Giảm ngứa tức thì', 'Diệt bào tử nấm'],
                steps: [
                    { title: 'Cạo sạch vùng lông tổn thương khu trú', desc: 'Tạo sự thông thoáng để thuốc tiếp xúc trực tiếp vào ổ nấm/vi khuẩn.' },
                    { title: 'Tắm xả bằng nước ấm ion hóa loại bỏ tế bào chết', desc: 'Làm mềm vảy gàu và rửa trôi chất nhờn tích tụ trên bề mặt da.' },
                    { title: 'Ủ dầu tắm dược liệu trị nấm Davis Chlorhexidine 15 phút', desc: 'Hoạt chất thấm sâu tiêu diệt bào tử nấm và vi khuẩn gây mủ.' },
                    { title: 'Ngâm bồn thảo dược phục hồi hàng rào bảo vệ da', desc: 'Chiết xuất yến mạch và tràm trà giúp giảm ngứa tức thì.' },
                    { title: 'Sấy khô bằng lồng sấy gió nhẹ & xịt dưỡng ẩm', desc: 'Không làm khô rát da, phục hồi nang lông mọc lại nhanh chóng.' }
                ]
            },

            // Nhóm 4: Lưu Trú & Tiện Ích (2 dịch vụ)
            {
                id: 11,
                name: 'Khách Sạn Thú Cưng Pet Hotel Đẳng Cấp 5 Sao (Có Camera 24/7)',
                price: 200000,
                duration: 'Tính theo ngày (24 giờ)',
                expert: 'Quản gia thú cưng & Bác sĩ túc trực',
                doctor: 'KTV Quản gia Pet Hotel',
                category: 'Lưu Trú & Tiện Ích',
                img: 'https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1541781774459-bb2af2f05b55?auto=format&fit=crop&w=600&q=80',
                desc: 'Phòng lưu trú riêng biệt máy lạnh 24/7, lọc không khí ion âm diệt khuẩn. Khách hàng có tài khoản xem camera riêng của phòng bé bất kỳ lúc nào.',
                description: 'Phòng lưu trú riêng biệt máy lạnh 24/7 kèm camera xem trực tiếp.',
                rating: 4.9,
                reviewsCount: 340,
                icon: 'fa-solid fa-hotel',
                tags: ['Camera 24/7', 'Điều hòa riêng', 'Dinh dưỡng 3 bữa'],
                steps: [
                    { title: 'Tiếp nhận & kiểm tra sức khỏe ban đầu', desc: 'Xác nhận sổ tiêm ngừa, kiểm tra ve rận và lập thực đơn ăn uống theo thói quen của bé.' },
                    { title: 'Nhận phòng VIP riêng biệt khử khuẩn bằng tia UV', desc: 'Trang bị nệm êm ái, khay cát riêng biệt và đồ chơi yêu thích.' },
                    { title: 'Chế độ dinh dưỡng 3 bữa tiêu chuẩn quốc tế', desc: 'Phục vụ hạt cao cấp Royal Canin/Orijen kèm pate tươi nấu trong ngày.' },
                    { title: 'Giờ vận động vui chơi sân vườn 2 lần/ngày', desc: 'Nhân viên dắt bé dạo chơi và tương tác tại khu vận động trong nhà sạch sẽ.' },
                    { title: 'Báo cáo video & nhật ký chăm sóc hàng ngày', desc: 'Gửi clip ăn uống, sinh hoạt và tặng gói tắm sấy trước khi check-out đón về.' }
                ]
            },
            {
                id: 12,
                name: 'Đưa Đón Thú Cưng Khám Bệnh & Spa Tận Cửa Bằng Xe Chuyên Dụng (Pet Taxi)',
                price: 150000,
                duration: 'Theo lịch hẹn khách đặt',
                expert: 'Tài xế chuyên trách & Nhân viên an toàn thú cưng',
                doctor: 'Đội xe Pet Taxi Cơ Động',
                category: 'Lưu Trú & Tiện Ích',
                img: 'https://images.unsplash.com/photo-1522276498395-f4f68f7f8454?auto=format&fit=crop&w=600&q=80',
                image: 'https://images.unsplash.com/photo-1522276498395-f4f68f7f8454?auto=format&fit=crop&w=600&q=80',
                desc: 'Xe ô tô cứu thương & đưa đón thú cưng chuyên dụng, khoang xe rộng rãi có điều hòa mát lạnh, lồng vận chuyển êm ái, dây an toàn chuyên dụng và tài xế am hiểu tâm lý động vật.',
                description: 'Xe ô tô chuyên dụng đưa đón thú cưng tận nhà an toàn chu đáo.',
                rating: 4.8,
                reviewsCount: 160,
                icon: 'fa-solid fa-taxi',
                tags: ['Đón tận cửa', 'Lồng chuyên dụng', 'Bật nhạc thiền thư giãn'],
                steps: [
                    { title: 'Nhận lịch hẹn & xác nhận địa chỉ đón trả', desc: 'Hệ thống gửi định vị xe và thời gian tài xế có mặt chuẩn xác từng phút.' },
                    { title: 'Đón bé tận cửa và kiểm tra dây đeo an toàn', desc: 'Nhân viên đưa bé vào lồng vận chuyển chuyên dụng êm ái và sạch sẽ.' },
                    { title: 'Di chuyển êm ái với điều hòa khoang riêng', desc: 'Bật nhạc thiền tần số thấp giúp thú cưng thư giãn, không bị say xe.' },
                    { title: 'Bàn giao trực tiếp cho Bác sĩ / Groomer tại viện', desc: 'Gửi video check-in khi bé đã đến nơi an toàn để phụ huynh an tâm.' },
                    { title: 'Đưa bé về tận nhà sau khi hoàn thành dịch vụ', desc: 'Bàn giao kèm sổ sức khỏe, quà tặng và dặn dò của bác sĩ.' }
                ]
            }
        ],
        get servicesList() { return this.services; },
        set servicesList(val) { this.services = val; },

        // 6 Bài viết PetShare360 do Admin đăng tải
        articles: [
            {
                id: 1,
                title: 'Cẩm Nang Dinh Dưỡng Vàng Cho Cún Con Từ 2 Đến 6 Tháng Tuổi',
                author: 'ThS.BS Nguyễn Minh Quân (Viện Trưởng PetCare360)',
                date: '18/10/2026',
                category: 'Dinh dưỡng thú cưng',
                views: 2450,
                likes: 318,
                image: 'https://images.unsplash.com/photo-1543466835-00a7907e9de1?auto=format&fit=crop&w=600&q=80',
                summary: 'Giai đoạn 2-6 tháng tuổi là "thời kỳ vàng" để hoàn thiện khung xương, hệ miễn dịch và phát triển não bộ của cún con. Một chế độ ăn sai lầm có thể dẫn đến dị tật xương suốt đời.',
                content: `
                    <p class="lead font-medium text-slate-700">Trong giai đoạn từ 2 đến 6 tháng tuổi, tốc độ phát triển thể chất của cún con diễn ra nhanh gấp 12 lần so với con người. Đây chính là lúc cơ thể bé cần nguồn năng lượng, canxi và kháng thể tối ưu nhất.</p>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">1. Tỷ lệ dinh dưỡng chuẩn cho cún con đang lớn</h4>
                    <p>Khẩu phần ăn của cún con cần đạt hàm lượng protein thô từ 28% - 32% (nguồn protein dễ hấp thu từ thịt gà, cá hồi hoặc trứng gà), chất béo tốt từ 14% - 18% và tỷ lệ Canxi : Photpho lý tưởng là 1.2 : 1.</p>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">2. Số bữa ăn và lượng thức ăn theo từng tháng tuổi</h4>
                    <ul class="list-disc list-inside space-y-1">
                        <li><strong>Từ 2 - 3 tháng tuổi:</strong> Chia làm 4 bữa nhỏ mỗi ngày. Ngâm mềm với sữa dinh dưỡng KMR.</li>
                        <li><strong>Từ 4 - 6 tháng tuổi:</strong> Giảm xuống 3 bữa/ngày, tập cho bé ăn hạt khô nguyên hạt để sạch răng.</li>
                    </ul>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">3. Những thực phẩm TUYỆT ĐỐI CẤM kỵ</h4>
                    <p class="text-rose-600 font-semibold">Sô cô la, hành tỏi, nho tươi/nho khô, xương ống động vật đã nấu chín và chất ngọt nhân tạo Xylitol.</p>
                `
            },
            {
                id: 2,
                title: 'Nhận Biết Dấu Hiệu Trầm Cảm & Căng Thẳng Ở Mèo Nuôi Trong Nhà',
                author: 'BS Trần Thu Hà (Chuyên gia Hành vi Động vật)',
                date: '15/10/2026',
                category: 'Hành vi & Tâm lý',
                views: 1890,
                likes: 245,
                image: 'https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?auto=format&fit=crop&w=600&q=80',
                summary: 'Mèo là bậc thầy giấu giếm cảm xúc và cơn đau. Nếu không chú ý các biểu hiện tinh tế, chủ nuôi có thể bỏ qua tình trạng stress nặng dẫn đến chứng viêm bàng quang vô căn nguy hiểm.',
                content: `
                    <p class="lead font-medium text-slate-700">Nhiều người nghĩ rằng mèo sống trong nhà kín là hoàn toàn an toàn và thoải mái. Tuy nhiên, sự nhàm chán hoặc thiếu không gian vận động theo chiều dọc có thể khiến mèo bị căng thẳng trầm trọng.</p>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">1. Các dấu hiệu cảnh báo mèo đang stress</h4>
                    <ul class="list-disc list-inside space-y-1">
                        <li><strong>Liếm lông quá mức:</strong> Bé liếm đến mức rụng trụi lông ở bụng hoặc mặt trong hai chân sau.</li>
                        <li><strong>Đi vệ sinh ngoài khay:</strong> Tiểu bậy lên giường, ghế sofa hoặc góc tường dù trước đó dùng khay ngoan.</li>
                        <li><strong>Thay đổi thói quen ăn uống:</strong> Bỏ ăn hoặc ăn ít hơn 50% khẩu phần bình thường.</li>
                        <li><strong>Thu mình trốn tránh:</strong> Trốn dưới gầm giường, gừ khè khi vuốt ve.</li>
                    </ul>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">2. Giải pháp giải tỏa căng thẳng hiệu quả</h4>
                    <p>Bổ sung thêm trụ cào móng cây cao cạnh cửa sổ, dành 15-20 phút chơi đùa cần câu lông vũ mỗi ngày và xịt pheromone làm dịu (Feliway).</p>
                `
            },
            {
                id: 3,
                title: 'Lịch Tiêm Phòng Vắc-xin & Tẩy Giun Định Kỳ Chuẩn Y Khoa 2026',
                author: 'ThS.BS Nguyễn Minh Quân (Viện Trưởng PetCare360)',
                date: '12/10/2026',
                category: 'Y tế & Phòng bệnh',
                views: 3120,
                likes: 480,
                image: 'https://images.unsplash.com/photo-1576201836106-db1758fd1c97?auto=format&fit=crop&w=600&q=80',
                summary: 'Tiêm chủng đầy đủ là bức tường thành vững chắc nhất bảo vệ thú cưng trước những dịch bệnh truyền nhiễm nguy hiểm gây tử vong cao như Parvovirus, Care hay Dại.',
                content: `
                    <p class="lead font-medium text-slate-700">Rất nhiều chủ nuôi thắc mắc tại sao cún mèo đã tiêm 1 mũi vẫn bị mắc bệnh. Nguyên nhân chính là do chưa hoàn thành đủ phác đồ mũi tiêm cơ sở để hình thành nồng độ kháng thể bảo hộ.</p>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">1. Lịch tiêm chuẩn cho Chó con</h4>
                    <ul class="list-disc list-inside space-y-1">
                        <li><strong>6 - 8 tuần tuổi:</strong> Mũi 1 - Vắc-xin phòng 5 bệnh.</li>
                        <li><strong>10 - 12 tuần tuổi:</strong> Mũi 2 - Vắc-xin phòng 7 bệnh.</li>
                        <li><strong>14 - 16 tuần tuổi:</strong> Mũi 3 - Vắc-xin 7 bệnh nhắc lại + Vắc-xin Dại (bắt buộc).</li>
                        <li><strong>Định kỳ hàng năm:</strong> Nhắc lại 01 mũi 7 bệnh và 01 mũi Dại mỗi 12 tháng.</li>
                    </ul>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">2. Lịch tiêm chuẩn cho Mèo</h4>
                    <ul class="list-disc list-inside space-y-1">
                        <li><strong>8 tuần tuổi:</strong> Mũi 1 - Vắc-xin 4 bệnh mèo.</li>
                        <li><strong>12 tuần tuổi:</strong> Mũi 2 - Vắc-xin 4 bệnh nhắc lại + Vắc-xin Dại.</li>
                        <li><strong>Định kỳ hàng năm:</strong> Nhắc lại 01 mũi 4 bệnh và 01 mũi Dại.</li>
                    </ul>
                `
            },
            {
                id: 4,
                title: 'Kỹ Thuật Chăm Sóc Lông Chống Vón Cục & Bệnh Nấm Da Vào Mùa Mưa',
                author: 'Master Groomer Lê Thanh Hằng',
                date: '08/10/2026',
                category: 'Spa & Chăm sóc lông',
                views: 1640,
                likes: 198,
                image: 'https://images.unsplash.com/photo-1516734212186-a967f81ad0d7?auto=format&fit=crop&w=600&q=80',
                summary: 'Độ ẩm không khí tăng cao vào mùa mưa là điều kiện thuận lợi nhất để vi nấm và vi khuẩn sinh sôi, gây ngứa ngáy dữ dội và vón rối lông ở các giống chó lông dài như Poodle, Corgi, Samoyed.',
                content: `
                    <p class="lead font-medium text-slate-700">Khi lông bị ẩm ướt kết hợp với bụi bẩn, các sợi lông sẽ bện chặt lại tạo thành các búi lông rối sát da. Dưới lớp búi lông này, da bị bí khí, ẩm mốc và phát sinh nấm da rất nhanh chóng.</p>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">1. Nguyên tắc sấy khô tuyệt đối sau khi dạo mưa</h4>
                    <p>Mỗi khi bé đi dạo dính mưa về, phải lau sạch 4 bàn chân bằng khăn khô và dùng máy sấy ấm sấy kỹ phần đệm chân, bụng và nách. Tuyệt đối không để lông tự khô tự nhiên.</p>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">2. Cách chải lông đúng kỹ thuật</h4>
                    <p>Dùng lược ghim (Slicker Brush) chải từng lớp lông mỏng từ trong chân lông ra ngoài. Dùng xịt gỡ rối chuyên dụng trước khi chải để không làm rách da bé.</p>
                `
            },
            {
                id: 5,
                title: 'Sơ Cứu Khẩn Cấp Tại Nhà Khi Thú Cưng Bị Hóc Dị Vật Hoặc Ngộ Độc',
                author: 'BS Đỗ Hoàng Nam (Đội Trưởng Cấp Cứu 24/7)',
                date: '03/10/2026',
                category: 'Cấp cứu & An toàn',
                views: 2980,
                likes: 512,
                image: 'https://images.unsplash.com/photo-1583337130417-3346a1be7dee?auto=format&fit=crop&w=600&q=80',
                summary: 'Thời gian vàng cứu sống thú cưng khi bị tắc nghẽn đường thở chỉ tính bằng vài phút. Hãy ghi nhớ thủ thuật Heimlich dành riêng cho thú cưng để xử trí kịp thời trước khi đến bệnh viện.',
                content: `
                    <p class="lead font-medium text-slate-700">Thú cưng thường có thói quen gặm nhấm đồ chơi nhỏ, xương hoặc tò mò liếm phải hóa chất lau sàn. Biết cách xử lý sơ cứu tại chỗ sẽ quyết định tính mạng của bé.</p>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">1. Thủ thuật Heimlich khi thú cưng bị hóc dị vật khó thở</h4>
                    <ul class="list-disc list-inside space-y-1">
                        <li><strong>Dành cho cún/mèo nhỏ:</strong> Bế bé dốc đầu xuống 45 độ, dùng lòng bàn tay vỗ dứt khoát 4-5 lần vào giữa hai xương bả vai.</li>
                        <li><strong>Dành cho cún lớn:</strong> Ôm vòng qua eo, nắm một tay thành nắm đấm đặt ngay dưới xương sườn (vùng cơ hoành), ép chặt và giật mạnh hướng lên trên ngực.</li>
                    </ul>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">2. Khi nghi ngờ bé ngộ độc hóa chất</h4>
                    <p class="text-rose-600 font-semibold">GỌI NGAY HOTLINE CẤP CỨU 24/7 (1900 6868). Giữ lại bao bì hóa chất mang theo, KHÔNG tự ý gây nôn nếu bé đã bất tỉnh.</p>
                `
            },
            {
                id: 6,
                title: 'Hướng Dẫn Huấn Luyện Cún Đi Vệ Sinh Đúng Chỗ Trong Vòng 7 Ngày',
                author: 'HLV Huỳnh Anh Tuấn (Trung Tâm Huấn Luyện K9)',
                date: '28/09/2026',
                category: 'Huấn luyện & Kỹ năng',
                views: 2150,
                likes: 367,
                image: 'https://images.unsplash.com/photo-1583511655857-d19b40a7a54e?auto=format&fit=crop&w=600&q=80',
                summary: 'Bí quyết dạy cún đi vệ sinh đúng khay vệ sinh hoặc bồn cầu cực kỳ nhẹ nhàng bằng phương pháp củng cố tích cực (Positive Reinforcement), tuyệt đối không la mắng hay đánh đập.',
                content: `
                    <p class="lead font-medium text-slate-700">Nhiều người có thói quen dí mũi cún vào bãi tiểu khi bé đi sai chỗ để trừng phạt. Hành động này hoàn toàn sai khoa học và chỉ khiến cún sợ hãi, lén lút đi vệ sinh vào góc khuất.</p>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">1. Bắt trúng "khung giờ vàng" đi vệ sinh của cún</h4>
                    <p>Cún có nhu cầu đi vệ sinh vào 3 thời điểm: Ngay sau khi ngủ dậy, trong vòng 15-20 phút sau khi ăn no, và sau khi nô đùa mệt mỏi.</p>
                    <h4 class="font-bold text-slate-800 text-sm mt-3">2. Các bước thực hiện trong 7 ngày</h4>
                    <ul class="list-disc list-inside space-y-1">
                        <li><strong>Bước 1:</strong> Bố trí khay cố định, thấm một chút nước tiểu của bé vào tấm lót tạo mùi quen thuộc.</li>
                        <li><strong>Bước 2:</strong> Vào thời điểm vàng, dẫn cún đến khay với khẩu lệnh ngắn ("Đi tè đi").</li>
                        <li><strong>Bước 3:</strong> Khen thưởng tức thì! Thưởng ngay 1 viên bánh thưởng thơm ngon khi bé đi đúng chỗ.</li>
                    </ul>
                `
            }
        ],
        get petshareArticles() { return this.articles; },
        set petshareArticles(val) { this.articles = val; },

        // 5 Câu hỏi FAQ chi tiết
        faqs: [
            {
                q: 'Quy trình đặt lịch dịch vụ tại PetCare360 diễn ra như thế nào và tôi có thể hủy hoặc đổi giờ hẹn không?',
                question: 'Quy trình đặt lịch dịch vụ tại PetCare360 diễn ra như thế nào và tôi có thể hủy hoặc đổi giờ hẹn không?',
                a: 'Quý khách có thể dễ dàng đặt lịch trực tuyến ngay trên WebApp PetCare360: chọn dịch vụ mong muốn, chọn bé cưng, ngày và khung giờ thuận tiện. Hệ thống sẽ lập tức gửi xác nhận qua SMS và phân bổ phòng dịch vụ vô khuẩn cùng bác sĩ chuyên trách. Trong trường hợp có việc bận đột xuất, quý khách hoàn toàn có thể đổi giờ hoặc hủy lịch hẹn trước ít nhất 02 giờ mà không mất bất kỳ chi phí nào.',
                answer: 'Quý khách có thể dễ dàng đặt lịch trực tuyến ngay trên WebApp PetCare360: chọn dịch vụ mong muốn, chọn bé cưng, ngày và khung giờ thuận tiện. Hệ thống sẽ lập tức gửi xác nhận qua SMS và phân bổ phòng dịch vụ vô khuẩn cùng bác sĩ chuyên trách. Trong trường hợp có việc bận đột xuất, quý khách hoàn toàn có thể đổi giờ hoặc hủy lịch hẹn trước ít nhất 02 giờ mà không mất bất kỳ chi phí nào.'
            },
            {
                q: 'Các bé cưng có biểu hiện hung dữ hoặc quá sợ hãi thì PetCare360 có nhận dịch vụ Spa và khám chữa bệnh không?',
                question: 'Các bé cưng có biểu hiện hung dữ hoặc quá sợ hãi thì PetCare360 có nhận dịch vụ Spa và khám chữa bệnh không?',
                a: 'PetCare360 hoàn toàn có năng lực tiếp nhận các bé có tâm lý nhạy cảm, sợ hãi hoặc phòng thủ cao. Đội ngũ bác sĩ và chuyên viên Spa tại PetCare360 đều được đào tạo bài bản chứng chỉ Fear Free quốc tế (chăm sóc không sang chấn tâm lý). Chúng tôi áp dụng kỹ thuật xoa bóp trấn an, sử dụng pheromone làm dịu và bánh thưởng chuyên dụng. Trong trường hợp bắt buộc phải can thiệp y tế khẩn cấp, bác sĩ sẽ tư vấn tiền mê nhẹ an toàn để bé không phải trải qua hoảng loạn.',
                answer: 'PetCare360 hoàn toàn có năng lực tiếp nhận các bé có tâm lý nhạy cảm, sợ hãi hoặc phòng thủ cao. Đội ngũ bác sĩ và chuyên viên Spa tại PetCare360 đều được đào tạo bài bản chứng chỉ Fear Free quốc tế (chăm sóc không sang chấn tâm lý). Chúng tôi áp dụng kỹ thuật xoa bóp trấn an, sử dụng pheromone làm dịu và bánh thưởng chuyên dụng. Trong trường hợp bắt buộc phải can thiệp y tế khẩn cấp, bác sĩ sẽ tư vấn tiền mê nhẹ an toàn để bé không phải trải qua hoảng loạn.'
            },
            {
                q: 'Chính sách bảo hành y tế và cam kết an toàn khi gửi thú cưng tại khách sạn Pet Hotel như thế nào?',
                question: 'Chính sách bảo hành y tế và cam kết an toàn khi gửi thú cưng tại khách sạn Pet Hotel như thế nào?',
                a: 'Mọi thú cưng khi lưu trú tại Pet Hotel đều được kiểm tra sức khỏe ban đầu miễn phí, ở phòng riêng biệt có điều hòa 24/7 và camera giám sát trực tiếp. PetCare360 cam kết bảo hiểm sức khỏe 100% trong suốt thời gian lưu trú: nếu bé có bất kỳ dấu hiệu bỏ ăn hay mệt mỏi, bác sĩ thú y sẽ thăm khám và chăm sóc ngay lập tức với sự đồng ý của phụ huynh mà không phát sinh phụ phí khám.',
                answer: 'Mọi thú cưng khi lưu trú tại Pet Hotel đều được kiểm tra sức khỏe ban đầu miễn phí, ở phòng riêng biệt có điều hòa 24/7 và camera giám sát trực tiếp. PetCare360 cam kết bảo hiểm sức khỏe 100% trong suốt thời gian lưu trú: nếu bé có bất kỳ dấu hiệu bỏ ăn hay mệt mỏi, bác sĩ thú y sẽ thăm khám và chăm sóc ngay lập tức với sự đồng ý của phụ huynh mà không phát sinh phụ phí khám.'
            },
            {
                q: 'Sản phẩm thức ăn và thuốc thú y trên hệ thống PetCare360 có đảm bảo chính hãng và nguồn gốc rõ ràng không?',
                question: 'Sản phẩm thức ăn và thuốc thú y trên hệ thống PetCare360 có đảm bảo chính hãng và nguồn gốc rõ ràng không?',
                a: '100% sản phẩm trên PetCare360 (từ hạt khô, pate dinh dưỡng đến thuốc thú y đặc trị) đều được nhập khẩu chính ngạch từ các tập đoàn thú y hàng đầu thế giới như Royal Canin (Pháp), Orijen (Canada), Zoetis (Mỹ), Boehringer Ingelheim (Đức). Mỗi sản phẩm đều có đầy đủ hóa đơn VAT, tem phụ tiếng Việt, mã vạch truy xuất nguồn gốc và hạn sử dụng dài hạn. Chúng tôi cam kết đền bù gấp 10 lần nếu phát hiện hàng giả, hàng nhái.',
                answer: '100% sản phẩm trên PetCare360 (từ hạt khô, pate dinh dưỡng đến thuốc thú y đặc trị) đều được nhập khẩu chính ngạch từ các tập đoàn thú y hàng đầu thế giới như Royal Canin (Pháp), Orijen (Canada), Zoetis (Mỹ), Boehringer Ingelheim (Đức). Mỗi sản phẩm đều có đầy đủ hóa đơn VAT, tem phụ tiếng Việt, mã vạch truy xuất nguồn gốc và hạn sử dụng dài hạn. Chúng tôi cam kết đền bù gấp 10 lần nếu phát hiện hàng giả, hàng nhái.'
            },
            {
                q: 'Tôi ở xa hoặc vào ban đêm khi phòng khám đóng cửa, nếu thú cưng gặp tình trạng khẩn cấp thì phải làm sao?',
                question: 'Tôi ở xa hoặc vào ban đêm khi phòng khám đóng cửa, nếu thú cưng gặp tình trạng khẩn cấp thì phải làm sao?',
                a: 'PetCare360 duy trì hệ thống Cấp cứu Thú y 24/7/365 và tổng đài Bác sĩ trực tuyến miễn phí (1900 6868). Quý khách chỉ cần nhấn nút "Chat" trên góc phải màn hình WebApp hoặc gọi hotline cấp cứu, bác sĩ chuyên khoa hồi sức sẽ hướng dẫn sơ cứu tức thì qua video call và điều động xe cứu thương Pet Ambulance chuyên dụng đến tận nơi đón bé trong vòng 15-30 phút.',
                answer: 'PetCare360 duy trì hệ thống Cấp cứu Thú y 24/7/365 và tổng đài Bác sĩ trực tuyến miễn phí (1900 6868). Quý khách chỉ cần nhấn nút "Chat" trên góc phải màn hình WebApp hoặc gọi hotline cấp cứu, bác sĩ chuyên khoa hồi sức sẽ hướng dẫn sơ cứu tức thì qua video call và điều động xe cứu thương Pet Ambulance chuyên dụng đến tận nơi đón bé trong vòng 15-30 phút.'
            }
        ],
        faqActive: 0,
        get faqList() { return this.faqs; },
        set faqList(val) { this.faqs = val; },

        // 8 Lịch hẹn Admin phong phú
        appointments: [
            {
                id: 'APT-1089',
                customerName: 'Nguyễn Phương Thảo',
                customerPhone: '0988 123 456',
                petName: 'Bơ (Butter)',
                petType: 'Cún Corgi',
                serviceName: 'Gói Spa & Grooming Cắt Tỉa Lông Tạo Kiểu Toàn Diện',
                date: '2026-10-21',
                time: '09:30',
                branch: 'Chi nhánh Quận 7',
                status: 'Đã đặt hẹn',
                notes: 'Bé sợ tiếng sấy to, cần vệ sinh kẽ ngón chân cẩn thận do vừa mới khỏi viêm da.'
            },
            {
                id: 'APT-1088',
                customerName: 'Trần Văn Hoàng',
                customerPhone: '0912 345 678',
                petName: 'Kem Mút',
                petType: 'Mèo ALN',
                serviceName: 'Khám Sức Khỏe Tổng Quát & Tầm Soát Bệnh Lý Thú Cưng',
                date: '2026-10-21',
                time: '10:30',
                branch: 'Chi nhánh Cầu Giấy',
                status: 'Đang tiếp khách',
                notes: 'Bé có dấu hiệu uống nhiều nước hơn bình thường, nhờ bác sĩ kiểm tra chức năng thận.'
            },
            {
                id: 'APT-1087',
                customerName: 'Lê Thị Mai',
                customerPhone: '0977 888 999',
                petName: 'Lu Lu',
                petType: 'Cún Poodle',
                serviceName: 'Tiêm Chủng Vắc-xin Phòng Bệnh Đa Giá Nhập Khẩu',
                date: '2026-10-20',
                time: '14:00',
                branch: 'Chi nhánh Bình Thạnh',
                status: 'Hoàn thành',
                notes: 'Tiêm mũi nhắc lại hàng năm, kiểm tra mắt có ghèn.'
            },
            {
                id: 'APT-1086',
                customerName: 'Phạm Quốc Bảo',
                customerPhone: '0903 555 777',
                petName: 'Miu Miu',
                petType: 'Mèo Ba Tư',
                serviceName: 'Lấy Cao Răng Siêu Âm Không Đau & Đánh Bóng Men Răng',
                date: '2026-10-20',
                time: '16:00',
                branch: 'Chi nhánh Quận 7',
                status: 'Đã đặt hẹn',
                notes: 'Bé khó tính khi đụng vào miệng, cần tiền mê nhẹ an toàn.'
            },
            {
                id: 'APT-1085',
                customerName: 'Đặng Tuấn Anh',
                customerPhone: '0933 222 111',
                petName: 'Rocky',
                petType: 'Chó Golden',
                serviceName: 'Cấp Cứu Thú Y 24/7 & Hồi Sức Tích Cực (ICU)',
                date: '2026-10-20',
                time: '21:15',
                branch: 'Chi nhánh Quận 1',
                status: 'Hoàn thành',
                notes: 'Bé bị sốc nhiệt sau khi chạy bộ, đã hạ sốt và truyền dịch ổn định.'
            },
            {
                id: 'APT-1084',
                customerName: 'Hoàng Minh Đức',
                customerPhone: '0903 111 222',
                petName: 'Bông Lan',
                petType: 'Mèo Xiêm',
                serviceName: 'Khách Sạn Thú Cưng Pet Hotel Đẳng Cấp 5 Sao',
                date: '2026-10-22',
                time: '08:00',
                branch: 'Chi nhánh Quận 7',
                status: 'Đã đặt hẹn',
                notes: 'Gửi bé 3 ngày, cho ăn pate Ciao vị cá ngừ mỗi tối, gửi clip camera hàng ngày.'
            },
            {
                id: 'APT-1083',
                customerName: 'Vũ Thùy Linh',
                customerPhone: '0944 666 888',
                petName: 'Milu',
                petType: 'Chó Pug',
                serviceName: 'Tắm Trị Liệu Trị Nấm & Viêm Da Chuyên Sâu',
                date: '2026-10-19',
                time: '15:00',
                branch: 'Chi nhánh Bình Thạnh',
                status: 'Hoàn thành',
                notes: 'Vùng nách và nếp gấp mặt bị đỏ ngứa, dùng dầu tắm Davis 4%.'
            },
            {
                id: 'APT-1082',
                customerName: 'Đỗ Thị Hạnh',
                customerPhone: '0918 999 123',
                petName: 'Lucky',
                petType: 'Chó Samoyed',
                serviceName: 'Đưa Đón Thú Cưng Khám Bệnh & Spa (Pet Taxi)',
                date: '2026-10-19',
                time: '08:30',
                branch: 'Chi nhánh Quận 1',
                status: 'Hủy hẹn',
                notes: 'Khách bận công tác đột xuất, đã hẹn dời sang tuần sau.'
            }
        ],

        // 8 Đơn hàng Admin
        orders: [
            {
                id: 'ORD-8821',
                customer: 'Nguyễn Phương Thảo',
                date: '2026-10-20',
                items: 'Royal Canin Mini Adult (1kg), Sữa tắm Davis 4%',
                total: 700000,
                totalAmount: 700000,
                paymentMethod: 'Chuyển khoản VietQR',
                status: 'Đã thanh toán',
                branch: 'Q7'
            },
            {
                id: 'ORD-8820',
                customer: 'Hoàng Minh Đức',
                date: '2026-10-20',
                items: 'Orijen Original (2kg), Pate Ciao Churu (gói 20 thanh)',
                total: 1105000,
                totalAmount: 1105000,
                paymentMethod: 'Ví MoMo',
                status: 'Đang vận chuyển',
                branch: 'HN'
            },
            {
                id: 'ORD-8819',
                customer: 'Vũ Thùy Linh',
                date: '2026-10-19',
                items: 'Cát Đậu Nành Cature 6L (x2), Balo Phi Thuyền VIP',
                total: 820000,
                totalAmount: 820000,
                paymentMethod: 'COD khi nhận hàng',
                status: 'Hoàn thành',
                branch: 'BT'
            },
            {
                id: 'ORD-8818',
                customer: 'Trần Văn Hoàng',
                date: '2026-10-19',
                items: 'Viên nhai NexGard Spectra, Hạt Royal Canin Kitten',
                total: 855000,
                totalAmount: 855000,
                paymentMethod: 'Chuyển khoản VietQR',
                status: 'Đã thanh toán',
                branch: 'Q1'
            },
            {
                id: 'ORD-8817',
                customer: 'Lê Thị Mai',
                date: '2026-10-18',
                items: 'Trụ Cào Móng Cat Tree 3 Tầng, Pate Ciao Churu',
                total: 895000,
                totalAmount: 895000,
                paymentMethod: 'Ví MoMo',
                status: 'Hoàn thành',
                branch: 'Q7'
            },
            {
                id: 'ORD-8816',
                customer: 'Phạm Quốc Bảo',
                date: '2026-10-18',
                items: 'Tuýp nhỏ gáy Revolution Plus, Gel dinh dưỡng Virbac',
                total: 680000,
                totalAmount: 680000,
                paymentMethod: 'COD khi nhận hàng',
                status: 'Hoàn thành',
                branch: 'BT'
            },
            {
                id: 'ORD-8815',
                customer: 'Đặng Tuấn Anh',
                date: '2026-10-17',
                items: 'Combo 12 Lon Pate Monge, Cát Cature 6L',
                total: 585000,
                totalAmount: 585000,
                paymentMethod: 'Chuyển khoản VietQR',
                status: 'Hoàn thành',
                branch: 'Q1'
            },
            {
                id: 'ORD-8814',
                customer: 'Đỗ Thị Hạnh',
                date: '2026-10-17',
                items: 'Thức Ăn Hạt Orijen Original (2kg)',
                total: 890000,
                totalAmount: 890000,
                paymentMethod: 'Ví VNPay',
                status: 'Đang vận chuyển',
                branch: 'Q7'
            }
        ],

        // 6 Khách hàng Admin với cột Thú Cưng Đang Nuôi chi tiết
        customers: [
            {
                id: 1,
                name: 'Nguyễn Phương Thảo',
                phone: '0988 123 456',
                email: 'phuongthao.petcare@gmail.com',
                tier: 'Thành viên Vàng',
                petCount: 3,
                pets: 'Bơ (Corgi), Mochi (Mèo ALN), Đậu Đậu (Poodle)',
                petsList: [
                    { name: 'Bơ', breed: 'Corgi', type: 'Chó' },
                    { name: 'Mochi', breed: 'Mèo ALN', type: 'Mèo' },
                    { name: 'Đậu Đậu', breed: 'Poodle', type: 'Chó' }
                ],
                spent: 18500000,
                totalSpent: 18500000,
                points: 3450,
                avatar: 'https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=300&q=80',
                createdAt: '15/01/2025'
            },
            {
                id: 2,
                name: 'Hoàng Minh Đức',
                phone: '0903 111 222',
                email: 'minhduc.dev@gmail.com',
                tier: 'Thành viên Kim Cương',
                petCount: 2,
                pets: 'Bông Lan (Mèo Xiêm), Sushi (Chó Shiba)',
                petsList: [
                    { name: 'Bông Lan', breed: 'Mèo Xiêm', type: 'Mèo' },
                    { name: 'Sushi', breed: 'Shiba Inu', type: 'Chó' }
                ],
                spent: 32400000,
                totalSpent: 32400000,
                points: 8200,
                avatar: 'https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=300&q=80',
                createdAt: '10/08/2024'
            },
            {
                id: 3,
                name: 'Lê Thị Mai',
                phone: '0977 888 999',
                email: 'maile.design@gmail.com',
                tier: 'Thành viên Bạc',
                petCount: 1,
                pets: 'Lu Lu (Poodle)',
                petsList: [
                    { name: 'Lu Lu', breed: 'Poodle', type: 'Chó' }
                ],
                spent: 4500000,
                totalSpent: 4500000,
                points: 1250,
                avatar: 'https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=300&q=80',
                createdAt: '05/06/2025'
            },
            {
                id: 4,
                name: 'Trần Văn Hoàng',
                phone: '0912 345 678',
                email: 'hoang.tran@gmail.com',
                tier: 'Thành viên Vàng',
                petCount: 2,
                pets: 'Kem Mút (Mèo ALN), Milo (Pug)',
                petsList: [
                    { name: 'Kem Mút', breed: 'Mèo ALN', type: 'Mèo' },
                    { name: 'Milo', breed: 'Pug', type: 'Chó' }
                ],
                spent: 14800000,
                totalSpent: 14800000,
                points: 2900,
                avatar: 'https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=300&q=80',
                createdAt: '12/11/2024'
            },
            {
                id: 5,
                name: 'Phạm Quốc Bảo',
                phone: '0903 555 777',
                email: 'bao.pham@vietin.vn',
                tier: 'Thành viên Bạc',
                petCount: 1,
                pets: 'Miu Miu (Mèo Ba Tư)',
                petsList: [
                    { name: 'Miu Miu', breed: 'Mèo Ba Tư', type: 'Mèo' }
                ],
                spent: 6200000,
                totalSpent: 6200000,
                points: 1540,
                avatar: 'https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=300&q=80',
                createdAt: '22/02/2025'
            },
            {
                id: 6,
                name: 'Đặng Tuấn Anh',
                phone: '0933 222 111',
                email: 'tuananh.dang@gmail.com',
                tier: 'Thành viên Kim Cương',
                petCount: 2,
                pets: 'Rocky (Golden Retriever), Tom (Mèo Mướp)',
                petsList: [
                    { name: 'Rocky', breed: 'Golden', type: 'Chó' },
                    { name: 'Tom', breed: 'Mèo Mướp', type: 'Mèo' }
                ],
                spent: 28900000,
                totalSpent: 28900000,
                points: 7450,
                avatar: 'https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=300&q=80',
                createdAt: '18/09/2024'
            }
        ],

        // MOCK DATA 6 THÁNG GẦN NHẤT CHO BIỂU ĐỒ DOANH THU (TRIỆU VNĐ)
        revenueMonthlyMock: [
            { month: 'Tháng 5', ecommerceRevenue: 135000000, serviceRevenue: 152000000 },
            { month: 'Tháng 6', ecommerceRevenue: 148000000, serviceRevenue: 168000000 },
            { month: 'Tháng 7', ecommerceRevenue: 162000000, serviceRevenue: 185000000 },
            { month: 'Tháng 8', ecommerceRevenue: 175000000, serviceRevenue: 198000000 },
            { month: 'Tháng 9', ecommerceRevenue: 190000000, serviceRevenue: 220000000 },
            { month: 'Tháng 10', ecommerceRevenue: 215000000, serviceRevenue: 245000000 }
        ],

        // Doanh thu chi tiết theo ngành hàng
        analyticsRevenueCommerce: [
            { category: 'Thức ăn hạt khô', revenue: 145000000, share: 42, growth: '+18.5%' },
            { category: 'Pate & Treats dinh dưỡng', revenue: 68000000, share: 20, growth: '+24.2%' },
            { category: 'Thuốc & Y tế đặc trị', revenue: 55000000, share: 16, growth: '+12.0%' },
            { category: 'Vệ sinh & Cát đậu nành', revenue: 42000000, share: 12, growth: '+8.4%' },
            { category: 'Phụ kiện & Balo đồ chơi', revenue: 35000000, share: 10, growth: '+15.1%' }
        ],
        analyticsRevenueService: [
            { category: 'Spa & Cắt tỉa Grooming', revenue: 168000000, share: 45, growth: '+28.4%' },
            { category: 'Khám chữa bệnh & Nội trú', revenue: 95000000, share: 25, growth: '+14.2%' },
            { category: 'Khách sạn thú cưng Pet Hotel', revenue: 52000000, share: 14, growth: '+35.0%' },
            { category: 'Tiêm chủng & Phòng dịch', revenue: 38000000, share: 10, growth: '+9.8%' },
            { category: 'Cấp cứu 24/7 & Xe đưa đón', revenue: 22000000, share: 6, growth: '+19.6%' }
        ],

        // Giỏ hàng & Booking flow
        cart: [],
        bookingItem: null,
        prodModalQty: 1,

        // Form thêm thú cưng mới (Có hỗ trợ tải ảnh và xác thực đỏ)
        newPetData: {
            name: '',
            type: 'Chó',
            breed: '',
            gender: 'Đực',
            age: '',
            weight: '',
            avatar: '',
            appearance: '',
            allergies: '',
            diet: '',
            habits: '',
            personality: '',
            ownerName: 'Nguyễn Phương Thảo',
            ownerPhone: '0988 123 456',
            ownerAddress: 'Căn hộ 12.04 Tòa Park 6, Vinhomes Central Park, Bình Thạnh, TP.HCM',
            ownerEmergency: '0912 345 678 (Chồng)'
        },

        newProdForm: {
            sku: '',
            name: '',
            brand: '',
            price: null,
            stockQ1: 20,
            stockBT: 15,
            stockQ7: 25,
            category: 'Thức ăn & Dinh dưỡng',
            img: 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=500&q=80',
            desc: ''
        },

        restockForm: {
            productId: '',
            branch: 'Q1',
            quantity: 50,
            costPrice: null,
            supplier: '',
            notes: ''
        },

        checkoutForm: {
            name: 'Nguyễn Phương Thảo',
            phone: '0988 123 456',
            address: 'Căn hộ 12.04 Tòa Park 6, Vinhomes Central Park, Bình Thạnh, TP.HCM',
            paymentMethod: 'vietqr'
        },

        // Live Chat Box
        chatMessages: [
            {
                sender: 'bot',
                text: 'Xin chào quý khách! Bác sĩ thú y và Đội ngũ CSKH PetCare360 rất hân hạnh được đồng hành cùng bạn và bé cưng. Bạn đang cần hỗ trợ dịch vụ nào ạ?',
                time: 'Vừa xong'
            }
        ],
        newChatMessage: '',

        // COMPUTED & GETTERS
        get cartItemsCount() {
            return this.cart.reduce((sum, item) => sum + (item.qty || 1), 0);
        },

        get cartTotal() {
            return this.cart.reduce((sum, item) => sum + (item.price * (item.qty || 1)), 0);
        },

        // Lọc sản phẩm theo 3 danh mục chính xác
        get filteredProducts() {
            return this.products.filter(p => {
                const cat = this.filterCategory || 'all';
                const matchCat = (cat === 'all') || (p.category === cat);
                const query = (this.searchQuery || this.productSearchQuery || '').toLowerCase().trim();
                const matchSearch = !query || p.name.toLowerCase().includes(query) || (p.brand && p.brand.toLowerCase().includes(query));
                return matchCat && matchSearch;
            });
        },

        // Lọc dịch vụ theo 4 danh mục chính xác
        get filteredServices() {
            return this.services.filter(s => {
                const cat = this.filterServiceCategory || 'all';
                const matchCat = (cat === 'all') || (s.category === cat);
                const query = (this.serviceSearchQuery || this.searchQuery || '').toLowerCase().trim();
                const matchSearch = !query || s.name.toLowerCase().includes(query) || (s.desc && s.desc.toLowerCase().includes(query));
                return matchCat && matchSearch;
            });
        },

        get filteredArticles() {
            return this.articles.filter(art => {
                const cat = (this.filterArticleCat || 'all');
                const matchCat = cat === 'all' || art.category.toLowerCase().includes(cat.toLowerCase());
                const query = (this.searchArticleQuery || this.searchQuery || '').toLowerCase();
                const matchSearch = !query || art.title.toLowerCase().includes(query) || art.summary.toLowerCase().includes(query);
                return matchCat && matchSearch;
            });
        },

        get filteredAppointments() {
            return this.appointments.filter(apt => {
                const q = (this.appointmentSearchQuery || '').toLowerCase();
                const matchQ = !q || apt.customerName.toLowerCase().includes(q) || apt.petName.toLowerCase().includes(q) || apt.id.toLowerCase().includes(q);
                const matchServ = (this.appointmentServiceFilter || 'all') === 'all' || apt.serviceName.includes(this.appointmentServiceFilter);
                const matchBranch = (this.globalBranch || 'all') === 'all' || apt.branch.includes(this.getBranchLabel(this.globalBranch));
                return matchQ && matchServ && matchBranch;
            });
        },

        get filteredAdminOrders() {
            return this.orders.filter(ord => {
                const q = (this.orderSearchQuery || '').toLowerCase();
                const matchQ = !q || ord.customer.toLowerCase().includes(q) || ord.id.toLowerCase().includes(q);
                const matchStatus = (this.orderStatusFilter || 'all') === 'all' || ord.status === this.orderStatusFilter;
                const matchBranch = (this.globalBranch || 'all') === 'all' || (ord.branch === this.globalBranch);
                return matchQ && matchStatus && matchBranch;
            });
        },

        get filteredOrdersByBranch() {
            return this.filteredAdminOrders;
        },

        get filteredProductsInventory() {
            return this.products.filter(p => {
                const q = (this.productSearchQuery || '').toLowerCase();
                const matchQ = !q || p.name.toLowerCase().includes(q) || p.sku.toLowerCase().includes(q);
                const totalStock = this.getSafeTotalStock(p);
                const matchLow = !this.showLowStockOnly || totalStock <= 10;
                return matchQ && matchLow;
            });
        },

        get filteredAdminPets() {
            return this.pets.filter(p => {
                const q = (this.petSearchQuery || '').toLowerCase();
                return !q || p.name.toLowerCase().includes(q) || p.breed.toLowerCase().includes(q) || (p.chipId && p.chipId.includes(q)) || (p.ownerName && p.ownerName.toLowerCase().includes(q));
            });
        },

        get filteredAdminCustomers() {
            return this.customers.filter(c => {
                const q = (this.customerSearchQuery || '').toLowerCase();
                return !q || c.name.toLowerCase().includes(q) || c.phone.includes(q) || c.email.toLowerCase().includes(q) || (c.pets && c.pets.toLowerCase().includes(q));
            });
        },

        // TÍNH TOÁN AN TOÀN TRÁNH NaN DOANH THU
        get unreadNotificationsCount() {
            return (this.adminNotifications || []).filter(n => !n.read).length;
        },

        get totalEcommerceRevenue() {
            const list = this.revenueMonthlyMock || [];
            return list.reduce((sum, item) => sum + (Number(item.ecommerceRevenue) || 0), 0);
        },

        get totalServiceRevenue() {
            const list = this.revenueMonthlyMock || [];
            return list.reduce((sum, item) => sum + (Number(item.serviceRevenue) || 0), 0);
        },

        get totalRevenueFiltered() {
            if (this.adminTimeFilter === 'today') return 18500000;
            if (this.adminTimeFilter === '7days') return 112000000;
            if (this.adminTimeFilter === 'month') return 460000000;
            if (this.adminTimeFilter === 'quarter') return 1380000000;
            return this.totalEcommerceRevenue + this.totalServiceRevenue;
        },

        get pendingOrdersCount() {
            return this.orders.filter(o => o.status !== 'Hoàn thành').length;
        },

        get inProgressAppointmentsCount() {
            return this.appointments.filter(a => a.status === 'Đang tiếp khách' || a.status === 'Đã đặt hẹn').length;
        },

        get lowStockCount() {
            return this.products.filter(p => this.getSafeTotalStock(p) <= 10).length;
        },

        get urgentTasksCount() {
            return this.pendingOrdersCount + this.inProgressAppointmentsCount;
        },

        // Helper tính tổng tồn kho an toàn tuyệt đối tránh NaN
        getSafeTotalStock(p) {
            const q1 = Number(p.stockQ1 !== undefined ? p.stockQ1 : (p.q1 !== undefined ? p.q1 : 0)) || 0;
            const bt = Number(p.stockBT !== undefined ? p.stockBT : (p.bt !== undefined ? p.bt : 0)) || 0;
            const q7 = Number(p.stockQ7 !== undefined ? p.stockQ7 : (p.q7 !== undefined ? p.q7 : 0)) || 0;
            return q1 + bt + q7;
        },

        // Helper label formatters
        formatCurrency(amount) {
            const num = Number(amount);
            if (isNaN(num) || (!num && num !== 0)) return '0 đ';
            return new Intl.NumberFormat('vi-VN', { style: 'currency', currency: 'VND' }).format(num);
        },

        formatMoney(amount) {
            return this.formatCurrency(amount);
        },

        getBranchLabel(code) {
            if (code === 'HN' || code === 'Q1') return 'Quận 1';
            if (code === 'Q7') return 'Quận 7';
            if (code === 'BT') return 'Bình Thạnh';
            return 'Toàn Hệ Thống';
        },

        getTimeFilterLabel(code) {
            if (code === 'today') return 'Hôm nay';
            if (code === '7days') return '7 ngày qua';
            if (code === 'month') return 'Tháng này';
            if (code === 'quarter') return 'Quý này';
            return 'Toàn bộ thời gian';
        },

        formatAppointmentStatus(status) {
            return status || 'Đã đặt hẹn';
        },

        formatOrderStatusLabel(status) {
            return status || 'Đã ghi nhận';
        },

        // Khởi tạo app & vẽ biểu đồ doanh thu Chart.js
        initApp() {
            console.log('PetCare360 Unified SuperApp Initialized!');
            if (window.lucide) {
                window.lucide.createIcons();
            }
            this.$nextTick(() => {
                this.renderRevenueChart();
            });
        },

        // VẼ BIỂU ĐỒ DOANH THU 6 THÁNG GẦN NHẤT BẰNG CHART.JS
        renderRevenueChart() {
            const canvas = document.getElementById('revenueChart');
            if (!canvas) return;

            // Xóa instance cũ nếu tồn tại
            if (window.petcareRevenueChartInstance) {
                window.petcareRevenueChartInstance.destroy();
                window.petcareRevenueChartInstance = null;
            }

            const data = this.revenueMonthlyMock || [];
            if (data.length === 0) return;

            const labels = data.map(d => d.month);
            // Quy đổi sang Triệu VNĐ: Math.round(revenue / 1000000)
            const ecomData = data.map(d => Math.round((Number(d.ecommerceRevenue) || 0) / 1000000));
            const servData = data.map(d => Math.round((Number(d.serviceRevenue) || 0) / 1000000));

            const ctx = canvas.getContext('2d');
            window.petcareRevenueChartInstance = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: labels,
                    datasets: [
                        {
                            label: 'Sản phẩm E-Commerce (Triệu VNĐ)',
                            data: ecomData,
                            backgroundColor: '#0d9488', // teal-600
                            borderColor: '#0f766e',
                            borderWidth: 1,
                            borderRadius: 6
                        },
                        {
                            label: 'Dịch vụ Y tế & Spa (Triệu VNĐ)',
                            data: servData,
                            backgroundColor: '#6366f1', // indigo-500
                            borderColor: '#4f46e5',
                            borderWidth: 1,
                            borderRadius: 6
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            position: 'top',
                            labels: {
                                boxWidth: 14,
                                font: { size: 12, weight: 'bold' }
                            }
                        },
                        tooltip: {
                            callbacks: {
                                label: function(context) {
                                    return context.dataset.label + ': ' + context.parsed.y + ' Triệu VNĐ';
                                }
                            }
                        }
                    },
                    scales: {
                        x: {
                            grid: { display: false },
                            ticks: { font: { size: 11, weight: 'bold' } }
                        },
                        y: {
                            beginAtZero: true,
                            title: {
                                display: true,
                                text: 'Doanh thu (Triệu VNĐ)',
                                font: { size: 11, weight: 'bold' }
                            },
                            ticks: {
                                callback: function(value) {
                                    return value + ' tr';
                                }
                            }
                        }
                    }
                }
            });
        },

        // Điều hướng & Auth
        openLoginModal() {
            this.loginUsername = '';
            this.loginPassword = '';
            this.loginError = '';
            this.showLoginModal = true;
            this.loginModalOpen = true;
        },

        handleLogin() {
            const user = (this.loginUsername || '').trim();
            const pass = (this.loginPassword || '').trim();

            if (!user || !pass) {
                this.loginError = 'Tên đăng nhập hoặc mật khẩu không đúng.';
                return;
            }

            if (user === 'teamnhonho' && pass === 'noletdtu$2006') {
                this.isLoggedIn = true;
                this.currentRole = 'admin';
                this.activeAdminTab = 'dashboard';
                this.showLoginModal = false;
                this.loginModalOpen = false;
                this.loginError = '';
                alert('Đăng nhập thành công với quyền Quản Trị Viên (Admin PetCare360)!');
                this.$nextTick(() => {
                    this.renderRevenueChart();
                });
            } else {
                this.isLoggedIn = true;
                this.currentRole = 'customer';
                this.showLoginModal = false;
                this.loginModalOpen = false;
                this.loginError = '';
                alert('Đăng nhập thành công tài khoản Khách Hàng: ' + user + '!');
            }
        },

        logout() {
            this.isLoggedIn = false;
            this.currentRole = 'customer';
            this.activeCustomerTab = 'home';
            alert('Bạn đã đăng xuất tài khoản thành công.');
        },

        handleLogout() {
            this.logout();
        },

        switchAdminTab(tab) {
            this.activeAdminTab = tab;
            if (tab === 'dashboard' || tab === 'analytics') {
                this.$nextTick(() => {
                    this.renderRevenueChart();
                });
            }
        },

        applyTimeFilter(period) {
            this.adminTimeFilter = period;
            alert('Đã cập nhật bộ lọc thời gian: ' + this.getTimeFilterLabel(period));
            this.$nextTick(() => {
                this.renderRevenueChart();
            });
        },

        // Quản lý thông báo Admin
        toggleAdminNotifications() {
            this.showAdminNotifications = !this.showAdminNotifications;
        },

        markNotificationRead(id) {
            const notif = (this.adminNotifications || []).find(n => n.id === id);
            if (notif) notif.read = true;
        },

        markAllNotificationsRead() {
            this.adminNotifications.forEach(n => n.read = true);
            alert('Đã đánh dấu đọc tất cả thông báo!');
        },

        // Modal triggers
        openProductDetail(product) {
            this.selectedProductModal = product;
            this.prodModalQty = 1;
        },

        openServiceDetail(service) {
            this.selectedServiceModal = service;
        },

        openArticleDetail(article) {
            this.selectedArticleModal = article;
        },

        openPetHealthModal(pet) {
            this.selectedPetHealthModal = pet;
        },

        openPolicyModal(type) {
            this.showLegalModal = true;
            this.policyModalOpen = true;
        },

        openAddProductModal() {
            this.showAddProductModal = true;
            this.addProductModalOpen = true;
        },

        openRestockModal(product) {
            this.showRestockModal = true;
            this.restockModalOpen = true;
            if (product) {
                this.restockForm.productId = product.id;
            }
        },

        openCustomerSupportChat() {
            this.showChatModal = true;
            this.chatModalOpen = true;
        },

        openChatWithCustomer(customerName) {
            this.showChatModal = true;
            this.chatModalOpen = true;
        },

        openNewAppointmentModal() {
            alert('Để tạo lịch hẹn mới cho khách, vui lòng chọn dịch vụ trong danh mục Dịch Vụ.');
            this.activeCustomerTab = 'booking';
        },

        openOrderDetail(order) {
            this.selectedOrder = order;
            this.orderDrawerOpen = true;
        },

        // Thao tác giỏ hàng & Đặt lịch
        addToCart(product, qty = 1) {
            const existing = this.cart.find(item => item.id === product.id && !item.isService);
            if (existing) {
                existing.qty += qty;
            } else {
                this.cart.push({
                    id: product.id,
                    name: product.name,
                    price: product.price,
                    img: product.img || product.image,
                    qty: qty,
                    isService: false
                });
            }
            this.showCartDrawer = true;
            this.cartOpen = true;
        },

        buyNow(product, qty = 1) {
            this.addToCart(product, qty);
        },

        removeFromCart(index) {
            this.cart.splice(index, 1);
        },

        openBookingModalForService(service) {
            let cartService = this.cart.find(i => i.id === service.id && i.isService);
            if (!cartService) {
                cartService = {
                    id: service.id,
                    name: service.name,
                    price: service.price,
                    img: service.img || service.image,
                    qty: 1,
                    isService: true,
                    selectedPet: this.pets.length > 0 ? this.pets[0].name : '',
                    bookingDate: new Date(Date.now() + 86400000).toISOString().split('T')[0],
                    bookingTime: '09:30',
                    bookingBranch: 'Chi nhánh Quận 7 (450 Nguyễn Thị Thập, P. Tân Quy, Q7, TP.HCM)',
                    bookingNotes: ''
                };
                this.cart.push(cartService);
            }
            this.bookingItem = cartService;
            this.showBookingDetailModal = true;
            this.bookingDetailModalOpen = true;
        },

        saveBookingDetails() {
            if (!this.bookingItem.selectedPet || !this.bookingItem.bookingDate) {
                alert('Vui lòng chọn thú cưng và ngày hẹn!');
                return;
            }
            this.showBookingDetailModal = false;
            this.bookingDetailModalOpen = false;
            this.showCartDrawer = true;
            this.cartOpen = true;
            alert('Đã cập nhật thông tin đặt lịch chi tiết cho bé ' + this.bookingItem.selectedPet + ' thành công!');
        },

        // VALIDATION: Bắt buộc điền đủ đặt lịch chi tiết cho dịch vụ trước khi thanh toán
        checkAndOpenCheckout() {
            if (this.cart.length === 0) {
                alert('Giỏ hàng của bạn đang trống! Vui lòng chọn sản phẩm hoặc dịch vụ.');
                return;
            }

            const incompleteService = this.cart.find(item => item.isService && (!item.bookingDate || !item.selectedPet));
            if (incompleteService) {
                alert('⚠️ NHẮC NHỞ: Bạn chưa điền đầy đủ thông tin "Đặt lịch chi tiết" (chọn thú cưng và ngày hẹn) cho dịch vụ: "' + incompleteService.name + '". Vui lòng hoàn tất thông tin để phòng khám chuẩn bị buồng chăm sóc chu đáo trước khi thanh toán!');
                this.openBookingModalForService(incompleteService);
                return;
            }

            this.showCartDrawer = false;
            this.cartOpen = false;
            this.showCheckoutModal = true;
        },

        confirmOrderAndPay() {
            const orderId = 'ORD-' + Math.floor(1000 + Math.random() * 9000);
            const serviceItems = this.cart.filter(item => item.isService);

            // Đồng bộ sang Admin Lịch hẹn
            serviceItems.forEach(serv => {
                this.appointments.unshift({
                    id: 'APT-' + Math.floor(1000 + Math.random() * 9000),
                    customerName: this.checkoutForm.name,
                    customerPhone: this.checkoutForm.phone,
                    petName: serv.selectedPet,
                    petType: 'Thú cưng khách chọn',
                    serviceName: serv.name,
                    date: serv.bookingDate,
                    time: serv.bookingTime || '09:00',
                    branch: serv.bookingBranch || 'Chi nhánh Quận 7',
                    status: 'Đã đặt hẹn',
                    notes: serv.bookingNotes || 'Khách hàng đặt trực tuyến qua SuperApp.'
                });
            });

            // Tạo bản ghi đơn hàng
            this.orders.unshift({
                id: orderId,
                customer: this.checkoutForm.name,
                date: new Date().toISOString().split('T')[0],
                items: this.cart.map(i => i.name + (i.isService ? ' (Dịch vụ)' : ' (x' + i.qty + ')')).join(', '),
                total: this.cartTotal,
                totalAmount: this.cartTotal,
                paymentMethod: this.checkoutForm.paymentMethod === 'vietqr' ? 'Chuyển khoản VietQR' : (this.checkoutForm.paymentMethod === 'momo' ? 'Ví MoMo' : 'COD'),
                status: 'Đã thanh toán',
                branch: 'Q7'
            });

            const earnedPoints = Math.floor(this.cartTotal / 10000);
            this.customerProfile.points += earnedPoints;

            this.cart = [];
            this.showCheckoutModal = false;

            alert('🎉 CHÚC MỪNG QUÝ KHÁCH! Đơn hàng & Lịch hẹn ' + orderId + ' đã được thanh toán thành công! Bạn được cộng thêm ' + earnedPoints + ' điểm thành viên.');
        },

        // XỬ LÝ TẢI ẢNH THÚ CƯNG TỪ THIẾT BỊ (FILEREADER)
        handlePetPhotoUpload(event) {
            const file = event.target.files && event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = (e) => {
                    this.newPetData.avatar = e.target.result;
                    this.petFormError = '';
                };
                reader.readAsDataURL(file);
            }
        },

        // LƯU HỒ SƠ THÚ CƯNG MỚI (KIỂM TRA CẢNH BÁO ĐỎ NẾU CHƯA ĐỦ THÔNG TIN HOẶC CHƯA TẢI ẢNH)
        saveNewPet() {
            // Kiểm tra bắt buộc: Phải có ảnh thú cưng, tên, loài, giống, cân nặng
            if (!this.newPetData.avatar || !this.newPetData.avatar.trim()) {
                this.petFormError = '⚠️ Vui lòng tải ảnh thú cưng lên để hoàn tất nhận diện bé cưng!';
                return;
            }

            if (!this.newPetData.name || !this.newPetData.name.trim() || !this.newPetData.breed || !this.newPetData.weight) {
                this.petFormError = '⚠️ Vui lòng điền đầy đủ các thông tin bắt buộc (Tên bé, loài, giống loài, cân nặng)!';
                return;
            }

            this.petFormError = '';
            const newId = this.pets.length + 1;
            const newPet = {
                id: newId,
                name: this.newPetData.name.trim(),
                type: this.newPetData.type || 'Chó',
                species: this.newPetData.type || 'Chó',
                breed: this.newPetData.breed.trim() || 'Chưa cập nhật',
                gender: this.newPetData.gender || 'Đực',
                age: this.newPetData.age.trim() || 'Mới nhận nuôi',
                weight: String(this.newPetData.weight).trim(),
                chipId: '900118000' + Math.floor(100000 + Math.random() * 900000),
                chip: '900118000' + Math.floor(100000 + Math.random() * 900000),
                avatar: this.newPetData.avatar,
                image: this.newPetData.avatar,
                appearance: this.newPetData.appearance.trim() || 'Ngoại hình khỏe mạnh, đặc điểm nhận dạng đặc trưng',
                health: 'Đã hoàn tất kiểm tra lâm sàng ban đầu',
                allergies: this.newPetData.allergies.trim() || 'Không ghi nhận tiền sử dị ứng thuốc hay thực phẩm',
                diet: this.newPetData.diet.trim() || 'Thức ăn hạt dinh dưỡng theo độ tuổi, nước uống sạch đầy đủ',
                habits: this.newPetData.habits.trim() || 'Thích vui chơi, thói quen sinh hoạt ổn định',
                personality: this.newPetData.personality.trim() || 'Thân thiện, nghe lời chủ nuôi',
                ownerName: this.newPetData.ownerName.trim() || this.customerProfile.name,
                ownerPhone: this.newPetData.ownerPhone.trim() || this.customerProfile.phone,
                ownerAddress: this.newPetData.ownerAddress.trim() || this.customerProfile.address,
                ownerEmergency: this.newPetData.ownerEmergency.trim() || '1900 6868 (Hotline Cấp cứu)',
                isDefault: false,
                lastVaccine: 'Khám lâm sàng ban đầu (' + new Date().toLocaleDateString('vi-VN') + ')',
                nextVaccine: 'Nhắc lại sau 1 tháng',
                vaccines: [
                    { name: 'Khám lâm sàng ban đầu & Sổ tiêm', date: new Date().toLocaleDateString('vi-VN'), doctor: 'ThS.BS Nguyễn Minh Quân', nextDate: 'Hẹn 1 tháng sau', status: 'Đã hoàn thành' }
                ],
                medicalHistory: [
                    { date: new Date().toLocaleDateString('vi-VN'), diagnosis: 'Tạo hồ sơ thú cưng mới trên hệ thống PetCare360', treatment: 'Khám sàng lọc và tư vấn dinh dưỡng ban đầu', notes: 'Bé ngoan, thể trạng ổn định.' }
                ]
            };

            this.pets.push(newPet);
            this.customerProfile.petCount = this.pets.length;
            this.showAddPetModal = false;
            this.addPetModalOpen = false;

            // Reset form
            this.newPetData = {
                name: '',
                type: 'Chó',
                breed: '',
                gender: 'Đực',
                age: '',
                weight: '',
                avatar: '',
                appearance: '',
                allergies: '',
                diet: '',
                habits: '',
                personality: '',
                ownerName: this.customerProfile.name,
                ownerPhone: this.customerProfile.phone,
                ownerAddress: this.customerProfile.address,
                ownerEmergency: '0912 345 678'
            };

            alert('🎉 ĐÃ LƯU HỒ SƠ BÉ CƯNG! Hồ sơ bé ' + newPet.name + ' cùng ảnh chụp đã được hệ thống lưu trữ vĩnh viễn và đồng bộ sang dữ liệu Microchip toàn quốc.');
        },

        deletePet(id) {
            if (confirm('Bạn có chắc muốn xóa hồ sơ thú cưng này không?')) {
                this.pets = this.pets.filter(p => p.id !== id);
                this.customerProfile.petCount = this.pets.length;
                alert('Đã xóa hồ sơ bé thành công.');
            }
        },

        setDefaultPet(id) {
            this.pets.forEach(p => p.isDefault = (p.id === id));
            alert('Đã đặt làm bé cưng mặc định cho các dịch vụ tiếp theo.');
        },

        saveUserProfile() {
            this.showEditProfileModal = false;
            this.editProfileModalOpen = false;
            alert('Thông tin tài khoản và Avatar đại diện của bạn đã được cập nhật thành công!');
        },

        deleteAddress(id) {
            this.addresses = this.addresses.filter(a => a.id !== id);
            alert('Đã xóa địa chỉ thành công.');
        },

        setDefaultAddress(id) {
            this.addresses.forEach(a => a.isDefault = (a.id === id));
            alert('Đã đổi địa chỉ mặc định thành công.');
        },

        // Admin actions
        updateAppointmentStatusDirect(apt, status) {
            apt.status = status;
            alert('Đã cập nhật trạng thái lịch hẹn ' + apt.id + ' sang: "' + status + '"');
        },

        updateOrderStatus(order, status) {
            order.status = status;
            alert('Đã cập nhật trạng thái đơn hàng ' + order.id + ' sang: "' + status + '"');
        },

        adminSaveNewProduct() {
            if (!this.newProdForm.name || !this.newProdForm.price) {
                alert('Vui lòng điền đầy đủ tên sản phẩm và giá bán!');
                return;
            }
            const q1 = Number(this.newProdForm.stockQ1) || 20;
            const bt = Number(this.newProdForm.stockBT) || 15;
            const q7 = Number(this.newProdForm.stockQ7) || 25;
            this.products.unshift({
                id: this.products.length + 1,
                sku: this.newProdForm.sku || 'SKU-' + Math.floor(1000 + Math.random() * 9000),
                name: this.newProdForm.name,
                brand: this.newProdForm.brand || 'PetCare Brand',
                price: parseInt(this.newProdForm.price),
                rating: 5.0,
                reviews: 1,
                reviewsCount: 1,
                sold: 0,
                stockQ1: q1,
                stockBT: bt,
                stockQ7: q7,
                q1: q1, bt: bt, q7: q7,
                category: this.newProdForm.category || 'Thức ăn & Dinh dưỡng',
                categoryAdmin: this.newProdForm.category || 'Thức ăn & Dinh dưỡng',
                img: this.newProdForm.img || 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=500&q=80',
                image: this.newProdForm.img || 'https://images.unsplash.com/photo-1589924691995-400dc9ecc119?auto=format&fit=crop&w=500&q=80',
                desc: this.newProdForm.desc || 'Sản phẩm mới nhập kho chính hãng.',
                description: this.newProdForm.desc || 'Sản phẩm mới nhập kho chính hãng.',
                ingredients: 'Nguyên liệu đạt tiêu chuẩn kiểm nghiệm an toàn thú y quốc tế.',
                usage: 'Sử dụng theo hướng dẫn chi tiết in trên bao bì sản phẩm.'
            });
            this.showAddProductModal = false;
            this.addProductModalOpen = false;
            alert('Đã thêm sản phẩm "' + this.newProdForm.name + '" vào kho hệ thống!');
        },

        adminSaveRestock() {
            if (!this.restockForm.productId) {
                alert('Vui lòng chọn sản phẩm cần nhập thêm!');
                return;
            }
            const prod = this.products.find(p => p.id == this.restockForm.productId);
            if (prod) {
                const addQty = parseInt(this.restockForm.quantity) || 50;
                if (this.restockForm.branch === 'Q1' || this.restockForm.branch === 'HN') {
                    prod.stockQ1 = (Number(prod.stockQ1 || prod.q1) || 0) + addQty;
                    prod.q1 = prod.stockQ1;
                } else if (this.restockForm.branch === 'Q7') {
                    prod.stockQ7 = (Number(prod.stockQ7 || prod.q7) || 0) + addQty;
                    prod.q7 = prod.stockQ7;
                } else {
                    prod.stockBT = (Number(prod.stockBT || prod.bt) || 0) + addQty;
                    prod.bt = prod.stockBT;
                }

                this.showRestockModal = false;
                this.restockModalOpen = false;
                alert('Đã nhập thêm ' + addQty + ' sản phẩm "' + prod.name + '" vào chi nhánh thành công! Tổng tồn kho mới: ' + this.getSafeTotalStock(prod));
            }
        },

        // Chat CSKH
        sendChatMessage() {
            const text = (this.newChatMessage || '').trim();
            if (!text) return;

            this.chatMessages.push({
                sender: 'user',
                text: text,
                time: new Date().toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' })
            });
            this.newChatMessage = '';

            setTimeout(() => {
                const box = document.getElementById('chat-messages-box');
                if (box) box.scrollTop = box.scrollHeight;
            }, 50);

            setTimeout(() => {
                let reply = 'Cảm ơn quý khách đã liên hệ! Bác sĩ thú y trực ban đã ghi nhận tình trạng của bé và sẽ phản hồi chi tiết trong ít phút.';
                const lower = text.toLowerCase();
                if (lower.includes('tiêm') || lower.includes('vắc xin') || lower.includes('vaccine')) {
                    reply = 'Dạ về lịch tiêm phòng, PetCare360 hiện có sẵn đầy đủ vắc-xin 7 bệnh chó và 4 bệnh mèo nhập khẩu từ Pháp và Mỹ. Bác sĩ luôn khám sàng lọc miễn phí trước khi tiêm. Bạn có thể đặt lịch ngay trong mục Dịch Vụ nhé!';
                } else if (lower.includes('spa') || lower.includes('tắm') || lower.includes('tỉa')) {
                    reply = 'Dạ gói Spa Cắt Tỉa Lông chuẩn 5 bước tại PetCare360 đang có ưu đãi tặng sấy ion âm dưỡng lông và vệ sinh tai móng trọn gói. Bạn muốn đặt lịch cho bé vào ngày nào ạ?';
                } else if (lower.includes('cấp cứu') || lower.includes('khẩn cấp') || lower.includes('ngộ độc')) {
                    reply = '🚨 BÁC SĨ CẤP CỨU ĐANG KẾT NỐI: Vui lòng giữ bình tĩnh, đặt bé nằm nghiêng nơi thoáng mát. Đội xe cấp cứu PetCare360 có thể đón bé ngay qua hotline khẩn cấp 1900 6868!';
                }

                this.chatMessages.push({
                    sender: 'bot',
                    text: reply,
                    time: new Date().toLocaleTimeString('vi-VN', { hour: '2-digit', minute: '2-digit' })
                });

                setTimeout(() => {
                    const box = document.getElementById('chat-messages-box');
                    if (box) box.scrollTop = box.scrollHeight;
                }, 50);
            }, 600);
        },

        sendQuickChat(promptText) {
            this.newChatMessage = promptText;
            this.sendChatMessage();
        },

        setOrderTypeFilter(type) {
            this.currentOrderTypeTab = type;
        },

        showToast(msg) {
            alert(msg);
        },

        toggleDarkMode() {
            // Deprecated as per user request
        },

        refreshChart() {
            alert('Đã cập nhật số liệu biểu đồ phân tích thời gian thực!');
            this.renderRevenueChart();
        },

        scrollToUrgentTasks() {
            const el = document.getElementById('urgent-tasks-section');
            if (el) el.scrollIntoView({ behavior: 'smooth' });
        }
    };
}
</script>
'''
