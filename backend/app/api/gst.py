from fastapi import APIRouter
from app.utils.gst import calculate_gst

router = APIRouter(
    prefix="/gst",
    tags=["GST"]
)

@router.get("/calculate")
def gst_calculator(
    amount: float,
    gst_rate: float,
    intra_state: bool = True
):
    return calculate_gst(amount, gst_rate, intra_state)