from pydantic import BaseModel


class BidResponse(BaseModel):
    bid_amount: int

    class Config:
        """Configuration for the BidResponse schema."""
        extra = "forbid"  # Forbid extra fields
        allow_inf_nan = False  # Don't allow infinity values
        # title = "Auction Bid Response"
        # description = "A response containing a bid amount for an auction"
        # schema_extra = {
        #     "examples": [
        #         {
        #             "bid_amount": 100
        #         }
        #     ]
        # } 