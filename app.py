import streamlit as st

from src.agent.config import get_ai_settings
from src.agent.tasks import get_task_areas
from src.agent.workflow import run_workflow
from src.agent.history import get_history, save_history

st.set_page_config(
    page_title="Teacher Assistant Agent",
    page_icon="📚",
    layout="centered",
)

st.title("📚 Teacher Assistant Agent")
st.write("Asisten AI untuk membantu pekerjaan guru SMP/MTs.")

st.info(
    "Prototipe ini masih dalam tahap pengembangan. "
    "Periksa setiap hasil AI sebelum digunakan."
)

try:
    settings = get_ai_settings()
    st.caption(
        f"Provider aktif: {settings.provider} · Model: {settings.model}"
    )
except ValueError as exc:
    st.warning(f"Konfigurasi AI belum siap: {exc}")

st.subheader("Buat konten pembelajaran")

area_pekerjaan = st.selectbox(
    "Area pekerjaan guru",
    ["Pilih area pekerjaan", *get_task_areas()],
)

instruksi = st.text_area(
    "Instruksi",
    placeholder="Contoh: Buat materi IPA tentang ekosistem untuk kelas VII.",
    max_chars=5000,
    help="Masukkan instruksi yang ingin diproses oleh AI.",
)

if st.button("Jalankan AI", type="primary"):
    if area_pekerjaan == "Pilih area pekerjaan":
        st.warning("Silakan pilih area pekerjaan guru terlebih dahulu.")
    else:
        with st.spinner("AI sedang memproses instruksi..."):
            hasil = run_workflow(instruksi, area_pekerjaan)

        if hasil.success:
            st.success(hasil.message)

            save_history(
                task_area=area_pekerjaan,
                instruction=instruksi.strip(),
                content=hasil.content,
            )
            st.subheader("Hasil AI")
            st.markdown(hasil.content)

            if hasil.requires_review:
                st.info(
                    "Tinjau akurasi, kesesuaian materi, dan tingkat "
                    "kesulitan sebelum menggunakan hasil ini."
                )
        else:
            st.error(hasil.message)

st.divider()
st.subheader("📚 Riwayat Hasil AI")

try:
    riwayat = get_history(limit=20)

    if not riwayat:
        st.caption("Belum ada riwayat hasil AI.")
    else:
        for item in riwayat:
            with st.expander(
                f"#{item['id']} · {item['task_area']} · {item['created_at']}"
            ):
                st.markdown("**Instruksi:**")
                st.write(item["instruction"])
                st.markdown("**Hasil:**")
                st.markdown(item["content"])

except Exception:
    st.error("Gagal memuat riwayat hasil AI.")